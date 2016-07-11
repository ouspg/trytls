{-# LANGUAGE OverloadedStrings #-}

module Main where

import           Control.Exception          (SomeException, catch)
import           Control.Monad              (when)
import           System.Environment         (getArgs, getProgName)
import           System.Exit                (exitFailure, exitSuccess)

import           Network.HTTP.Client        (HttpException (..), httpLbs,
                                             newManager, parseRequest)
import           Network.HTTP.Client.TLS    (mkManagerSettings)

import           Data.X509.CertificateStore (CertificateStore,
                                             readCertificateStore)
import           System.X509                (getSystemCertificateStore)

import           Network.Connection
import           Network.TLS
import           Network.TLS.Extra.Cipher   (ciphersuite_all)

main :: IO ()
main = do
  args <- getArgs
  let argc = length args
  when (argc < 2 || argc > 3) $ do
    prog <- getProgName
    putStrLn $ prog ++ " <host> <port> [ca-bundle]"
    exitFailure

  let host = args !! 0
      port = args !! 1
      url = "https://" ++ host ++ ":" ++ port

  caBundle <- if argc == 3
              then do cas <- readCertificateStore (args !! 2)
                      case cas of
                        (Just _) -> return cas
                        _        -> do
                          putStrLn $ "Error: Invalid ca-bundle in " ++ args !! 2
                          exitFailure
              else fmap Just getSystemCertificateStore

  let params = injectCiphers . injectCA caBundle $ defaultParamsClient host ""

  manager <- newManager $ mkManagerSettings (TLSSettings params) Nothing
  request <- parseRequest url

  r <- catch (httpLbs request manager)
             (\exception -> do
                 let _ = exception :: SomeException
                 putStrLn "VERIFY FAILURE"
                 exitSuccess
             )

  putStrLn "VERIFY SUCCESS"
  exitSuccess

injectCA :: Maybe CertificateStore -> ClientParams -> ClientParams
injectCA caBundle p =
  case caBundle of
    Nothing -> p
    Just ca -> p { clientShared = shared { sharedCAStore = ca } }
  where
    shared = clientShared p

injectCiphers :: ClientParams -> ClientParams
injectCiphers p =
  p { clientSupported = supported { supportedCiphers = ciphersuite_all } }
  where
    supported = clientSupported p

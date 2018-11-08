{-# LANGUAGE OverloadedStrings #-}

module Main where

import           Control.Exception          (catch)
import           Control.Monad              (when)
import           Data.ByteString.Char8      (unpack)
import           System.Environment         (getArgs, getProgName)
import           System.Exit                (exitFailure, exitSuccess)

import           Network.HTTP.Client        (HttpException (..),
                                             HttpExceptionContent(..),
                                             httpLbs,
                                             newManager, parseRequest,
                                             responseStatus)
import           Network.HTTP.Client.TLS    (mkManagerSettings)
import           Network.HTTP.Types.Status  (statusCode, statusMessage)

import           Data.X509.CertificateStore (CertificateStore,
                                             readCertificateStore)
import           System.X509                (getSystemCertificateStore)

import           Network.Connection         (TLSSettings (..))
import           Network.TLS                (ClientParams, clientShared,
                                             clientSupported,
                                             defaultParamsClient, sharedCAStore,
                                             supportedCiphers)
import           Network.TLS.Extra.Cipher   (ciphersuite_default)

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

  _ <- catch (doGet request manager)
             (\exp' -> case exp' of
               HttpExceptionRequest _req (InternalException e) -> do
                 print e
                 putStrLn "REJECT"
                 exitSuccess
               e -> do
                 print e
                 exitFailure
             )
  return ()
  where
    doGet request manager = do
      r <- httpLbs request manager
      let status = responseStatus r
          code   = statusCode status
          msg    = statusMessage status
      putStrLn (show code ++" "++ unpack msg)
      putStrLn "ACCEPT"
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
  p { clientSupported = supported { supportedCiphers = ciphersuite_default } }
  where
    supported = clientSupported p

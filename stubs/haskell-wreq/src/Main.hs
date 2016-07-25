{-# LANGUAGE OverloadedStrings #-}

module Main where

import Data.ByteString.Char8 (unpack)
import Control.Exception (catch)
import Control.Monad (when)
import System.Environment (getArgs, getProgName)
import System.Exit (exitSuccess, exitFailure)

import Network.Wreq
import Control.Lens ((^.))
import Network.HTTP.Client (HttpException(TlsExceptionHostPort))

main :: IO ()
main = do
  args <- getArgs
  let argc = length args
  when (argc /= 2 && argc /= 3) $ do
    prog <- getProgName
    putStrLn $ prog ++ " <host> <port> [ca-bundle]"
    exitFailure

  when (argc == 3) $ do
    putStrLn "UNSUPPORTED"
    exitSuccess

  let host = args !! 0
      port = args !! 1

  catch
    (doGet $ "https://" ++ host ++ ":" ++ port)
    (\(TlsExceptionHostPort e _ _) -> do
        print e
        putStrLn "VERIFY REJECT"
        exitSuccess
    )
  where
    doGet :: String -> IO ()
    doGet url = do
      r <- get url
      let code = r ^. responseStatus . statusCode
          msg  = r ^. responseStatus . statusMessage
      putStrLn (show code ++" "++ unpack msg)
      putStrLn "VERIFY ACCEPT"
      exitSuccess

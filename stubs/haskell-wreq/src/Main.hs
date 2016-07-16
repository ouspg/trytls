{-# LANGUAGE OverloadedStrings #-}

module Main where

import Data.ByteString.Char8 (unpack)
import Control.Exception (catch, SomeException)
import Control.Monad (when)
import System.Environment (getArgs, getProgName)
import System.Exit (exitSuccess, exitFailure)

import Network.Wreq
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

  r <- catch (get $ "https://" ++ host ++ ":" ++ port)
             (\exception -> do
                 let (TlsExceptionHostPort exp _ _) = exception
                 putStrLn (show exp)
                 putStrLn "VERIFY FAILURE"
                 exitSuccess
             )

  putStrLn "VERIFY SUCCESS"
  exitSuccess

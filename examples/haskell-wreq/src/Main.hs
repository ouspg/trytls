{-# LANGUAGE OverloadedStrings #-}

module Main where

import Control.Exception (catch, SomeException)
import Control.Monad (when)
import System.Environment (getArgs, getProgName)
import System.Exit (exitSuccess, exitFailure)

import Network.Wreq

main :: IO ()
main = do
  args <- getArgs
  let argc = length args
  when (argc /= 2 && argc /= 3) $ do
    prog <- getProgName
    putStrLn $ prog ++ " <host> <port> [ca-bundle]"
    exitFailure

  let host = args !! 0
      port = args !! 1

  r <- catch (get $ "https://" ++ host ++ ":" ++ port)
    (\exception -> do
        let _ = exception :: SomeException
        putStrLn "OK"
        exitSuccess
        )

  putStrLn "FAIL"

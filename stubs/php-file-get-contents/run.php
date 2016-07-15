#!/usr/bin/php
<?php

if ($argc < 3 || $argc > 4 || in_array($argv[1], array('--help', '-h'))) {
  echo "Usage: " . $argv[0] . " <host> <port> [ca-bundle]" . "\n";
  exit(1);
}

$host = $argv[1];
$port = $argv[2];

if ($argc > 3) {
  $cabundle = $argv[3];
  echo "UNSUPPORTED" . "\n";
  exit(0);
}

if( !ini_get('allow_url_fopen') ) {
  echo "Error: " . "allow_url_fopen not set " . "cannot fetch remote urls" . "\n";
  echo "UNSUPPORTED" . "\n";
  exit(0);
}

$arrContextOptions = array(
  "ssl" => array(
    "verify_peer" => true,
    "verify_peer_name" => true,
  ),
);

$filename = "https://" . $host . ":" . $port;

function mywarning($errno, $errstr, $errfile, $errline, array $errcontext) {
  if (!error_reporting()) {
    return false;
  }
  throw new ErrorException($errstr, 0, $errno, $errfile, $errline);
}

set_error_handler('mywarning', E_WARNING);

try {
  $page = file_get_contents($filename, false, stream_context_create($arrContextOptions));
} catch (Exception $e) {
  // echo $e->getMessage() . "\n";
  // bail out early here and don't tust return value only
  echo ("VERIFY FAILURE" . "\n");
  exit(0);
}

if ($page) {
  echo ("VERIFY SUCCESS" . "\n");
} else {
  echo ("VERIFY FAILURE" . "\n");
}
?>

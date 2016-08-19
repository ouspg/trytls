if ($args.length -lt 2) {
   Write-Host "Usage: powershell run.ps1 <HOST> <PORT>";
   exit
} if ($args.length -gt 2) {
  Write-Host "UNSUPPORTED"
  exit
}

try {
    $progressPreference = 'silentlyContinue' 
    $r = Invoke-Webrequest https://$($args[0]):$($args[1])/  
    Write-Host "ACCEPT"
} catch { 
  Write-Host "REJECT" 
}


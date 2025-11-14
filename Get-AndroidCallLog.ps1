# A simple script to grab Android call logs using adb
# Reminder to make sure the phone you are testing on has developer mode and USB debugging on
$platformTools = "C:\platform-tools"
$adb = Join-Path $platformTools "adb.exe"

Write-Host "Using adb at: $adb"
Write-Host ""

# Check adb version
Write-Host "Checking adb version..."
& $adb version
Write-Host ""

# List connected devices
Write-Host "Listing connected devices..."
& $adb devices
Write-Host ""
Write-Host "If your phone is not listed, make sure:"
Write-Host " - USB debugging is enabled"
Write-Host " - You allowed the computer on your phone"
Write-Host ""

# Export call log to a raw text file in the current folder
Write-Host "Exporting call log to calllog_raw.txt ..."
& $adb shell "content query --uri content://call_log/calls" > "calllog_raw.txt"

Write-Host "Done. Raw call log saved as calllog_raw.txt"
Write-Host ""
Write-Host "Next step (run manually):"
Write-Host "  python convert_calllog_to_csv.py"

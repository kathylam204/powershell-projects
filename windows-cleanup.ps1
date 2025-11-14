<#
Empties the Recycle Bin
Cleans user & system TEMP files
Uses -Force and SilentlyContinue to avoid interruptions
Requires running PowerShell as Administrator
Use this script with caution
#>

Clear-RecycleBin -Force

Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue #User

Remove-Item -Path "C:\Windows\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue #System

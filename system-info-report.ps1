<#
Gather detailed computer information
Then it saves to a text file
Export it to a CSV format
Convert it to an HTML format
#>
$computerInfo = Get-ComputerInfo

$computerInfo | Out-File -FilePath "C:\Temp\ComputerInfo.txt"

$computerInfo | Export-Csv -Path "C:\Temp\ComputerInfo.csv" -NoTypeInformation

$computerInfo | ConvertTo-Html | Out-File -FilePath "C:\Temp\ComputerInfo.html"

Write-Host "Computer info saved to: C:\Temp\ComputerInfo.txt, C:\Temp\ComputerInfo.csv, and C:\Temp\ComputerInfo.html"

# https://learn.microsoft.com/fr-fr/troubleshoot/windows-server/user-profiles-and-logon/turn-on-automatic-logon
if(-not(query session jesus.garcia /server:warehouse-srv02)) {
  #kill process if exist
  Get-Process mstsc -IncludeUserName | Where {$_.UserName -eq "NORTH\jesus.garcia"}|Stop-Process
  #run the command
  mstsc /v:warehouse-srv02
}
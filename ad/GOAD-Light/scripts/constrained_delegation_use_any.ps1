# https://www.thehacker.recipes/ad/movement/kerberos/delegations/constrained#with-protocol-transition
Set-ADUser -Identity "juan.iniesta" -ServicePrincipalNames @{Add='CIFS/finance-dc02.north.dynamo.local'}
Get-ADUser -Identity "juan.iniesta" | Set-ADAccountControl -TrustedToAuthForDelegation $true
Set-ADUser -Identity "juan.iniesta" -Add @{'msDS-AllowedToDelegateTo'=@('CIFS/finance-dc02.north.dynamo.local','CIFS/finance-dc02')}
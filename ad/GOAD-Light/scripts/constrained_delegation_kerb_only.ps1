# https://www.thehacker.recipes/ad/movement/kerberos/delegations/constrained#without-protocol-transition
Set-ADComputer -Identity "warehouse-srv02$" -ServicePrincipalNames @{Add='HTTP/finance-dc02.north.dynamo.local'}
Set-ADComputer -Identity "warehouse-srv02$" -Add @{'msDS-AllowedToDelegateTo'=@('HTTP/finance-dc02.north.dynamo.local','HTTP/finance-dc02')}
# Set-ADComputer -Identity "warehouse-srv02$" -Add @{'msDS-AllowedToDelegateTo'=@('CIFS/finance-dc02.north.dynamo.local','CIFS/finance-dc02')}
Get-ADUser -Identity "vicente.garcia" | Set-ADAccountControl -DoesNotRequirePreAuth:$true
function listDomains ($apiBase, $headers) {
	$apiURL = $apiBase + "domains"
	$domains = ((Invoke-WebRequest -URI $apiURL -Headers $headers).content | ConvertFrom-JSON).domains
	
	$output = @()
	
	foreach ($domain in $domains) {
		$domainObject = New-Object -TypeName PSObject
		$domainObject | Add-Member -MemberType NoteProperty -Name "domain" -Value $domain
		$output += $domainObject
	}
	
	return $output.domain.name
}
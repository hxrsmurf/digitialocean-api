function getDomainRecords ($domains) {
	foreach ($domain in $domains.domain){
		listDomainRecords $domain.name $true
	}
}

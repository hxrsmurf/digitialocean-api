function listDomainRecords ($apiBase, $headers, $domain, $save) {
	if ($domain.length -eq 0){
		Write-Host "No input"
		return
	}

	$output = @()
	$apiURL = $apiBase + "domains/" + $domain + "/records"
	$records = ((Invoke-WebRequest -URI $apiURL -Headers $headers).content | ConvertFrom-JSON).domain_records
	
	foreach ($record in $records){
		$recordObject = New-Object -TypeName PSObject
	
		$recordInfo = [ordered]@{
			id = $record.id
			type = $record.type
			name = $record.name
			data = $record.data
		}
	
		foreach($key in $recordInfo.keys) {
			$recordObject | Add-Member -MemberType NoteProperty -Name $key -Value $recordInfo[$key]
		}
		$output += $recordObject
	}
	
	if ($save -eq $true){
		$fileDate = Get-Date -format "yyyyMMdd-HHmm"
		
		$folderPath =  "$(pwd)\reports\"
		if (! (Test-Path $folderPath)){
			New-Item -Path $folderPath -ItemType "directory"
		}
	
		$fileName = $folderPath + $domain + "-records-" + $fileDate + ".csv"
		Write-Host $fileName
		$output | Export-CSV -Delimiter "|" -NoTypeInformation -Path $fileName
		return $output
	}
	
	return $output
}
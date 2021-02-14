function getDroplets ($apiBase, $headers, $save) {
	# Need to update to support multiple droplets
	
	$apiURL = $apiBase + "droplets"

	$request = ((Invoke-WebRequest -URI $apiURL -Method GET -Headers $headers).content | ConvertFrom-JSON).droplets
	
	$output = @()
	
	foreach ($r in $request){
		$dropletObject = New-Object -TypeName PSObject
		$networks = @()
		
		foreach ($network in $request.networks.v4){
			$networkObject = New-Object -TypeName PSObject
		
			if ($network.gateway){
				$gateway = $network.gateway
			} else {
				$gateway = "null"
			}
			
			$networkInfo = [ordered]@{
				ipAddress = $network.ip_address
				subnet = $network.netmask
				gateway = $gateway
			}		
			
			foreach($key in $networkInfo.keys) {
				$networkObject | Add-Member -MemberType NoteProperty -Name $key -Value $networkInfo[$key]
			}
			
			$networks += $networkObject
		}		
		
		foreach ($n in $networks){
			$networkArray += $n.ipAddress + "," + $n.subnet + "," + $n.gateway + ";"
		}
		
		$dropletInfo = [ordered]@{
			dropletID = $r.id
			dropletName = $r.name
			dropletMemory = $r.memory
			dropletVCPUs = $r.vcpus
			dropletDisk = $r.disk
			dropletStatus = $r.status
			dropletNetworks = $networkArray
		}		
	}	
	
	foreach($key in $dropletInfo.keys) {
		$dropletObject | Add-Member -MemberType NoteProperty -Name $key -Value $dropletInfo[$key]
	}
	
	$output += $dropletObject
	
	if ($save -eq $true){
		$fileDate = Get-Date -format "yyyyMMdd-HHmm"
		
		$folderPath =  "$(pwd)\reports\"
		if (! (Test-Path $folderPath)){
			New-Item -Path $folderPath -ItemType "directory"
		}
		
		$fileDate = Get-Date -format "yyyyMMdd-HHmm"
		$fileName = $folderPath + "Droplets-" + $fileDate + ".csv"
		Write-Host "Saving $fileName"
		$output | Export-CSV -Delimiter "|" -NoTypeInformation -Path $fileName
	}
	return $output
}
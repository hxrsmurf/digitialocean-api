function environment {
	$configFile = Import-Csv "Config\config.csv"
	$config = @{}
	
	foreach ($c in $configFile){
		switch ($c.name){
			"api_token" { $config.apiToken = $c.value }
			"key" { $config.sshKey = $c.value }
			"home" { $config.homeName = $c.value }
			"apiBase" { $config.apiBase = $c.value }
		}
	}	
	return $config
}
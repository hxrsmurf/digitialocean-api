function login ($apiToken){
	$bearerToken = "Bearer " + $apiToken

	$headers = @{
		"Content-Type" = "application/json"
		"Authorization" = $bearerToken
	}
	
	return $headers
}
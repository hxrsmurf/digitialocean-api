function importFunctions {
	$functions = Get-ChildItem . | Select FullName
	foreach ($function in $functions.FullName){
			. $function
	}
}
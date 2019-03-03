<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>admin</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href='css/buttons.css' rel='stylesheet' type="text/css">
</head>
<body>
    <center>
        <form action="6af3223f1176293c.php" method="GET">
                <input type='text' placeholder='127.0.0.1' name='ip'>
				<input type="submit" value="Go" class="button button-pill button-primary">
        </form>
    </center>

</body>
</html>
<?php
error_reporting(0);
	// Get input

	$target = $_REQUEST[ 'ip' ];
    // var_dump($target);
	$target=trim($target);
	// var_dump($target);
	// Set blacklist
	$substitutions = array(
		'&'  => '',
		';' => '',
		'|' => '',
		'-'  => '',
		'$'  => '',
		'('  => '',
		')'  => '',
		'`'  => '',
		'||' => '',
	);

	// Remove any of the charactars in the array (blacklist).
	$target = str_replace( array_keys( $substitutions ), $substitutions, $target );
    

	// var_dump($target);

	// Determine OS and execute the ping command.
	if( stristr( php_uname( 's' ), 'Windows NT' ) ) {
		// Windows
		
		$cmd = shell_exec( 'ping  ' . $target );
	}
	else {
		// *nix
		$cmd = shell_exec( 'ping  -c 1 ' . $target );
	}

	// Feedback for the end user
	echo  "<pre>{$cmd}</pre>";
	

?>

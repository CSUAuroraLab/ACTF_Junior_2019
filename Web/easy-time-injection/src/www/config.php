<?php  
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "blind_time_injection";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("连接失败: ");
}

function stop_hack($value){
	$pattern = "insert|delete|or|concat|concat_ws|group_concat|join|floor|\/\*|\*|\.\.\/|\.\/|union|into|load_file|outfile|dumpfile|sub|hex|file_put_contents|fwrite|curl|system|eval";
	$back_list = explode("|",$pattern);
	foreach($back_list as $hack){
		if(preg_match("/$hack/i", $value))
			die("$hack detected!");
	}
	return $value;
}
?>
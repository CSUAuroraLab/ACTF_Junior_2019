<?php
include 'config.php';

$id = $_GET['id'];
$sql = "select * from users where id=".$id;

$res = $conn->query($sql);

if($res){
    if($res->num_rows > 0) { 
        //echo "This user exists.<br>"; 
    } else { 
        //echo "This user doesn't exist.<br>"; 
    } 
}else{ 
        //echo "Error in query.<br>"; 
    } 
$conn->close();

highlight_file(__FILE__);

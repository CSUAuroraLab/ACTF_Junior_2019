<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>XXE</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href='css/buttons.css' rel='stylesheet' type="text/css">
</head>
<body>
    <p>读取根目录的flag文件</p>
    <center>
       <textarea name="data" form="data" rows="10" cols="60" >请在此处输入payload</textarea> 
        <form action="index.php" method="POST" id='data'>
                <br>
                <input type='submit' class="button button-rounded button-large" value='Go'> 
        </form>
    </center>

</body>
</html>
<?php
error_reporting(0);
if(isset($_POST['data'])){
    $data = $_POST['data'];
    // echo $data;
    $xml = simplexml_load_string($data);
    
    echo $xml->name;
}

// highlight_file(__FILE__);
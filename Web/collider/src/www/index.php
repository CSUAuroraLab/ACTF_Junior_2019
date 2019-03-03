<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Md5 collision</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<p>请上传两个md5一样的PDF，第一个包含字符串“Give Me”，第二个包含字符串“ACTF Flag”</p>
<br>
<form action="index.php" method="post" enctype="multipart/form-data">
    <label for="file">PDF1:</label>
    <input type="file" name="pdf1"  />
    <br />
    <label for="file">PDF2:</label>
    <input type="file" name="pdf2"  />  
    <br />
    <input type="submit" name="submit" value="Submit" />
</form>
</body>
</html>
<?php
include_once "config.php";
if (isset($_POST['submit'])) {
    $pdf1 = $_FILES['pdf1']['tmp_name'];
    $pdf2 = $_FILES['pdf2']['tmp_name'];

    if (!strstr(shell_exec("pdftotext $pdf1 - | head -n 1 | grep -oP '^Give Me$'"), "Give Me")) {
        die("The first pdf does not contain 'Give Me'");
    }

    if (!strstr(shell_exec("pdftotext $pdf2 - | head -n 1 | grep -oP '^ACTF Flag$'"), "ACTF Flag")) {
        die("The second pdf does not contain 'ACTF Flag'");
    }

    if (md5_file($pdf1) != md5_file($pdf2)) {
        die("The MD5 hashes do not match!");
    }

    echo "$FLAG";

}
?>
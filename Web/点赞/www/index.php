<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>点赞</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href='css/buttons.css' rel='stylesheet' type="text/css">
</head>
<body>
    <p>一分钟猛击6666次即可获得大宝剑</p>
    <center>
        <form action="index.php" method="POST">
                <input type='hidden' value='have fun' name='just'>
                <button class="button button-3d button-action button-circle button-jumbo" style="width: 300px;height: 300px"><i class="fa fa-thumbs-up"></i>点赞</button>
               
        </form>
    </center>

</body>
</html>

<?php
function my_session_start($timeout = 1440) {
    ini_set('session.gc_maxlifetime', $timeout);
    session_start();

    if (isset($_SESSION['timeout_idle']) && $_SESSION['timeout_idle'] <= time()) {
        session_destroy();
        session_start();
        session_regenerate_id();
        $_SESSION = array();
        $_SESSION['timeout_idle'] = time() + $timeout;
        return ;
    }else if (isset($_SESSION['timeout_idle']) && $_SESSION['timeout_idle'] > time()){
        return ;
    }
    $_SESSION['timeout_idle'] = time() + $timeout;
}


my_session_start(60);

if(isset($_SESSION['like'])){
    if(isset($_POST['just'])){
        $_SESSION['like']=$_SESSION['like']+1;

    }
    
}
else{
    $_SESSION['like']=1;
}
  
echo "点赞：". $_SESSION['like'];
echo "<br>截止时间：".date('Y-m-d H:i:s', $_SESSION['timeout_idle'] + 8*3600);

echo "<br>";
if($_SESSION['like'] > 6665 ){
    die("ACTF{python_is_very_cooooooooool!!!}");
}

// session_destroy()
?>
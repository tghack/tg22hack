<?php

if ( isset($_GET['page'] ) ){
    $file = $_GET[ 'page' ];
} else {
    $file = '?page=index.html';
    header('Location: '.$file);
    die();
    
}

include $file;

?>
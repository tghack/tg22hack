<?php

if ( isset($_GET['page'] ) ){
    $file = $_GET[ 'page' ];
    $file = str_replace( array( "http://", "https://" ), "", $file );
    $file = str_replace( array( "../", "..\\" ), "", $file );
    if ( $file === '/flag' ){
        $file = 'sorry.txt';
    }
} else {
    $file = '?page=index.html';
    header('Location: '.$file);
    die();
    
}

include $file;

?>
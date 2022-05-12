<?php


//Make sure that it is a POST request.
if(strcasecmp($_SERVER['REQUEST_METHOD'], 'POST') != 0){
    echo 'Request is not POST';
} else {

    //Receive the RAW post data.
    $content = trim(file_get_contents("php://input"));

    //Attempt to decode the incoming RAW post data from JSON.
    $decoded = json_decode($content, true);

    //If json_decode failed, the JSON is invalid.
    if(!is_array($decoded)){
        echo 'Received content contained invalid JSON!';
        die();
    }

    //Make sure that the content type of the POST request has been set to application/json
    $contentType = isset($_SERVER["CONTENT_TYPE"]) ? trim($_SERVER["CONTENT_TYPE"]) : '';
    if(strcasecmp($contentType, 'application/json') != 0){
        echo "Data and content type does not match";
        die();
    }    

    echo "Good input! -> ";
    echo $decoded['input'];
    echo "\r\n";
    include '/flag';
}
/*
if ( isset($_POST['input'] ) ){
    echo "Got some data";
}
*/


?>
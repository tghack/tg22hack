<?php

$lat=(float)$_REQUEST["lat"];
$long=(float)$_REQUEST["long"];

// Viktingskipet:
// lat, long
// 60.7929008,11.1011103

// Lat > 60.7918
// Lat < 60.7942

// long > 11.10
// long < 11.103

if ($lat<=60.7942 && $lat>=60.7918){
    if ($long<=11.103 && $long>=11.10){
        echo "TG22{verdens_beste_og_største_påske_hytte}";
    }
    else{
        echo "You're very close but not quite home yet!";
    }
}
else{
    echo "You're not home :(";
}


?>
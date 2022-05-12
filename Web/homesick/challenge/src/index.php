<!DOCTYPE html>
<!--[if lt IE 8 ]><html class="no-js ie ie7" lang="en"> <![endif]-->
<!--[if IE 8 ]><html class="no-js ie ie8" lang="en"> <![endif]-->
<!--[if (gte IE 8)|!(IE)]><!--><html class="no-js" lang="en"> <!--<![endif]-->
<head>

   <!--- Basic Page Needs
   ================================================== -->
   <meta charset="utf-8">
	<title>Homesick</title>
	<meta name="description" content="">
	<meta name="author" content="">

   <!-- Mobile Specific Metas
   ================================================== -->
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

	<!-- CSS
    ================================================== -->
   <link rel="stylesheet" href="css/default.css">
	<link rel="stylesheet" href="css/layout.css">
   <link rel="stylesheet" href="css/media-queries.css">    

   <!-- Script
   ================================================== -->
	<script src="js/modernizr.js"></script>

   <!-- Favicons
	================================================== -->
	<link rel="shortcut icon" href="favicon.png" >

</head>

<body>

   <!-- Intro Section
   ================================================== -->
   <section id="intro">	

   	<div  id="main" class="row" style="text-align:center">
	   
	   		<br>
			<br>
			<br>
			<br>
			<br>
			<br>
			<br>
			<br>
			<br>
			<br>
			<br>
	   		<h1>Can you find your way back here?</h1>
			
			<button onclick="getLocation()">Check location</button>
			
			<h5 id="flag_position"></h5>

			   <script>
			   var x = document.getElementById("flag_position");
			   function getLocation() {
				 if (navigator.geolocation) {
				   navigator.geolocation.getCurrentPosition(showPosition);
				 } else { 
				   x.innerHTML = "Geolocation is not supported by this browser.";
				 }
			   }
			   
			   function showPosition(position) {
				 x.innerHTML = "Latitude: " + position.coords.latitude +
				 "<br>Longitude: " + position.coords.longitude;
				 //document.cookie = "longitude="+position.coords.longitude
				 //document.cookie = "latitude="+position.coords.latitude
				 //location.reload();
				   var xmlhttp = new XMLHttpRequest();
				   xmlhttp.onreadystatechange = function() {
					 if (this.readyState == 4 && this.status == 200) {
						 // when done
						 x.innerHTML = this.responseText;
					 }
				   };
				   xmlhttp.open("GET", "api.php?long="+position.coords.longitude+"&lat="+position.coords.latitude);
				   xmlhttp.send();
			   }
			   </script>
         

      </div> <!-- main end -->    	
   </section> <!-- end intro section -->
 

   <!-- Java Script
   ================================================== 
   <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
   <script>window.jQuery || document.write('<script src="js/jquery-1.10.2.min.js"><\/script>')</script>
   <script type="text/javascript" src="js/jquery-migrate-1.2.1.min.js"></script>
	<script src="js/gmaps.js"></script>
   <script src="js/waypoints.js"></script>
   <script src="js/jquery.countdown.js"></script>
   <script src="js/jquery.placeholder.js"></script>
   <script src="js/backstretch.js"></script>  
   <script src="js/init.js"></script>
   -->
</body>

</html>
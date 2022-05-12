<h1>Fresh out of the box</h1>
Can you find the file related to these two images?
<br>
<img src="2u8mqwgrfgp61.jpg" style="max-width: 33%">
<img src="Windows XP Professional CD.jpg" style="max-width: 33%">
<br>
Select file:
<br>
<input type="file" id="file">
<input type="submit" id="submit">
<form method="post" id="form">
  <input type="hidden" name="data" id="data">
  <input type="hidden" name="name" id="name">
  <input type="hidden" name="size" id="size">
</form>
<script>
document.getElementById('submit').addEventListener('click', function() {
  var files = document.getElementById('file').files;
  if (files.length > 0) {
    getBase64(files[0]);
  }
});

function getBase64(file) {
   var reader = new FileReader();
   reader.readAsDataURL(file);
   reader.onload = function () {
     console.log(reader.result);
     document.getElementById("data").value = reader.result;
     document.getElementById("name").value = file.name;
     document.getElementById("size").value = file.size;
     document.getElementById("form").submit();
   };
   reader.onerror = function (error) {
     console.log('Error: ', error);
   };
}
</script>
<?php

if (isset($_POST["data"]) AND isset($_POST["name"]) AND isset($_POST["size"])) {

  $hash = md5(base64_decode(substr($_POST["data"], strpos($_POST["data"], "base64,") + 7)));

  if ($hash == "c6bdf7f703f0fc47df6485467b6fd069"){
    echo "TG22{3k73_84ng3rRR}";
  } elseif ($_POST["name"] == "title.wma" AND ($_POST["size"] >= 2600000 OR $_POST["size"] <= 2650000)) {
    echo "You have to get the unmodified original file!";
  } else {
    echo "Wrong file!";
  }

}

?>

<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "goodlooks_database";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
// echo "Connected successfully";


?>

<style>

body {
  font-family: "Poppins", sans-serif;
}

</style>


<div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel">
  <div class="offcanvas-header">
    <a href="index.php" class="header-logo">
          <img src="../assets/images/logo/logo8.png" style = "align-items-start"   alt="Anon's logo" width="175" height="47">
        </a>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">



    <ol class="list-group ">
  <li class="list-group-item d-flex justify-content-between align-items-start">                                                                               

    <div style="w: 100vh; position: fixed;" class="ms-2 me-auto">
      <li  class="list-group-item fw-bold list-group  d-flex" >Home Decoration</li>
      <a href="search_results.php?search=Walldecor&search_data=null"><li class="list-group-item d-flex list-group-item-action">Wall decor</li></a>
      <a href="search_results.php?search=Clocks&search_data=null"><li class="list-group-item d-flex list-group-item-action">Clocks</li></a>
      <a href="search_results.php?search=Stickers&search_data=null"><li class="list-group-item d-flex list-group-item-action">Stickers</li></a>
      <a href="search_results.php?search=Mirrors&search_data=null"><li class="list-group-item d-flex list-group-item-action">Mirrors</li></a>
      <a href="search_results.php?search=WallDécor&search_data=null"><li class="list-group-item d-flex list-group-item-action">Wall Décor & Hanging</li></a>
      
      <li  class="list-group-item fw-bold list-group  d-flex" >Smart Gadgets</li>
      <a href="search_results.php?search=Kitchen&search_data=null"><li class="list-group-item d-flex list-group-item-action">Kitchen</li></a>
      <a href="search_results.php?search=Home&search_data=null"><li class="list-group-item d-flex list-group-item-action">Home</li></a>
      <a href="search_results.php?search=Garden&search_data=null"><li class="list-group-item d-flex list-group-item-action">Garden</li></a>
      <a href="search_results.php?search=SmartGadgets&search_data=null"><li class="list-group-item d-flex list-group-item-action">Smart</li></a>
      <a href="search_results.php?search=Gadgets&search_data=null"><li class="list-group-item d-flex list-group-item-action">Others</li></a>
      
      <li class="list-group-item fw-bold list-group  d-flex ">Tools</li>
      <a href="search_results.php?search=Hometools&search_data=null"><li class="list-group-item d-flex list-group-item-action">Home</li></a>
      <a href="search_results.php?search=Arttools&search_data=null"><li class="list-group-item d-flex list-group-item-action">Art</li></a>
      <a href="search_results.php?search=Kittools&search_data=null"><li class="list-group-item d-flex list-group-item-action">Craft Kit</li></a>
      <a href="search_results.php?search=Wrench&search_data=null"><li class="list-group-item d-flex list-group-item-action">Wrench</li></a>
      <a href="search_results.php?search=Walltools&search_data=null"><li class="list-group-item d-flex list-group-item-action">Wall</li></a>
      <a href="search_results.php?search=ToolBox&search_data=null"><li class="list-group-item d-flex list-group-item-action">Portable Tool Box</li></a>

      
      <li class="list-group-item fw-bold list-group  d-flex ">Others</li>
      <a href="index.php&search_data=null"><li class="list-group-item d-flex list-group-item-action">Others Items</li></a>
      
    </li>
    </div>

    </div>
    
    
    <!-- <span class="badge text-bg-primary rounded-pill">14</span> -->
  </li>

</ol>



  </div>

  
</div>

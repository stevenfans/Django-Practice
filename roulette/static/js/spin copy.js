//  script automatically requests and gets user's location
// then sends and posts results from yelp api with location 

var degrees = 1; // start off with 0 degrees
var map, infoWindow;

function initMap() {
  console.log("before geolocation");
  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      console.log("inside the navigator");

      $("#buttonStr").click(function(){
        var lat = pos.lat; 
        var lon = pos.lng; 

        console.log(lat); 
        console.log(lon);

        spin();

        $.ajax({
          type: "GET",
          url: 'process_loc', 
          data: {
            'lat': lat,
            'lon': lon,
          }, 
          datatype: "json",
          success:function(){
            console.log("ajax was a success")
          },
          error:function(xhr,errmsg,err){
            alert("Could not send URL to Django. Error: " + xhr.status + ": " + xhr.responseText);
          }
        })
      });
      
    });
} 
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
  infoWindow.open(map);
}

function spin(){
    var wheel = document.getElementById("wheel"); 
    console.log("inside funcn"); 
    function rotationAnimation(){
        wheel.style.transform = "rotate("+degrees+"deg)"; 
        wheel.style.webkitTransform = "rotate("+degrees+"deg)"; 
        wheel.style.msTransform = "rotate("+degrees+"deg)"; 
        
        setTimeout(rotationAnimation,0.25);

        degrees++; 
        if(degrees>359){
            degrees == 1; 
        }
    }
    console.log("outside function");
    rotationAnimation();
    setTimeout(alertDone, 4000);
};  

function alertDone(){
    //once done we need to get the next url
    //$(document).ready(function(){
        $.ajax({
            type: "GET", 
            url: "goToResults",
           success:function(){
            console.log("ajax was a success")
            window.location.href = "http://127.0.0.1:8000/results/"
          },
          error:function(xhr,errmsg,err){
            alert("Could not send URL to Django. Error: " + xhr.status + ": " + xhr.responseText);
          }
        })
}
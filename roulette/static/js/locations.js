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
      // console.log(pos.lat);
      // console.log(pos.lng);
      $("#buttonLoc").click(function(){
        var lat = pos.lat; 
        var lon = pos.lng; 
        //console.log("document is ready");
        console.log(lat); 
        console.log(lon);

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
console.log("hi"); 
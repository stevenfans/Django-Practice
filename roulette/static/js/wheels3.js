    // var loop; 
    var degrees = 1; // start off with 0 degrees
        // this script just spins the wheel on spin click
        //TODO: Uncaught RangeError: Maximum call stack size exceeded
        $("#buttonSub").click(function(){
            console.log("test");
                setTimeout(test(),1000);
            // var wheel = document.getElementById("wheel"); 
            // function rotationAnimation(){
            //     wheel.style.transform = "rotate("+degrees+"deg)"; 
            //     wheel.style.webkitTransform = "rotate("+degrees+"deg)"; 
            //     wheel.style.msTransform = "rotate("+degrees+"deg)"; 
                
            //     setTimeout(rotationAnimation,0.25);

            //     degrees++; 
            //     if(degrees>359){
            //         degrees == 1; 
            //     }
            // }
            // // console.log("outside function");
            // rotationAnimation();
            // setTimeout(alertDone, 4000);

            // TODO: NEED TO FIX FORM ANIMATION
    });  

function test(){
    alert("test");
}
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
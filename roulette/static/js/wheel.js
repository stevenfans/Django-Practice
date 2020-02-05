    // var loop; 
    var degrees = 1; // start off with 0 degrees

        // this script just spins the wheel on spin click
        //TODO: Uncaught RangeError: Maximum call stack size exceeded
        $("#buttonStr").click(function(){
            var wheel = document.getElementById("wheel"); 
            console.log("inside function"); 
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
            setTimeout(alert, 5000);
    });  
console.log("test that spinning is connected");

function alertDone(){
    alert("Done");
}
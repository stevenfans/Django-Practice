    var loop; 
    var degrees = 1; // start off with 0 degrees

    // $(document).ready(function(){
        // this script just spins the wheel on spin click
        //TODO: Uncaught RangeError: Maximum call stack size exceeded
        $("#buttonStr").click(function(){
            var wheel = document.getElementById("wheel"); 
            console.log("inside function"); 
            function rotationAnimation(){
                wheel.style.transform = "rotate("+degrees+"deg)"; 
                wheel.style.webkitTransform = "rotate("+degrees+"deg)"; 
                wheel.style.msTransform = "rotate("+degrees+"deg)"; 
                
                setTimeout(rotationAnimation,20);

                degrees++; 
                if(degrees>359){
                    degrees == 1; 
                }
            }
            console.log("outside function");
            rotationAnimation();
    });  
// })
console.log("test that spinning is connected");

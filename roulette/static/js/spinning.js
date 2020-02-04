    var loop; 
    var degrees = 1; // start off with 0 degrees

    $(document).ready(function(){
        // this script just spins the wheel on spin click
        var wheel = document.getElementById("wheel"); 
        //TODO: Uncaught RangeError: Maximum call stack size exceeded
        $("#buttonStr").click(function(){
            console.log("inside function"); 
            function rotationAnimation(){
                wheel.style.transform = "rotate("+degrees+"deg)"; 
                wheel.style.webkitTransform = "rotate("+degrees+"deg)"; 
                wheel.style.msTransform = "rotate("+degrees+"deg)"; 
                
                loop = setTimeout(rotationAnimation(),20);

                degrees++; 
                if(degrees>359){
                    degrees == 1; 
                }
            }
            console.log("outsied function");
            rotationAnimation();
    });  
})
console.log("test that spinning is connected");

// $(document).ready(function(){
//     $('#buttonStr').on('click',function(){
//         $('#wheel').animate({'-webkit-animation':'rotation 0.4s linear 3',
//                             'rotation': })
//         alert("FUCK ME");
//     });
// });
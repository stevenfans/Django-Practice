// this script just spins the wheel on spin click
var spin = document.getElementById("buttonStr")
var degrees = 20; // start off with 0 degrees
// $("button").click(function(){
//     alert("help i've fallen and i cant get up"); 
//   }); 

$("#buttonStr").click(function rotationAnimation(object, speed){
    var objectElement = document.getElementById(object); 
    objectElement.style.transform = "rotate("+degrees+"deg)"; 
    objectElement.style.webkitTransform = "rotate("+degrees+"deg)"; 
    objectElement.style.msTransform = "rotate("+degrees+"deg)";

    alert("test"); 
});  
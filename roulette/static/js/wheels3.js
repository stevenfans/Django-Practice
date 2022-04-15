    // test connection 
    var degrees = 1; // start off with 0 degrees
        // this script just spins the wheel on spin click
        //TODO: Uncaught RangeError: Maximum call stack size exceeded
        $("#button-test").click(function(){
            console.log("test");
                setTimeout(test(),1000);
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
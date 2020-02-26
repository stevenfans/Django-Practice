var spinButton = document.getElementById("buttonRel"); 
console.log("test"); 
spinButton.onclick = function(){
     alert("you clicked the button"); 

    $.ajax({
        type:"GET",
        // url:"reload",
        success:function(){
            console.log("test reload was a success");
            window.location.href="http://127.0.0.1:8000/results/";
        },
        // error:function(xhr,errmsg,err){
        //     console.log("test was a failure")
        //     alert("Could not send URL to Django. Error: " + xhr.status + ": " + xhr.responseText);
        // }
    })
};
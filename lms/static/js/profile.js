function change(){
    document.getElementById("t1").readOnly = false;
    document.getElementById("t2").readOnly = false;
    document.getElementById("t3").readOnly = false;
    document.getElementById("btnchoise").style.display = "block";
    
}

function unchange(){
    document.getElementById("t1").readOnly = true;
    document.getElementById("t2").readOnly = true;
    document.getElementById("t3").readOnly = true;
    document.getElementById("btnchoise").style.display = "none";
}
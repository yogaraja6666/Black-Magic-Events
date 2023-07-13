function page2(){
    window.open("Home Page/anirudhevent.html","_self")
}

function ch(){

    var checkbox = document.getElementById("show")
    var text = document.getElementById("check")
    if (checkbox.checked ==true){
        text.style.display = "block";
    } else{
        text.style.display = "none";
    }
}
/*function signup(){
    var signtext = document.getElementById("logintext")
    signtext.innerHTML = "Sign Up"
    var mailtext = document.getElementById("emailtext")
    mailtext.innerHTML = "Email"
    var crpassword = document.getElementById("createpassword")
    crpassword.innerHTML = "Create Password"
    var confpass = document.getElementById("conpass")
    confpass.style.display = "block"
    var forgpass = document.getElementById("forpass")
    forgpass.style.display = "none"
    var loginbtntext = document.getElementById("logbtntext")
    loginbtntext.innerHTML = "Sign Up"
    var alreadylogin = document.getElementById("already")
    alreadylogin.style.display ="block"
    var notmemtext = document.getElementById("notmemembertext")
    notmemtext.style.display = "none"
}
function loginlink(){
    var lgtext = document.getElementsByClassName("logintext")
    lgtext.innerHTML = "Login"
}*/

function join(){
    window.open("/sign up page/signup.html","_blank")
}
function conctact(){
    window.open("{% url 'contact' %}","_blank")
}
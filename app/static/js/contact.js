function sm(){
    let name1 = document.getElementById("name").value
    let email1 = document.getElementById("email").value
    let text1 = document.getElementById("msg").value
    var regEmail =  /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    var regName = /\d+$/g;
    var allInputs = document.querySelectorAll('input');

    if (name1 == "" || regName.test(name1)) {
        window.alert("Please enter your name.");
        name1.focus();
        return false;
    }
    if (email1 == "" || !regEmail.test(email1)) {
        window.alert("Please enter a valid e-mail address.");
        email1.focus();
        return false;
    }
    if (text1 =="")
    {
        alert("Enter Message")
        return false
    }
    
    else{
        alert("Message Sent Successfully")
        
    }
}


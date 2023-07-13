function submit(){
    let pass1 = document.getElementById("p1").value
    let pass2 = document.getElementById("p2").value
    let name1 = document.getElementById("name").value
    let email1 = document.getElementById("email").value
    var regEmail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    var regName = /\d+$/g;
    var checkbox = document.getElementById("check")

    if (name1 == "" || regName.test(name1)) {
        window.alert("Please enter your name.");
        return false;
    }
    if (email1 == "" || !regEmail.test(email1)) {
        window.alert("Please enter a valid e-mail address.");
        return false;
    }
    if (pass1 != pass2)
    {
        alert("Password mismatch")
        return false
    }
    if (checkbox.checked == true)
    {
        window.close()

    }
    else{
        alert("Agree to Terms and Conditions")

    }
}

function register() {
 
    var username = document.getElementById("username");
    var pass = document.getElementById("password");
    var email = document.getElementById("email");
    var first = document.getElementById("firstname");
    var last = document.getElementById("lastname");

    if (username.value == "") {
 
        alert("Please enter the username!");
 
    } else if (pass.value  == "") {
 
        alert("Please enter the password!");
 
    } else if (email.value  == "") {
 
        alert("Please enter the email!");

    } else if (first.value  == "") {
 
        alert("Please enter the firstname!");

    }  else if (last.value  == "") {
 
        alert("Please enter the lastname!");

    }else {

        alert("Successfully!");
 
        window.location.href="login"
 
    }
}
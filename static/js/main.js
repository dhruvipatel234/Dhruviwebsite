function login() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("repassword").value;
    if (email == ""|| password=="") {
        window.alert("Please enter email and password");
        return false;
    }
}
function userlogin() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("repassword").value;
  if (username == ""|| password=="") {
    window.alert("Please username and password");
      return false;
  }
}

function createuser() {
  var email = document.getElementById("email").value;
  var username = document.getElementById("username").value;
  var password = document.getElementById("repassword").value;
  if (email == "" || username == ""|| password=="") {
    window.alert("Please username , email and password");
    return false;
  }
}

function password() {
    var x = document.getElementById("repassword");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
}

function edituser() {  
  var email = document.getElementById("email").value;
  var username = document.getElementById("username").value;
  if (username == ""|| email=="") {
    window.alert("Please enter username  and email");
    return false;
     
  }
}
function resetpassword()
{
        window.alert("i send link in your mail");
        return false;
}
function setnewpassword()
{
  window.alert("your password is updated and we sned in your mail");
  return false;
}
$(document).ready(function () {
  $('#dtBasicExample').DataTable();
  $('.dataTables_length').addClass('bs-select');
});
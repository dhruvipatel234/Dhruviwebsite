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

function setnewpassword()
{
  window.alert("your password is updated and we sned in your mail");
  return false;
}
$(document).ready(function () {
  $('#dtBasicExample').DataTable();
  $('.dataTables_length').addClass('bs-select');
});

function onemail()
{
  var email = document.getElementById("email").value;
  
  var x = document.getElementById("submit");
  var filter =/^\w+.+@\w+([\.])+\w+/;

  if (filter.test(email)) {
    x.disabled=false;
    $('#repassword').show();
    $('#username').show();
    $('#onrepassword').show();

    document.getElementById("error").innerHTML =  "";
  }
  else {
    document.getElementById("error").innerHTML =  "Please enter a valid email and show next fields";
    x.disabled=true;
    $('#repassword').hide();
    $('#username').hide();
    $('#onrepassword').hide();
    
    return false;
  }
  
  

}

function onpassword()
{
  var email = document.getElementById("repassword").value;
  var x = document.getElementById("submit");
  var filter =/(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}/;

  if (filter.test(email)) {
    x.disabled=false;
   
    $('#username').show();
    $('#onrepassword').show();
    document.getElementById("password").innerHTML =  "";
  }
  else {
    document.getElementById("password").innerHTML =  "please enter upercase,lowecase,digit and special character how next fields";
    x.disabled=true;
    $('#username').hide();
    $('#onrepassword').hide();
  }
}
function onusername()
{
  var username = document.getElementById("username").value;
  var x = document.getElementById("submit");
  var filter =/[A-Za-z][A-Za-z0-9_]{7,29}$/;

  if (filter.test(username)) {
    x.disabled=false;
    $('#repassword').show();
    $('#onrepassword').show();
    document.getElementById("uname").innerHTML =  "";
  }
  else {
    document.getElementById("uname").innerHTML =  "Please enter a valid Username and how next fields";
    x.disabled=true;
    $('#repassword').hide();
    $('#onrepassword').hide();
  }
}
function onname()
{                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
  var name = document.getElementById("uname").value;
  var x = document.getElementById("submit");
  var filter =/[A-Z]+[A-za-z]+/;

  if (filter.test(name)) {
    
    x.disabled=false;
    document.getElementById("name").innerHTML =  "";
  }
  else {
    x.disabled=true;
    document.getElementById("name").innerHTML =  "Must be enter first letter capital";
    
  }
}
function onlastname()
{
  var name = document.getElementById("llname").value;
  var x = document.getElementById("submit");
  var filter =/[A-Z]+[A-za-z]+/;

  if (filter.test(name)) {
 
    x.disabled=false;
    document.getElementById("lastname").innerHTML =  "";
  }
  else {
    x.disabled=true;
    document.getElementById("lastname").innerHTML =  "Must be enter first letter capital";
    
  }
}

function oncity()
{
  var name = document.getElementById("city").value;
  var x = document.getElementById("submit");
  var filter =/[A-Z]+[A-za-z]+/;

  if (filter.test(name)) {
 
    x.disabled=false;
    document.getElementById("oncity").innerHTML =  "";
  }
  else {
    document.getElementById("oncity").innerHTML =  "Must be enter first letter capital";
    x.disabled=true;
    
  }
}
function onmoblienumber()
{
  var name = document.getElementById("mno").value;
  var x = document.getElementById("submit");
  var filter =/[789][0-9]{9}/;

  if (filter.test(name)) {
 
    x.disabled=false;
    document.getElementById("mnum").innerHTML =  "";
  }
  else {
    document.getElementById("mnum").innerHTML =  "Must be enter 10 digit and start with 7,8,9";
    x.disabled=true;
  }
}
function onzipcode()
{
  var name = document.getElementById("zip").value;
  var x = document.getElementById("submit");
  var filter =/[0-9]{5}/;

  if (filter.test(name)) {
 
    x.disabled=false;
    document.getElementById("zipcode").innerHTML =  "";
  }
  else {
    document.getElementById("zipcode").innerHTML =  "Must be enter 06 digit";
    x.disabled=true;
  }
}
function onaddress()
{
  var name = document.getElementById("address").value;
  var x = document.getElementById("submit");
  var filter =/[A-Za-z0-9'\.\-\s\,]+/;

  if (filter.test(name)) {
 
    x.disabled=false;
    document.getElementById("add").innerHTML =  "";
  }
  else {
    document.getElementById("add").innerHTML =  "Must be enter valid address";
    x.disabled=true;
  }
}

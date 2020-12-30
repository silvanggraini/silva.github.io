var apalah  = document.querySelector(".masuk")
var username = document.querySelector('#username');
username.addEventListener('keyup',function(){
    var userKosong = document.getElementById('userKosong');
    if (username.value.length == 0 || username.value.length < 6) {
        username.style.border = "1px solid red";
        userKosong.style.display = "block";
        apalah.setAttribute('href','#');
        return false;
    }
    else{
        username.style.border = "1px solid #40a8c4";
        userKosong.style.display = "none";
        apalah.setAttribute('href','home.html')
    }
})

var apalah  = document.querySelector(".masuk")
var password = document.querySelector('#password');
password.addEventListener('keyup',function(){
    var passKosong = document.getElementById('passKosong');
    if (password.value.length == 0 || password.value.length < 8) {
        password.style.border = "1px solid red";
        passKosong.style.display = "block";
        apalah.setAttribute('href','#');
        return false;
    }
    else{
        password.style.border = "1px solid #40a8c4";
        passKosong.style.display = "none";
        apalah.setAttribute('href','home.html')
    }
})

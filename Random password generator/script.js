const passwordBox = document.getElementById("password")
const length = 12

const uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
const lowercase = "abcdefghijklmnopqrstuvwxyz"
const number = "1234567890"
const symbols = "!@#$%^&*()<>?{}|><-+"

const alchars = uppercase+lowercase+number+symbols

function createpassword(){
    let password = ""
    password += uppercase[Math.floor(Math.random()*uppercase.length)]
    password += lowercase[Math.floor(Math.random()*lowercase.length)]
    password += number[Math.floor(Math.random() *number.length)]
    password += symbols[Math.floor(Math.random()*symbols.length)]

    while(length>password.length){
        password += alchars[Math.floor(Math.random()*alchars.length)]
    }
    passwordBox.value = password
}

function copypassword(){
    passwordBox.select()
    document.execCommand("copy")
}
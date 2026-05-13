<<<<<<< HEAD
// ATM state
    let enteredValue = "";
    let balance = 0;
    const correctPin = "1234"; // default PIN
    let authenticated = false;

    const display = document.getElementById("display");
    const buttons = document.querySelectorAll(".keypad button");

    // Handle keypad clicks
    buttons.forEach(btn => {
        btn.addEventListener("click", () => {
            const value = btn.textContent;

            if(value === "Clear"){
                enteredValue = "";
                display.textContent = "Cleared. Enter PIN or amount";
            } else if(value === "Enter"){
                if(!authenticated){
                    // PIN check
                    if(enteredValue === correctPin){
                        authenticated = true;
                        display.textContent = "PIN accepted. Choose action.";
                    } else {
                        display.textContent = "Incorrect PIN!";
                    }
                } else {
                    // Amount entry mode
                    display.textContent = `Amount entered: ${enteredValue}`;
                }
                enteredValue = "";
            } else {
                // Append number
                enteredValue += value;
                display.textContent = enteredValue;
            }
        });
    });

    // Action buttons
    document.getElementById("deposit").addEventListener("click", () => {
        if(!authenticated){
            display.textContent = "Enter PIN first!";
            return;
        }
        let amount = parseInt(enteredValue);
        if(amount > 0){
            balance += amount;
            display.textContent = `Deposited: ${amount}, Balance: ${balance}`;
        } else {
            display.textContent = "Invalid deposit amount";
        }
        enteredValue = "";
    });

    document.getElementById("withdraw").addEventListener("click", () => {
        if(!authenticated){
            display.textContent = "Enter PIN first!";
            return;
        }
        let amount = parseInt(enteredValue);
        if(amount > 0 && amount <= balance){
            balance -= amount;
            display.textContent = `Withdrawn: ${amount}, Balance: ${balance}`;
        } else if(amount > balance){
            display.textContent = "Insufficient balance!";
        } else {
            display.textContent = "Invalid withdrawal amount";
        }
        enteredValue = "";
    });

    document.getElementById("balance").addEventListener("click", () => {
        if(!authenticated){
            display.textContent = "Enter PIN first!";
            return;
        }
        display.textContent = `Your balance: ${balance}`;
    });
=======
const inputBox = document.getElementById("input-box");
const listcontainer = document.getElementById("list-container")

function addTask(){
    if(inputBox.value===''){
        alert("you must write something")
    }else{
        let li = document.createElement("li")
        li.innerHTML = inputBox.value
        listcontainer.appendChild(li)
        let span = document.createElement("span")
        span.innerHTML= "\u00d7"
        li.appendChild(span)
    }
    inputBox.value=""
}
listcontainer.addEventListener("click",function(e){
    if(e.target.tagName === "LI"){
        e.target.classList.toggle("checked")
        saveData()
    }
    else if(e.target.tagName === "SPAN"){
        e.target.parentElement.remove()
        saveData()
    }
},false)

function saveData(){
    localStorage.setItem("data", listcontainer.innerHTML)

}
function showTask(){
    listcontainer.innerHTML=localStorage.getItem("data")
}
showTask()
>>>>>>> 21c8c9cfb0f52551aad39ef4efedcc1ae0d50e37

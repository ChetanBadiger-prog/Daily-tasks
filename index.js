const hourE1 = document.querySelector(".hour");
const minuteE1 = document.querySelector(".minute");
const secondsE1 = document.querySelector(".seconds");

function updateclock() {
    const currentDate = new Date();

    const hour = currentDate.getHours();
    const minute = currentDate.getMinutes();
    const second = currentDate.getSeconds();

    const hourDeg = (hour % 12) / 12 * 360 + (minute / 60) * 30;
    const minuteDeg = (minute / 60) * 360;
    const secondDeg = (second / 60) * 360;

    hourE1.style.transform = `rotate(${hourDeg}deg)`;
    minuteE1.style.transform = `rotate(${minuteDeg}deg)`;
    secondsE1.style.transform = `rotate(${secondDeg}deg)`;
}

// run immediately
updateclock();

// update every second
setInterval(updateclock, 1000);

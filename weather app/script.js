const apikey = "340677cb6d7066e64bdaa44b46a6f727";

const apiUrl =
  "https://api.openweathermap.org/data/2.5/weather?units=metric&q=";

const searchBox = document.querySelector(".search input");

const searchBtn = document.querySelector(".search button");

const weatherIcon = document.querySelector(".weather-icon");


async function checkweather(city) {

    try {
        const response = await fetch(apiUrl + city + `&appid=${apikey}`);
        if(response.status == 404){
            alert("City not found");
            return;
        }

        var data = await response.json();
        console.log(data);
        document.querySelector(".city").innerHTML = data.name;
        document.querySelector(".temp").innerHTML =
            Math.round(data.main.temp) + "°c";
        document.querySelector(".humidity").innerHTML =
            data.main.humidity + "%";
        document.querySelector(".wind").innerHTML =
            data.wind.speed + " km/h";
        if(data.weather[0].main == "Clouds"){
            weatherIcon.src = "./images/clouds.png";
        }
        else if(data.weather[0].main == "Clear"){
            weatherIcon.src = "./images/clear.png";
        }
        else if(data.weather[0].main == "Rain"){
            weatherIcon.src = "./images/rain.png";
        }
        else if(data.weather[0].main == "Drizzle"){
            weatherIcon.src = "./images/drizzle.png";
        }
        else if(data.weather[0].main == "Mist"){
            weatherIcon.src = "./images/mist.png";
        }
    }
    catch(error){
        console.log(error);
    }
}
searchBtn.addEventListener("click", () => {
    checkweather(searchBox.value);
});
searchBox.addEventListener("keypress", (e) => {
    if(e.key === "Enter"){
        checkweather(searchBox.value);
    }

});
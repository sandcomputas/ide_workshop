
document.addEventListener("DOMContentLoaded", function () {
    const dataList = document.getElementById("nasa-response");
    const apiUrl = "/asteroids";

    // Fetch data from the API
    fetch(apiUrl)
        .then((response) => response.json())
        .then((data) => {
            // Loop through the JSON data and create list items
            data.forEach((item) => {
                const listItem = document.createElement("li");
                listItem.textContent = "id: " + item.id + " | Name: " + item.name + " | is_potentially_hazardous_asteroid:" + item.is_potentially_hazardous_asteroid + " | miss_distance: " + item.miss_distance_km;
                dataList.appendChild(listItem);
            });
        })
        .catch((error) => {
            console.error("Error fetching data:", error);
        });
});




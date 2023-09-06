

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("myForm");
    const parameter1 = document.getElementById("parameter1");
    const parameter2 = document.getElementById("parameter2");

    document.getElementById("submitButton").addEventListener("click", function () {
        const p1 = parameter1.value;
        const p2 = parameter2.value;

        if (p1 && p2) {
            const jsonData = {
                parameter1: p1,
                parameter2: p2,
                operation: "Addition"
            };
            sendPostRequest(jsonData);
        } else {
            alert("Please fill in all fields");
        }
    });

    function sendPostRequest(data) {
        console.log(data)
        console.log(JSON.stringify(data))
        fetch("calculation", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        }).then(function(response) {
            return response.json()
        }).then(function(data) {
            console.log(data)
            //document.getElementById("").innerHTML = JSON.parse(data)
        }).catch(function(err) {
            console.log("Fetch error:", err)
        })
    }


    function sendPostRequest2(data) {
        const xhr = new XMLHttpRequest();
        const url = "/calculation"; // Replace with your API endpoint URL

        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    alert("POST request successful!");
                } else {
                    alert("POST request failed. Status: " + xhr.status);
                }
            }
        };

        xhr.send(JSON.stringify(data));
    }
});






document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("add");
    const parameter1 = document.getElementById("parameter1_add");
    const parameter2 = document.getElementById("parameter2_add");

    document.getElementById("submitButton_add").addEventListener("click", function () {
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

});




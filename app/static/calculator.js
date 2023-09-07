// OBS! This is very ugly frontend code! Not really part of workshop, only meant to display some data in a very simple way.

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
        document.getElementById("result").innerHTML = data.answer
    }).catch(function(err) {
        console.log("Fetch error:", err)
    })
}

function doMathAdd(event) {
    const form = document.getElementById("add");
    const parameter1 = document.getElementById("parameter1_add");
    const parameter2 = document.getElementById("parameter2_add");

    document.getElementById("submitButton_add").addEventListener("click", function (event) {
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
    })
}
function doMathSub(event) {
    const form = document.getElementById("sub");
    const parameter1 = document.getElementById("parameter1_sub");
    const parameter2 = document.getElementById("parameter2_sub");

    document.getElementById("submitButton_sub").addEventListener("click", function (event) {
        console.log(event.currentTarget.id);
        const p1 = parameter1.value;
        const p2 = parameter2.value;

        if (p1 && p2) {
            const jsonData = {
                parameter1: p1,
                parameter2: p2,
                operation: "Subtract"
            };
            sendPostRequest(jsonData);
        } else {
            alert("Please fill in all fields");
        }
    })
}
function doMathMult(event) {
    const form = document.getElementById("mult");
    const parameter1 = document.getElementById("parameter1_mult");
    const parameter2 = document.getElementById("parameter2_mult");

    document.getElementById("submitButton_mult").addEventListener("click", function (event) {
        console.log(event.currentTarget.id);
        const p1 = parameter1.value;
        const p2 = parameter2.value;

        if (p1 && p2) {
            const jsonData = {
                parameter1: p1,
                parameter2: p2,
                operation: "Multiply"
            };
            sendPostRequest(jsonData);
        } else {
            alert("Please fill in all fields");
        }
    })
}
function doMathDiv(event) {
    const form = document.getElementById("div");
    const parameter1 = document.getElementById("parameter1_div");
    const parameter2 = document.getElementById("parameter2_div");

    document.getElementById("submitButton_div").addEventListener("click", function (event) {
        console.log(event.currentTarget.id);
        const p1 = parameter1.value;
        const p2 = parameter2.value;

        if (p1 && p2) {
            const jsonData = {
                parameter1: p1,
                parameter2: p2,
                operation: "Divide"
            };
            sendPostRequest(jsonData);
        } else {
            alert("Please fill in all fields");
        }
    })
}

document.addEventListener("DOMContentLoaded", doMathAdd);
document.addEventListener("DOMContentLoaded", doMathSub);
document.addEventListener("DOMContentLoaded", doMathMult);
document.addEventListener("DOMContentLoaded", doMathDiv);






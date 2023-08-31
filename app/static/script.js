

fetch("/health").then(function(response) {
    return response.json();
}).then(function(data) {
    console.log("lastet");
    document.getElementById("mytext").innerHTML = JSON.parse(data);
}).catch(function(err) {
    console.log('Fetch Error :-S', err);
});

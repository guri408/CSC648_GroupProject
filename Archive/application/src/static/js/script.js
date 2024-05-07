// script.js

// Define a function to be called when a button is clicked
function greet() {
    // Retrieve the input value from the textbox with id "name"
    var name = document.getElementById("name").value;
    
    // Construct a greeting message
    var message = "Hello, " + name + "! Welcome to our website!";
    
    // Display the greeting message in an alert box
    alert(message);
}

This tasks is all about JQuery.
How to Listen/Bind to User Events
Listening or binding to user events involves setting up event handlers that respond to various actions performed by the user, such as clicks, key presses, mouse movements, and more. Here are some common ways to bind event listeners in JavaScript and jQuery:

JavaScript
Using addEventListener:

Click Event:

javascript
Copy code
var button = document.getElementById('buttonId');
button.addEventListener('click', function() {
    alert('Button clicked!');
});
Mouseover Event:

javascript
Copy code
var element = document.getElementById('elementId');
element.addEventListener('mouseover', function() {
    console.log('Mouse is over the element');
});
Keydown Event:

javascript
Copy code
document.addEventListener('keydown', function(event) {
    console.log('Key pressed:', event.key);
});
Form Submit Event:

javascript
Copy code
var form = document.getElementById('formId');
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    console.log('Form submitted');
});
Using onclick, onmouseover, etc.:

javascript
Copy code
var button = document.getElementById('buttonId');
button.onclick = function() {
    alert('Button clicked!');
};
jQuery
Using .on():

Click Event:

javascript
Copy code
$('#buttonId').on('click', function() {
    alert('Button clicked!');
});
Mouseover Event:

javascript
Copy code
$('#elementId').on('mouseover', function() {
    console.log('Mouse is over the element');
});
Keydown Event:

javascript
Copy code
$(document).on('keydown', function(event) {
    console.log('Key pressed:', event.key);
});
Form Submit Event:

javascript
Copy code
$('#formId').on('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    console.log('Form submitted');
});
Using shorthand methods:

Click Event:

javascript
Copy code
$('#buttonId').click(function() {
    alert('Button clicked!');
});
Mouseover Event:

javascript
Copy code
$('#elementId').mouseover(function() {
    console.log('Mouse is over the element');
});
Keydown Event:

javascript
Copy code
$(document).keydown(function(event) {
    console.log('Key pressed:', event.key);
});
Form Submit Event:

javascript
Copy code
$('#formId').submit(function(event) {
    event.preventDefault(); // Prevent form submission
    console.log('Form submitted');
});

// Write a JavaScript script that fetches the character name from this
// URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

let sw_url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(sw_url, function(data, status) {
  $('DIV#character').text(data.name);
});

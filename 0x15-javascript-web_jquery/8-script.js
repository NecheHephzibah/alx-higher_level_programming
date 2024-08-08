// Write a JavaScript script that fetches and lists the title for all movies
// by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

let sw_url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(sw_url, function(data) {
  let movies = data.results;
  for (let m of movies) {
    $('UL#list_movies').append(`<li>${m.title}</>`)
  }
});

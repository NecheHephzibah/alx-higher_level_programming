// Write a JavaScript script that fetches from
// https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of
// hello from that fetch in the HTML tag DIV#hello.

let sw_url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(sw_url, function(data) {
  $('DIV#hello').text(data.name);
})

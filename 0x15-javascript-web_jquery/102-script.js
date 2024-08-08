// Write a JavaScript script that fetches and prints how to say
// “Hello” depending on the language using this API service
// https://www.fourtonfish.com/hellosalut/hello/

$(document).ready(function() {
  $('INPUT#btn_translate').click(function() {
    const langCode = $('INPUT#language_code').val();

    const url = 'https://www.fourtonfish.com/hellosalut/hello/';

    $.get(url, function(data) {
      $('DIV#hello').text(data.hello);
    });
  });
});

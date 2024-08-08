// Write a JavaScript script that fetches and prints how to say
// “Hello” depending on the language using this API service
// https://www.fourtonfish.com/hellosalut/hello/
// The translation must be fetched when the user clicks on INPUT#btn_translate
// OR presses ENTER when the focus is on INPUT#language_code

$(document).ready(function() {
  function getTranslation() {
    const langCode = $('INPUT#language_code').val();

    const url = 'https://www.fourtonfish.com/hellosalut/hello/';

    $.get(url, function(data) {
      $('DIV#hello').text(data.hello);
    });
  }

  $('INPUT#btn_translate').click(getTranslation);

  $('INPUT#language_code')keypress(function(event) {
    if (event.which === 13) {
	  getTranslation();
    }
  });
});

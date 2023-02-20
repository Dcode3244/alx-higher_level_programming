// $('document').ready(function () {
//   $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
//     $('DIV#hello').text(data.hello);
//   });
// });
$.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", function (data) {
  $("DIV#hello").html(data.hello)
});
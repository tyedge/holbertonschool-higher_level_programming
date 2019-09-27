const l = navigator.language;
const u = 'https://fourtonfish.com/hellosalut/?lang=' + l;
$.get(u, function (data) {
  $('DIV#hello').text(data.hello);
});

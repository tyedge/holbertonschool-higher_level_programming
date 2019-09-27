$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  const nm = data.name;
  $('DIV#character').text(nm);
});

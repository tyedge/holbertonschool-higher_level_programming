$.get('https://swapi.co/api/films/?format=json', function (data) {
  const res = data.results;
  for (const x of res) {
    const title = $('<li></li>').text(x.title);
    $('UL#list_movies').append(title);
  }
});

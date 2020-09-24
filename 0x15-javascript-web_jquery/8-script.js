$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  const results = data.results;
  const flist = $('UL#list_movies');
  for (let i = 0; i < results.length; i++) {
    flist.append(`<li>${results[i].title}</li>`);
  }
});

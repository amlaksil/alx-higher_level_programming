$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data) {
    $.each(data.results, function (index, movie) { // Loop through all movie title
      const li = $('<li>'); // Create a new li element
      li.text(movie.title); // Set the text of the li element to the movie title
      $('UL#list_movies').append(li);
    });
  });

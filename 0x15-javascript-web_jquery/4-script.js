$('DIV#toggle_header').on('click', function () {
  // Get the current class of the `header` element
  const currentClass = $('header').attr('class');
  // If the current class is "red", set the class to "green"
  if (currentClass === 'red') {
    $('header').attr('class', 'green');
  } else {
    // If the current class is "green", set the class to "red"
    $('header').attr('class', 'red');
  }
});

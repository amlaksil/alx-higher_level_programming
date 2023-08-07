$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    const langCode = $('#language_code').val();
    $.getJSON(`https://www.fourtonfish.com/hellosalut/?lang=${langCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  });
});

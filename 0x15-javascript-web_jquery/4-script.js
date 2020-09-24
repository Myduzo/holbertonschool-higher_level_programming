$('DIV#toggle_header').click(function () {
  if ($('HEADER').hasClass('green')) {
    $('HEADER').removeClass('green').addClass('red');
  } else {
    $('HEADER').removeClass('red').addClass('green')
  }
});

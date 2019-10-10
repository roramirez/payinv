// Here a custom Javascript code for all project

$(document).ready(function() {
  $('.datepicker').datepicker({
      format: 'yyyy-mm-dd',
  });

  $('#language').change(function() {
    $('#change-language').submit();
  });
});

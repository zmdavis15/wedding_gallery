$(document).ready(function() {

  $('#upload_img_form').submit(function(e) {
    e.preventDefault();
    // show uploading status
    $('#status').show();
    // disable submit button on press
    $('#submit_button').attr("disabled", true);
    $(this).closest("form")[0].submit();

 });

});

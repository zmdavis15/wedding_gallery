$(document).ready(function() {

  $('#upload_img_form').submit(function(e) {
    e.preventDefault();
    // show uploading status
    $('#status').show();
    $(this).closest("form")[0].submit();
    // disable submit button on press
    $('#submit_button').attr("disabled", true);
 });

});

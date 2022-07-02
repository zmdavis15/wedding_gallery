$(document).ready(function() {
  // hide success message
  setTimeout(function(){
    $('.alert').hide();
  }, 2000);

  // photo create modal
  var url = $('#main_content').attr('data-form-url');
  $("#upload_photo_btn").modalForm({
    formURL: url
  });
});

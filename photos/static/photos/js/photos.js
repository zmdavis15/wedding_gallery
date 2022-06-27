
// var img_upload = $('#id_img');
//
//
// $("#upload_img_form").submit(function(e){
//   console.log('form not submitted!')
//     return false;
//
// });
//
//
//

$(document).ready(function() {

  $("#id_img").on('change',function() {
    console.log('img upload button clicked');
    if ($('#id_img').get(0).files.length === 0) {
      console.log('no files uploaded');
    } else {
      console.log('files uploaded');
    }
  });

    var bar = $('.bar');
    var percent = $('.percent');
    var status = $('#status');

    $('form').ajaxForm({
        beforeSend: function() {
            status.empty();
            var percentVal = '0%';
            bar.width(percentVal);
            percent.html(percentVal);
        },
        uploadProgress: function(event, position, total, percentComplete) {
            var percentVal = percentComplete + '%';
            bar.width(percentVal);
            percent.html(percentVal);
        },
        complete: function(xhr) {
            status.html(xhr.responseText);
        }
    });







      //
      // $('#upload_img_form').submit(function() {
      //
      //     return true;
      // });
      //



});




// const uploadForm = document.getElementById('upload_img_form')
// const input = document.getElementById('id_img')
// console.log(input)
//
// const alertBox = document.getElementById('alert-box')
// const imageBox = document.getElementById('image-box')
// const progressBox = document.getElementById('progress-box')
// const cancelBox = document.getElementById('cancel-box')
// const cancelBtn = document.getElementById('cancel-btn')
//
// const csrf = document.getElementsByName('csrfmiddlewaretoken')
//
// input.addEventListener('change', ()=>{
//     progressBox.classList.remove('not-visible')
//     cancelBox.classList.remove('not-visible')
//
//     const img_data = input.files[0]
//     const url = URL.createObjectURL(img_data)
//     console.log(img_data)
//
//     const fd = new FormData()
//     fd.append('csrfmiddlewaretoken', csrf[0].value)
//     fd.append('image', img_data)
//
//     $.ajax({
//         type:'POST',
//         url: uploadForm.action,
//         enctype: 'multipart/form-data',
//         data: fd,
//         beforeSend: function(){
//             console.log('before')
//             alertBox.innerHTML= ""
//             imageBox.innerHTML = ""
//         },
//         xhr: function(){
//             const xhr = new window.XMLHttpRequest();
//             xhr.upload.addEventListener('progress', e=>{
//                 // console.log(e)
//                 if (e.lengthComputable) {
//                     const percent = e.loaded / e.total * 100
//                     console.log(percent)
//                     progressBox.innerHTML = `<div class="progress">
//                                                 <div class="progress-bar" role="progressbar" style="width: ${percent}%" aria-valuenow="${percent}" aria-valuemin="0" aria-valuemax="100"></div>
//                                             </div>
//                                             <p>${percent.toFixed(1)}%</p>`
//                 }
//
//             })
//             cancelBtn.addEventListener('click', ()=>{
//                 xhr.abort()
//                 setTimeout(()=>{
//                     uploadForm.reset()
//                     progressBox.innerHTML=""
//                     alertBox.innerHTML = ""
//                     cancelBox.classList.add('not-visible')
//                 }, 2000)
//             })
//             return xhr
//         },
//         success: function(response){
//             console.log(response)
//             imageBox.innerHTML = `<img src="${url}" width="300px">`
//             alertBox.innerHTML = `<div class="alert alert-success" role="alert">
//                                     Successfully uploaded the image below
//                                 </div>`
//             cancelBox.classList.add('not-visible')
//         },
//         error: function(error){
//             console.log(error)
//             alertBox.innerHTML = `<div class="alert alert-danger" role="alert">
//                                     Ups... something went wrong
//                                 </div>`
//         },
//         cache: false,
//         contentType: false,
//         processData: false,
//     })
// })

let close_button=document.querySelector('.add-wrapper .fa-times');
let modal=document.querySelector('.modal');
let edit=document.querySelector('.aside .section h1 .far');

edit.addEventListener('click',function(){
	modal.style.display="block";
})

close_button.addEventListener('click', function(){
	modal.style.display="none";
})

// window.addEventListener('click', function(){
// 	modal.style.display="none";
// });

window.addEventListener('load', function() {
  document.querySelector('input[type="file"]').addEventListener('change', function() {
      if (this.files && this.files[0]) {
          var img = document.querySelector('#p-image');
          var lbl = document.querySelector('#p-name');  // $('img')[0]
          img.src = URL.createObjectURL(this.files[0]);
          lbl.innerHTML=this.files[0].name; // set src to blob url
          img.onload = imageIsLoaded;
      }
  });
});


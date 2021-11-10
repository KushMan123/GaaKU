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

function imageIsLoaded() { 
  // alert(this.src);  // blob url
  // // update width and height ...
}
const category = document.querySelector("#id_category");
const sub1 = document.querySelector("#id_sub_category1");
const sub2 = document.querySelector("#id_sub_category2");

window.addEventListener("load", function () {
  document
    .querySelector('input[type="file"]')
    .addEventListener("change", function () {
      if (this.files && this.files[0]) {
        var img = document.querySelector("#p-image");
        // var lbl = document.querySelector("#p-name"); // $('img')[0]
        img.src = URL.createObjectURL(this.files[0]);
        // lbl.innerHTML = this.files[0].name; // set src to blob url
        img.onload = imageIsLoaded;
      }
    });
});

category.addEventListener("change", function () {
  if (category.value == "Education Materials") {
    sub1.style.display = "block";
    sub2.style.display = "block";
  } else {
    sub1.style.display = "none";
    sub2.style.display = "none";
  }
});

sub1.addEventListener("change", function () {
  if (sub1.value == "Labcoats" || sub1.value == "Drafters") {
    sub2.style.display = "none";
  } else {
    sub2.style.display = "block";
  }
});

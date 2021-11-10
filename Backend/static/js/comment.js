const like = document.querySelectorAll('.like-button');

like.addEventListener('click', function(event){
    event.target.innerHTML = 'Dislike';
});
// function getEventTarget(e){
// 	e=e||window.event;
// 	return e.target || e.srcElement;
// }

function changeinnerhtml(event){
	event.target.innerHTML = 'Dislike';
}



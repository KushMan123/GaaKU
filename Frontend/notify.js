const notify_btn=document.querySelector('.notification-btn');
const update_btn=document.querySelector('.update-btn');
const notification=document.querySelector('#notification');
const update=document.querySelector('#updates');
const btn=document.querySelector('#change-btn');
const bar=document.querySelector('.menu-icons');
const change_bar=document.querySelector('.menu-icons i');
const notification_container=document.querySelector('.notification-container')
let visible=false;

notify_btn.addEventListener('click',function(){
	notification.style.left="32px";
	update.style.left="432px";
	btn.style.left="0px";
	update_btn.style.color="black";
	notify_btn.style.color="white";

});

update_btn.addEventListener('click',function(){
	notification.style.left="-432px";
	update.style.left="32px";
	btn.style.left="135px";
	update_btn.style.color="white";
	notify_btn.style.color="black";
});

bar.addEventListener('click',function(){
	if(!visible){
		notification_container.style.display="block";
		change_bar.classList.remove('fa-bars');
		change_bar.classList.add('fa-times');
		visible=true;
	}
	else{
		notification_container.style.display="none";
		change_bar.classList.remove('fa-times');
		change_bar.classList.add('fa-bars');
		visible=false;
	}
})

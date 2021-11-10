const comment_box=document.querySelector('.commnet-input');
const comment_btn=document.querySelector('.comment-submit');
const comment_section=document.querySelector('.comment-section');
const reply_box=document.querySelector('.reply');

function reply(){
	reply_box.style.display="block";
}

function addReplyButton(){
	let btn=document.createElement('button');
	btn.appendChild(document.createTextNode('Reply'));
	btn.onclick=reply;
	return btn;
}

function addCommentItems(){
	let ul=document.createElement('ul');
	let li=document.createElement('li');
	li.appendChild(document.createTextNode(comment_box.value));
	li.appendChild(addReplyButton());
	ul.appendChild(li);
	ul.classList.add('comment');
	comment_section.appendChild(ul);
	comment_box.value="";
}

comment_btn.addEventListener('click',()=>{
	if(comment_box.value.length>0){
		addCommentItems();
	}
})

comment_box.addEventListener('keypress',(event)=>{
	if(comment_box.value.length>0 && event.keyCode===13){
		addCommentItems();
	}
})
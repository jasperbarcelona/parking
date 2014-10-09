$(document).ready(function(){

$('#intro').delay(4000).fadeOut(1500);

$(".buttons").click(function(){
	$(this).flip({direction:'lr',content:'Loading...',color:'#FFD700'})
});
});
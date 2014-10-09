$(document).ready(function(){

$('#intro').delay(4000).fadeOut(1500);
$('#content').delay(6000).fadeIn();

$(".buttons").click(function(){
	$(this).flip({direction:'lr',content:'Loading...',color:'#FFD700'})
});
});
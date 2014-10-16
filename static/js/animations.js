$(document).ready(function(){

$('#intro').delay(4000).fadeOut(1500);
$('#content').delay(6000).fadeIn();

$(".outerLayer").click(function(){
	$(this).flip({direction:'lr',color:'#FFD700'})
});
});
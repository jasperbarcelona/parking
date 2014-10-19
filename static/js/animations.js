$(document).ready(function(){

$('#intro').delay(4000).fadeOut(1500);
$('#content').delay(6000).fadeIn();

$(".glyphicon-align-justify").click(function(){
	$("#navigation").toggle({ origin: ["top", "right"] });
});
});
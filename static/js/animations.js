$(document).ready(function(){

$('#intro').delay(4000).fadeOut(1500);
$('#content').delay(6000).fadeIn();

var height = $(window).height()-80;
$("#container").css("height",height);


$(window).resize(function(){
	var height = $(window).height()-80;
	$("#container").css("height",height);
});


$(".glyphicon-align-justify").click(function(){
	$("#navigation").toggle();
	$(this).toggleClass("clicked unclicked");
	$("#container").toggleClass("containerClicked containerUnclicked");
});


});
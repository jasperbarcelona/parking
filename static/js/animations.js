$(document).ready(function(){

$(window).load(function() {
    $('#intro').hide();
  });


var height = $(window).height()-80;
$("#container").css("height",height);



$(window).resize(function(){
	var height = $(window).height()-80;
	$("#container").css("height",height);
});


$(".glyphicon-align-justify").click(function(){
	$("#navigation").slideToggle();
	$(this).toggleClass("clicked unclicked");
	$("#container").toggleClass("containerClicked containerUnclicked");
});


});
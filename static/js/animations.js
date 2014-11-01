$(document).ready(function(){

$(window).load(function() {
    $('#intro').delay(5000).fadeOut();
  });


var height = $(window).height()-60;
$("#container").css("height",height);



$(window).resize(function(){
	var height = $(window).height()-60;
	$("#container").css("height",height);
});


$("#parking").on('click', function() {
	$("#navigation").stop().slideToggle();
	$(".toggleUnclicked").switchClass( "toggleUnclicked", "toggleClicked" );
	$(".toggleClicked").switchClass( "toggleClicked", "toggleUnclicked" );
	$("#container").toggleClass("containerClicked containerUnclicked");
});


});

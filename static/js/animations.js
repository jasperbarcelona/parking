$(document).ready(function(){

$(window).load(function() {
    $('#intro').delay(5000).fadeOut();
  });


var height = $(window).height()-80;
$("#container").css("height",height);


$("#container").scroll(function(){
	$("#head").slideUp(1000);
	$("#container").animate({top:"0"});
	$("#container").css("height","100%");
	
	$("#search").css("position", "fixed");
	$("#search").animate({top: "0"});
	$("#search").animate({width: "95%"},1000);
	$("#search").css("left", "0");
	$("#search").css("right", "0");
	$("#search").css("margin-right", "auto");
	$("#search").css("margin-left", "auto");
	$(".places").css("margin-top", "80");
	$(".destinations").css("margin-top", "-22");
});


$(window).resize(function(){
	var height = $(window).height()-80;
	$("#container").css("height",height);
});


$("#toggleDown").click(function(){
	$("#navigation").slideDown(1500);
	$(this).css("display","none");
	$("#toggleUp").show();
	$("#container").toggleClass("containerClicked containerUnclicked");
});


});
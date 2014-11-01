$(document).ready(function(){

$(window).load(function() {
    $('#intro').delay(5000).fadeOut();
  });


/*var height = $(window).height()-80;
$("#container").css("height",height);*/


$(window).scroll(function(){
	$("#head").slideUp();
	$("#head").css("display","none");
	$("#search").css("position","fixed");
	$("#search").css("left","0");
	$("#search").css("right","0");
	$("#search").css("margin-left","auto");
	$("#search").css("margin-right","auto");
	$("#search").animate({width:"95%",top:"0"},500);


});


/*$(window).resize(function(){
	var height = $(window).height()-80;
	$("#container").css("height",height);
});*/


$("#toggleDown").click(function(){
	$("#navigation").slideDown(1500);
	$(this).css("display","none");
	$("#toggleUp").show();
	$("#container").toggleClass("containerClicked containerUnclicked");
});


});
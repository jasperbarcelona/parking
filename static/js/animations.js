$(document).ready(function(){

$(window).load(function() {
    $('#intro').delay(5000).fadeOut();
  });


/*var height = $(window).height()-80;
$("#container").css("height",height);*/



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
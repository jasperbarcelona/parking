$(document).ready(function(){

/*$('#intro').delay(4000).fadeOut(1500);*/

$(".buttons").click(function(){
	var height = $(window).height();
	$(this).css({ "position": "absolute","left":"0"});
   $(this).animate({height: "100%", width: "100%"}, "slow");
});

});
$(document).ready(function(){

$('#intro').delay(4000).fadeOut(1500);
$('#content').delay(6000).fadeIn();


$("#container").scroll(function () {
    if ($("#container").scrollTop() > 40) {
        $('#head').hide();
    }
    else{
    	$('#head').show();
    } 
});


$(".glyphicon-align-justify").click(function(){
	$("#navigation").toggle();
	$(this).toggleClass("clicked unclicked");
	$("#container").toggleClass("containerClicked containerUnclicked");
});


});
$(document).ready(function(){

$(window).load(function() {
    $('#intro').delay(5000).fadeOut();
  });

var height = $(window).height()-60;
$("#container").css("height",height);
$("#searchResult").css("height",height);


$(window).resize(function(){
	var height = $(window).height()-60;
	$("#container").css("height",height);
	$("#searchResult").css("height",height);
});

$(".rows").on('click', function() {
	$(this).animate({"margin-left":"100%"},300,'easeInSine');
});


$("#search").on('click', function() {
	$(".toggleClicked").switchClass( "toggleClicked", "toggleUnclicked" );
	$(".navClicked").switchClass( "navClicked", "navUnclicked" );
	$("#head").animate({"left":"-100%"},300,'jswing');
	$("#searchHead").animate({"left":"0"},300,'jswing');
	$("#searchResult").animate({"top":"60px"},300,'jswing');
});


$("#backSearch").on('click', function() {
	$("#head").animate({"left":"0"},300,'jswing');
	$("#searchHead").animate({"left":"100%"},300,'jswing');
	$("#searchResult").animate({"top":"100%"},300,'jswing');
});

$("#backTheme").on('click', function() {
	$("#head").animate({"left":"0"},300,'jswing');
	$("#themeHead").animate({"left":"-100%"},300,'jswing');
});


$("#parking").on('click', function() {
	var $this = jQuery(this);
    if ($this.data('activated')) return false;  // Pending, return

    $this.data('activated', true);
    setTimeout(function() {
        $this.data('activated', false)
    }, 500); // Freeze for 500ms

	$(".navUnclicked").switchClass( "navUnclicked", "navClicked" );
	$(".navClicked").switchClass( "navClicked", "navUnclicked" );
	$(".toggleUnclicked").switchClass( "toggleUnclicked", "toggleClicked" );
	$(".toggleClicked").switchClass( "toggleClicked", "toggleUnclicked" );

	return false; 
});

$("#changeTheme").on('click', function() {

	$(".toggleClicked").switchClass( "toggleClicked", "toggleUnclicked" );
	$(".navClicked").switchClass( "navClicked", "navUnclicked" );
	$("#head").animate({"left":"110%"});
	$("#themeHead").animate({"left":"0"});

	return false; 
});


var mousewheelevt = (/Firefox/i.test(navigator.userAgent)) ? "DOMMouseScroll" : "mousewheel" //FF doesn't recognize mousewheel as of FF3.x
$('#container').bind(mousewheelevt, function(e){

    var evt = window.event || e //equalize event object     
    evt = evt.originalEvent ? evt.originalEvent : evt; //convert to originalEvent if possible               
    var delta = evt.detail ? evt.detail*(-10) : evt.wheelDelta //check for detail first, because it is used by Opera and FF

    if(delta > 0) {
        $("#head").animate({"top":"0px"});
    }
    else{
        $("#head").animate({"top":"-60px"});
    }   
});



});
$(document).ready(function(){

$(window).load(function() {
    $('#intro').delay(5000).fadeOut();
  });


/*var height = $(window).height()-60;
$("#container").css("height",height);
$("#searchResult").css("height",height);


$(window).resize(function(){
	var height = $(window).height()-60;
	$("#container").css("height",height);
	$("#searchResult").css("height",height);
});*/

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

$(function(){
    var _top = $("#container").scrollTop();
    var _direction;
    $("#container").scroll(function(){
        var _cur_top = $("#container").scrollTop();
        if(_top < _cur_top)
        {
           $("#head").animate({"top":"-60px"});
        }
        else
        {
            $("#head").animate({"top":"0"});
        }
        _top = _cur_top;
        console.log(_direction);
    });
});


});
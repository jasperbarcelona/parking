$(document).ready(function(){

var refreshMap;
var refreshSlotCount;
/*clearInterval(refresh);
clearInterval(refreshSlotCount);*/

$('#loading').hide();

$(window).load(function() {
    $('#intro').delay(5000).fadeOut();
  });


var height = $(window).height()-60;
$("#container").css("height",height);


$(window).resize(function(){
	var height = $(window).height()-60;
	$("#container").css("height",height);
});


$("#search").on('click', function() {
	$(".toggleClicked").switchClass( "toggleClicked", "toggleUnclicked", 500 );
	$(".navClicked").switchClass( "navClicked", "navUnclicked", 500 );
	$("#head").animate({"left":"-100%"}, 500,'jswing');
	$("#searchHead").animate({"left":"0"}, 500,'jswing');
});


$("#zoomIn").on('click', function() {
	var element = document.getElementById('mapContainer'),
    style = window.getComputedStyle(element),
    zoom = style.getPropertyValue('zoom')*100;
    newZoom = zoom + 10;
    if(newZoom <= 130){
    	$("#mapContainer").css("zoom",newZoom+"%");
    }
});


$("#zoomOut").on('click', function() {
	var element = document.getElementById('mapContainer'),
    style = window.getComputedStyle(element),
    zoom = style.getPropertyValue('zoom')*100;
    newZoom = zoom - 10;
	if(newZoom >= 25){
    	$("#mapContainer").css("zoom",newZoom+"%");
    }
});


$("#backSearch").on('click', function() {
	$("#head").animate({"left":"0"}, 500,'jswing');
	$("#searchHead").animate({"left":"100%"}, 500,'jswing');
});


$("#backTheme").on('click', function() {
	$("#head").animate({"left":"0"}, 500,'jswing');
	$("#themeHead").animate({"left":"-100%"}, 500,'jswing');
});


$(".rows").on('click', function() {
	$("#controlPanel").show();
	$("#container").css("overflow-x","scroll");
	$("#toggleDown").hide();
	$("#parking").hide();
	$("#backMap").show();
	$(".mapName").show();

	setTimeout(function getCount(page){
	$.post('/count',
	function(data){
	$('#controlLeft').html(data);
	});
	},3000);

	refresh = setInterval(function refresh(){
	$.post('/refresh',
	function(data){
	$('#container').html(data);
	});
	},5000);

	refreshSlotCount = setInterval(function refreshcount(){
	$.post('/refreshcount',
	function(data){
	$('#controlLeft').html(data);
	});
	},6000);
});


$("#backMap").on('click', function() {
	clearInterval(refresh);
	clearInterval(refreshSlotCount);
	$("#controlPanel").hide();
	$("#container").css("overflow-x","hidden");
	$("#backMap").hide();
	$(".mapName").hide();
	$("#toggleDown").show();
	$("#parking").show();
	
});

$("#parking").on('click', function() {
	var $this = jQuery(this);
    if ($this.data('activated')) return false;  // Pending, return

    $this.data('activated', true);
    setTimeout(function() {
        $this.data('activated', false)
    }, 500); // Freeze for 500ms

	$(".navUnclicked").switchClass( "navUnclicked", "navClicked", 500 );
	$(".navClicked").switchClass( "navClicked", "navUnclicked",500 );
	$(".toggleUnclicked").switchClass( "toggleUnclicked", "toggleClicked", 500  );
	$(".toggleClicked").switchClass( "toggleClicked", "toggleUnclicked", 500  );

	return false; 
});


$("#changeTheme").on('click', function() {

	$(".toggleClicked").switchClass( "toggleClicked", "toggleUnclicked" );
	$(".navClicked").switchClass( "navClicked", "navUnclicked" );
	$("#head").animate({"left":"110%"});
	$("#themeHead").animate({"left":"0"});

	return false; 
});

});
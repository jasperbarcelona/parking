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
	var $this = jQuery(this);
        if ($this.data('activated')) return false;  // Pending, return

        $this.data('activated', true);
        setTimeout(function() {
            $this.data('activated', false)
        }, 500); // Freeze for 500ms
        
	$("#navigation").stop().slideToggle();
	$(".toggleUnclicked").switchClass( "toggleUnclicked", "toggleClicked" );
	$(".toggleClicked").switchClass( "toggleClicked", "toggleUnclicked" );
	$("#container").toggleClass("containerClicked containerUnclicked");
	
	return false; 
});


});

function map(page){
$('#loading').show();
var page = page;
$.post('/map',{page:page},
function(data){
$('#container').html(data);
$('#loading').hide();
$('#controlLoad').hide();
});
}






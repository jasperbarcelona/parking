function map(page){
$('#loading').show();
var page = page;
$.post('/map',{page:page},
function(data){
$('#container').html(data);
});
$('#loading').hide();
}

setTimeout(function getCount(page){
$.post('/count',
function(data){
$('#controlLeft').html(data);
});
},2000);

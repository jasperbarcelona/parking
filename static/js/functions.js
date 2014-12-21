function map(page){
var page = page;
$.post('/map',{page:page},
function(data){
$('#container').html(data);
});
getCount();
}

function getCount(page){
$.post('/count',
function(data){
$('#controlLeft').html(data);
});
}

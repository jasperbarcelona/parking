function map(page){


var page = page;
$.post('/map',{page:page},
function(data){
$('#container').html(data);
});
}




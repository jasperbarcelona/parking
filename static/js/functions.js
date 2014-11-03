function channel_click(){

setTimeout(function nextpage(){
$.post('/nextpage',
function(data){
$('#container').html(data);
});
},2000)

}
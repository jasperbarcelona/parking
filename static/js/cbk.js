function updateTextInput(val) {
var hour = val/60
var minutes = val%60
if(minutes<10){
	min = "0" + minutes;
}
else{
	min = minutes;
}
  document.getElementById('timeOutput').value=parseInt(hour) + ":" + min;
}

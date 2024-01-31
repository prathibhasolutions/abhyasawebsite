var img = document.getElementById('img');
var slideshow = ['b.jpg','c.jpg']
var Start=0;
function slider(){
    if(Start<slideshow.length){
        Start=Start+1;}
    else{
        Start=1;
    }    
}
setInterval(slider,2000);
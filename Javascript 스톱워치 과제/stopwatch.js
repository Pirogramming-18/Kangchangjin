let seconds=0;
let millis=0;

const appendmillis=document.getElementById("tenmillis");
const appendseconds=document.querySelector('#seconds');
const buttonstart=document.querySelector('#start');
const buttonstop=document.querySelector('#stop');
const buttonreset=document.querySelector('#reset');


console.log(buttonstart)

buttonstart.onclik=function(){
    setInterval(operatetimer,10)
}

function operatetimer(){
    millis++;
    appendmillis.textContent=millis;
    
}
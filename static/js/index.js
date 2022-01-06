// variables
const click1 = new Audio("/static/sound/click1.mp3");
const click2 = new Audio("static/sound/click2.mp3");
var isPlaying = false;
var play = null;
let beatsPerMeasure = 4;
let count = 0;


const getBPM = id => {
    let bpm = document.getElementById(id).id.split('-')[1];
    let idTd = document.getElementById(id);
    if(isPlaying){
        clearInterval(play);
        idTd.innerHTML = (
            `<img id='${bpm}' src="https://img.icons8.com/ios-glyphs/30/000000/play--v1.png" />`
        );
    }
    else {
        play = setInterval(playBeat, 60000/bpm);
        idTd.innerHTML = (
            `<img id='${bpm}' src="https://img.icons8.com/ios-glyphs/30/000000/pause--v1.png" />`
        );
        
    }
    isPlaying = !isPlaying;
}

const playBeat = () => {
    click2.play();
}

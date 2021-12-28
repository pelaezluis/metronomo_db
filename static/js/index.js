// variables
const click1 = new Audio("/static/sound/click1.mp3");
const click2 = new Audio("static/sound/click2.mp3");
var isPlaying = false;

const getId = id => {  
    console.log('now is ' + isPlaying)

    let bpm = parseInt(id.split('-')[1])
    let idTd = document.getElementById(id)

    let click = setInterval( () => {
        click2.play()
    }, 60000/bpm)

    if (isPlaying === false){
        idTd.innerHTML = (
            `<img id='${bpm}' src="https://img.icons8.com/ios-glyphs/30/000000/pause--v1.png" />`
        );
        console.log('tocando')
    }
    else if (isPlaying === true){
        idTd.innerHTML = (
            `<img id='${bpm}' src="https://img.icons8.com/ios-glyphs/30/000000/play--v1.png" />`
        );
        console.log('pausando')
        clearInterval(click)
    }
    isPlaying = !isPlaying;
}

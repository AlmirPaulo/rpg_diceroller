// Variables

const btn = document.getElementById('btn');
const out = document.getElementById('out');
// const storage = ...

// Setting Websocket
const socket = io.connect('localhost:8000/room', {'transports': ["websocket"]}); //Remember change host when dep


// Data to dice roller
function roll () {
    const player = document.getElementById('player').value
    const action = document.getElementById('action').value
    const dice_pile = document.getElementById('dice-pile').value
    const dice = document.getElementById('dice').value
    const mod = document.getElementById('mod').value
    const date = new Date().toString()

    const data = {"player":player, "action":action, "dice_pile":dice_pile, "dice":dice,"mod":mod,"date":date}
   console.log(data) 
    socket.emit('roll', data)
    console.log('data sent')
    

};

btn.addEventListener('click', roll)

socket.on('result', (output) =>{
   console.log(output); 

});

function close_ws(){ socket.close()};
    
window.addEventListener("beforeunload", close_ws)

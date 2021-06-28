// Variables
const btn = document.getElementById('btn');
const out = document.getElementById('out');
const storage = localStorage;
const socket = io({transports:['websocket']});

//Send data to dice roller
function roll () {
    const player = document.getElementById('player').value;
    const action = document.getElementById('action').value;
    const dice_pile = document.getElementById('dice-pile').value;
    const dice = document.getElementById('dice').value;
    const mod = document.getElementById('mod').value;
    const date = new Date().toString();

    const data = {"player":player, "action":action, "dice_pile":dice_pile, "dice":dice,"mod":mod,"date":date}
    socket.emit('roll', data)
};

btn.addEventListener('click', roll)


socket.on('result', (output) =>{
    //Insert a roll log in local storage
    const salt = Math.random().toString();
    storage.setItem('roll_log_'+salt, output);

    //Show roll results on the page
    const roll_result = document.createElement('p');
    const roll_result_text = document.createTextNode(output);
    roll_result.appendChild(roll_result_text);

    out.insertAdjacentElement('afterbegin',roll_result)    

});

//Bug handle for Firefox
function close_ws(){ socket.close()};
    
window.addEventListener("beforeunload", close_ws);


//Print the whole log of rolls
    //Precisa arrumar, esta devolvendo tudo bagunçado
for (let k in storage){
    //Show roll results on the page
    if(k.includes('roll_log')){
    let roll_result = document.createElement('p');
    let roll_result_text = document.createTextNode(`${storage[k]}`);
    roll_result.appendChild(roll_result_text);
    out.insertAdjacentElement('afterbegin',roll_result) 
    };
};

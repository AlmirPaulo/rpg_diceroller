from browser import websocket, document, html, window, local_storage,console
import random, time

#Global variables
btn = document['btn']
out = document['out']

#Setting Local Storage 
storage = local_storage.storage

#Setting Websocket 
ws = websocket.WebSocket("ws://localhost:5000/room")
console.log(ws)

# Diceroller
def diceroller(ev):
#Local variables
    player = document['player'].value
    action = document['action'].value
    dice_pile = document['dice-pile'].value 
    dice = document['dice'].value
    mod = document['mod'].value
    date = time.asctime()
    total = 0
    salt = str(random.randint(10000, 99999)) #for the local storage

    json = {'player':player, "action":action, "dice_pile":dice_pile, "dice":dice,"mod":mod,"date":date, "results":[],"total":total}

    w(json)

#Event Listener
btn.bind('click', diceroller)

def show_result(ev):
   #local storage log
    console.log(ev.data)
    storage['roll_log'+salt] = ev['ouput']

    #parsing output to HTML
    output_html = html.P(ev['output'])
    out.insertAdjacentElement('afterbegin',output_html)    

#socket.on('roll_result', show_result)


def ws_check(ev):
    console.log('connection open')
ws.bind('open', ws_check)
    

#print the roll log
for i in storage.values():
    out <= html.P(i)

#Firefox Issue
def close_socket(ev):
    ws.close()
window.addEventListener('beforeunload', close_socket)


from browser import document, html, window, local_storage,console
import random, time

#Global variables
btn = document['btn']
out = document['out']

#Setting Local Storage 
storage = local_storage.storage

#Setting Websocket 
socket = window.io.connect('localhost:5000/room', {'transports': ["websocket"]}) #Remember change host when deploy

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
    
    socket.emit("roll", json)

#Event Listener
btn.bind('click', diceroller)

def show_result(data):
   #local storage log
    storage['roll_log'+salt] = data['ouput']

    #parsing output to HTML
    output_html = html.P(data['output'])
    out.insertAdjacentElement('afterbegin',output_html)    

socket.on('roll_result', show_result)

#print the roll log
for i in storage.values():
    out <= html.P(i)

#Firefox Issue
def close_socket(ev):
    socket.close()

window.addEventListener('beforeunload', close_socket)


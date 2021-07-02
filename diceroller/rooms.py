from flask import Blueprint, request, flash
from flask_socketio import join_room
from . import views, socket
import random, logging

room_bp = Blueprint('room', __name__)

logging.basicConfig(level=logging.DEBUG)


@room_bp.route('/room')
def room():
    return views.room()

@room_bp.route('/', methods=['GET', 'POST'])
@socket.on('join')
def index():
    if request.method == 'POST':
        #Variables
        global room
        title = request.form.get('title')
        passwd = request.form.get('passed')
        enter_btn = request.form.get('enter')
        create_btn = request.form.get('create')
        if create_btn == 'create':
            if data['passwd'] > 12:
                flash('Your password is too long. Maximum 12 characters.')
            elif data['passwd'] < 8:
                flash('Your password is too short. Minimum 8 characters.')
            else:
                #hash password and save data in DB
                #Then, Join room
                logging.debug('Create working!!!!')
                logging.debug(create_btn)
                room = data['room']
                #redirect
                join_room(room)            
        elif enter_btn == 'enter': #and data['password'] == ...
            #Join room socket io
            logging.debug('Enter Working!!!')
            logging.debug(enter_btn)
            room = data['room']
            #redirect
            join_room(room)            


    return views.index()

@socket.on('roll')
def diceroller(data):
    #variables
    global room
    player = data['player']
    action = data['action']
    dice_pile = data['dice_pile']
    dice_pile_msg = dice_pile
    dice = data['dice']
    mod = data['mod']
    date = data['date']
    results = []   
    total = 0
    
    #rolling dices
    while int(dice_pile) > 0:
        if dice == 'd3':
            results.append(random.randint(1,3))

        elif dice == 'd4':
            results.append(random.randint(1,4))

        elif dice == 'd6':
            results.append(random.randint(1,6))
      
        elif dice == 'd8':
            results.append(random.randint(1,8))

        elif dice == 'd100':
            results.append(random.randint(1,100))

        elif dice == 'd10':
            results.append(random.randint(1,10))

        elif dice == 'd12':
            results.append(random.randint(1,12))

        elif dice == 'd20':
            results.append(random.randint(1,20))


        dice_pile = int(dice_pile) -1
        
    #Roll sum, with modifier
    for n in results:
        total = total +n

    total = total + int(mod)

    roll = []

    #Parsing back to string and formatting
    for i in results:
        roll.append(str(i))
     
    output = f"{date} - {player} tried to {action} and rolled {dice_pile_msg}{dice} + {mod}. Results: {', '.join(roll)}. Total= {total}."
    socket.emit('result',output, to=room)






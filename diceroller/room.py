from flask import Blueprint
from . import views, socket
import random

room_bp = Blueprint('room', __name__)


@socket.on('roll')
def diceroller(data):
    #variables
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
    socket.emit('result',output, broadcast=True)



@room_bp.route('/room')
def room():
    return views.room()

from browser import document, html, websocket
import random, time

btn = document['btn']

# Diceroller
def diceroller(ev):
#Variables
    card = document['card']
    player = document['player'].value
    action = document['action'].value
    dice_pile = document['dice-pile'].value 
    dice = document['dice'].value
    dice_pile_msg = dice_pile
    results = []
    total = 0
    mod = document['mod'].value
  # rolling the dices
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

    for n in results:
        total = total +n

    total = total + int(mod)

    roll = []

    for i in results:
        roll.append(str(i))
    
    date = time.asctime()
    
    output = f"{date} - {player} tried to {action} and rolled {dice_pile_msg}{dice} + {mod}. Result: {', '.join(roll)}. Modifier= {mod} Total= {total}."
        
    #parsing output to HTML
    output_html = html.P(output, Class='card-text')
    card <= output_html    

btn.bind('click', diceroller)

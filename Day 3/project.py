print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print('Welcome to Treasure Island')
print('Your mission is to find the treasure')

choise1 = input('Where do you want to go? Type "right" or "left": ').lower()

if choise1 != "left":
    print('You fell in to a hole. Game Over!')

else:
    choise2 = input('You\'ve come to a lake, there is an island in the middle of the lake. Type "wait" to wait for the boat or "swim": ').lower()

    if choise2 != 'wait':
        print("You were attacked by trout. Game over!")
    else:
        print('You come across three doors. Which do you choose?')
        choise3 = input('red, blue or yellow: ').lower()

        if choise3 == 'yellow':
            print('Congratulations. Your Win!')
        elif choise3 == 'Red':
            print('You were burned by fire. Game over')
        elif choise3 == 'Blue':
            print('You were eaten by wild beasts. Game over')
        else:
            print('Game Over!')
        
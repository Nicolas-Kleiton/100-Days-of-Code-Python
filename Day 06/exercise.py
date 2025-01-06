# https://reeborg.ca/reeborg.html

# Simulação das funções de movimento
def move():
    print("Move forward")

def turn_left():
    print("Turn left")

def at_goal():
    return False  

def wall_in_front():
    return False 

# Simule a função turn_right()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Função jump() com lógica
def jump():
    while wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    move()

# Loop principal
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
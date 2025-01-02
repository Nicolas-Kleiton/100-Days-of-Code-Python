# https://reeborg.ca/reeborg.html

# Simulando funções do ambiente de robô
def move():
    print("Move forward")

def turn_left():
    print("Turn left")

def right_is_clear():
    # Simule o comportamento da função, por exemplo:
    return False  # Troque True ou False para testar o código

def front_is_clear():
    return True  # Troque para False se quiser simular uma parede

def at_goal():
    return False  # Simule o objetivo (True quando alcançado)

# Definindo turn_right() com base em turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Programa principal
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif not right_is_clear():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_left()
        move()

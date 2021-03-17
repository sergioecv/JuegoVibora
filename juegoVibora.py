#Librerías
from turtle import *
from random import randrange
from freegames import square, vector

#Inicialización de variables
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
aim1 = vector(0, -10)

#Asigna números que serán asignados a un color
color_s = randrange(1,6)
color_f = randrange(1,6)

#Revisa que sean números diferentes
while color_f == color_s:
    color_f = randrange(1,6)

#Método que define el color en base al número random
def setColor(num):
    if num==1:
        color = 'green'
    elif num ==2:
        color = 'pink'
    elif num ==3:
        color = 'blue'
    elif num ==4:
        color = 'yellow'
    elif num ==5:
        color = 'gray'
    return color

#Cambia de direccion la serpiente
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

#Se agrego if para que la comida se pueda moverse al azar un paso a la vez  
    if x == 0:
        if y > 0:
            aim1.y = aim1.y + randrange(1, 10) * 10
        else:
            aim1.y = aim1.y + randrange(1, 10) * -10
    elif y == 0:
        if x > 0:
            aim1.x = aim1.x + randrange(1, 10) * 10
        else:
            aim1.x = aim1.x + randrange(1, 10) * -10
#limites            
    if not inside(aim1):
        if x == 0:
            if y > 0:
                aim1.y = -190 + randrange(1, 10) * 10
            else:
                aim1.y = 180 + randrange(1, 10) * -10
        elif y == 0:
            if x > 0:
                aim1.x = -190 + randrange(1, 10) * 10
            else:
                aim1.x = 180 + randrange(1, 10) * -10
        update()
        
#Regresa True si la cabeza está dentro de los límites    
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

#Avanza la serpiente un segmento y asigna el color a la comida y serpiente
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

 #si se sale del limite o se va en contra de la direccion se termina el juego
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    food.x = aim1.x
    food.y = aim1.y
   
#se modifico para que la comida se siga moviendo al azar una vez la serpiente la haya obtenido
    if head == food:
        print('Snake:', len(snake))
        aim1.x = randrange(-15, 15) * 10
        aim1.y = randrange(-15, 15) * 10
        food.x = aim1.x
        food.y = aim1.y
    else:
        snake.pop(0)

    clear()

 # se tiene de manera aleatoria 5 colores para la serpiente y la comida y es de manera aleatoria.
    for body in snake:
        square(body.x, body.y, 9, setColor(color_s))

    square(food.x, food.y, 9, setColor(color_f))
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

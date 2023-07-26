"""esse script usa o módulo turtle para desenhar efeito de circulo
"""
import turtle as t
import time
import colorsys

# Configurações da tela
screen = t.Screen()
screen.title('Circulo')
screen.bgcolor('black')
screen.tracer(2)

# Inciar variáveis
HUE = 0.5
STEP = 10

# criar uma caneta
pen = t.Turtle()
pen.pensize(1.4)
pen.speed(0)
time.sleep(2)

# Loop para desenhar o círculo
for i in range(350):
    # cor em rgb
    color_rgb = colorsys.hsv_to_rgb(HUE, 1, 1)
    HUE += 0.005

    # Configurações da caneta
    pen.pencolor(color_rgb)

    # Desenhar o círculo
    pen.right(20)
    pen.forward(i)
    pen.left(70)
    pen.forward(i)
    pen.circle(5, STEP)
    pen.left(60)
    pen.circle(HUE, 1)

# Finalizar o programa
t.done()

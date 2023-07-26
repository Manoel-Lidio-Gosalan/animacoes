"""esse script usa o módulo turtle para desenhar efeito de estrela
"""

import turtle as t
import colorsys

# tela
screen = t.Screen()
screen.title('Estrela')
screen.bgcolor('black')
screen.tracer(10)

# variaveis
M = 0.9
N = 95
# criar uma caneta
pen = t.Turtle()
pen.pensize(1.4)
pen.speed(0)

for i in range(450):
    # cor em rgb
    color_rgb= colorsys.hsv_to_rgb(M,1,1)
    # Configurações da caneta
    M += 0.005
    # Desenhar a estrela
    pen.color(color_rgb)
    pen.right(90)
    pen.forward(i+1)
    pen.left(90)
    pen.forward(i)
    pen.circle(2,N)
    pen.left(120)
    pen.circle(M,1)
    pen.hideturtle()
t.done()

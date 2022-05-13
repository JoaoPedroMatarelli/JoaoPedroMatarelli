"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
from freegames import square, vector
import sys
import os
from tkinter import *
from tkinter import messagebox


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
cores =  ['Black', 'Red', 'Blue', 'Purple', 'Purple', 'Aqua']
cor_pos = 1

class MinhaGUI:
 def __init__(self):
  # Criamos a janela principal
  self.janela_principal = Tk()
  
  # Criando os botões
  self.botao = Button(self.janela_principal, text='Clique aqui', command=self.jogo())
  self.botao_sair = Button(self.janela_principal, text='Sair', command=self.janela_principal.quit)
  
  # Empacotando os botões janela principal
  self.botao.pack()
  self.botao_sair.pack()
  
  # Rodando
  mainloop()

  
 
 def jogo(self):
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

objeto = MinhaGUI()







def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        gui = MinhaGUI()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        cor_pos =+ 1
        square(body.x, body.y, 9, cores[cor_pos])
        

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

def jogo():
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

jogo()
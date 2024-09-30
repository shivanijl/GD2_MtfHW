import pygame
import turtle
sc=turtle.Screen()
pen=turtle.Turtle()
pygame.init()
screen= pygame.display.set_mode((600,600))
screen.fill((255,255,255))
pygame.display.update()
sides = int(input("Enter the number of sides"))
for i in range(sides):
    pen.forward(150)
    pen.right(360/sides)







pygame.display.update()
import pygame
import sys
from pygame.color import THECOLORS

pygame.init()
# Создание экрана
screen = pygame.display.set_mode((1200,800)) # Размер экрана
image = pygame.image.load("kat.jpg") #Картинка героя
pygame.display. set_caption("MyOneGame") # Название игры
bg = pygame.image.load("Landscape.png") # Картинка фона
bg = pygame.transform.scale(bg,(1200,800)) # Расширения фона

screen.blit(bg,(0,0)) #Начальная точка фона
image = pygame.transform.scale(image,(30,32)) # Размер картинки героя
x = 600 # Начальная точка героя
y = 400 # Начальная точка героя
screen.blit(image, (x,y)) # Начальная точка героя
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()
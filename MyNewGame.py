import pygame
import time
import sys
import random

#стартуем в файле модули пайгейм
pygame.init()

#Размер окна
display_widht = 1920 # Высота
display_height = 1080 # Ширина

# Окно игры
gameDisplay = pygame.display.set_mode((display_widht,display_height)) # размер
pygame.display.set_caption("Car_win") # название игры

# Цвета
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#кадры в секунду
clock = pygame.time.Clock()

car_speed = 0 # Скорость

# Игрок
carImg = pygame.image.load('image/car_green.png') #картинка для игрока
carImg = pygame.transform.scale(carImg, (92,165))  #задаём размер картинки для игрока
car_width = 73
# функция для появления препятствий
def things (thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
# отрисовка авто
def car(x,y):
    gameDisplay.blit(carImg,(x,y))
# Обработка текста
def text_objects (text,font):
    textSurface = font.render (text,True,black)
    return textSurface, textSurface.get_rect()
# вывод текста на экран
def message_display (text):
    largeText= pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect = text_objects(text,largeText)
    TextRect.center = ((display_widht/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
def crash():
    message_display('Учись водить')


# Блок для запуска
def game_loop():
    #размещение авто
    x = (display_widht * 0.45)
    y = (display_height * 0.7)

    # параметры для появления thing
    thing_startx = random.randrange(0,display_widht)
    thing_starty = -600
    thing_speed = 5
    thing_widht = 100
    thing_height = 100

    x_change = 0  # Позиция
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                sys.quit()
                # блок для обработки нажатия на клавиши
            if event.type == pygame.KEYDOWN:
                #если нажалт на esc то игра закроется
                if event.key == pygame.K_ESCAPE:
                    crashed = True
                    pygame.quit()
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            # Условие для движения
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        # Смена позиции машины
        x += x_change
    # Фон
        gameDisplay.fill(white)
        # вызов things
        things(thing_startx,thing_starty,thing_widht,thing_height,black)
        thing_starty+=thing_speed


    #создаём машину
        car(x,y)
        if x > display_widht - car_width or x < 0: #Границы движения
            crashed = True
            crash()
        if thing_starty>display_height:
           thing_starty = 0-thing_height
           thing_startx = random.randrange(0,display_widht)

    # проверяем на обнавление
        pygame.display.update()
    # кадры в секунду = 60
        clock.tick(60)
game_loop()
pygame.quit()
quit()




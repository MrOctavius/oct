from pygame import *
from random import *
from time import time as timer
window = display.set_mode((700, 500))
display.set_caption("Пин-понг")


background = transform.scale(image.load("kort.jpg"),(700, 500))

font.init()
font1 = font.SysFont('Arial', 36)

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self): 
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys_pressed[K_DOWN] and self.rect.y < 630:
            self.rect.y += self.speed
    def update_2(self): 
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 630:
            self.rect.y += self.speed 

class Ball(GameSprite): 
    def update(self):
        pass





    
ball = Ball('tennis-ball.png', 50, 60, 10)
man = Player('brusli.png', 100, 120, 10)
man2 = Player('brusli2.png', 200, 210, 10)

finish = False
game = True    
    
while game:
    if not finish:
        window.blit(background,(0, 0))
        ball.reset()
        ball.update()
        man.reset()
        man.update()
        man2.reset()
        man2.update_2()



    clock.tick(FPS)
    display.update()
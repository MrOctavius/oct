from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Пин-понг")


background = transform.scale(image.load("kort.jpg"),(700, 500))

font.init()
font1 = font.SysFont('Arial', 36)

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, vid_height, vid_height1):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(vid_height, vid_height1))
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
        if keys_pressed[K_DOWN] and self.rect.y < 410:
            self.rect.y += self.speed
    def update_2(self): 
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 410:
            self.rect.y += self.speed 

class Ball(GameSprite): 
    speed_x = 3
    speed_y = 3
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.y > 410:
            self.speed_y *= -1
        if sprite.collide_rect(self, man) or sprite.collide_rect(self, man2):
            self.speed_x *= -1
        

ball = Ball('tennis-ball.png', 325, 225, 5, 40, 40)
man = Player('brusli.png', 575, 220, 10, 90, 90)
man2 = Player('brusli2.png', 40, 220, 10, 90, 90)


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

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()

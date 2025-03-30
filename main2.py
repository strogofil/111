from random import randint

from pygame import *
import time as tm


WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500

FPS= 60
class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    health = 5
    def update(self, screen):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 630:
            self.rect.x += self.speed

class Player(GameSprite):
    health = 5
    def update(self, screen):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 630:
            self.rect.x += self.speed


window = display.set_mode((700, 500))


player = Player("tank.png", 400, 400, 50,100, 10)
clock = time.Clock()

clock = time.Clock()
display.set_caption("Шутер")
FPS = 60

run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    player.update(window)
    display.update()
    clock.tick(FPS)
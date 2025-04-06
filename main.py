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

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    direction = "Left"
    health = 5
    bullets = sprite.Group()

    def update(self, screen):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
            if self.direction == "Right":
                self.direction = "Left"
                self.image = transform.flip(self.image, True, False)
        if keys[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
            if self.direction == "Left":
                self.direction = "Right"
                self.image = transform.flip(self.image, True, False)
        if keys[K_w] and self.rect.y  > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

        super().draw(screen)

    def fire(self):
        if self.direction == "Left":
            speed = -7
            x_side = self.rect.left
            y_side = self.rect.top
        else:
            speed = 7
            x_side = self.rect.left
            y_side = self.rect.top

        bullet = Bullet("enemy bullet.png", x_side, y_side, 50, 50, speed)
        self.bullets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0 or self.rect.x > 700:
            self.kill()

        self.draw(window)
class EnemyBullet(GameSprite):

    def update(self):
        self.rect.y = self.speed
        if self.rect.x > 500:
            self.kill()

lost = 0


enemy_bullets = sprite.Group()
bullets = sprite.Group()
enemies = sprite.Group()
for i in range(5):
    enemy = EnemyBullet("zombi.png", randint(0, 500), 5, 30, 55, randint(1, 3))
    enemies.add(enemy)
window = display.set_mode((700, 500))
display.set_caption("Шутер")

background = transform.scale(image.load("pole.png"), (700, 500))
player = Player("tank.png", 400, 400, 50,100, 1)

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
        if e.type == KEYDOWN and e.key == K_SPACE:
            player.fire()


    window.fill((255,255,255))
    
    enemies.update()
    enemies.draw(window)
    player.update(window)
    player.bullets.update()
    player.bullets.draw(window)

    display.update()
    clock.tick(FPS)

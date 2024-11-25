#Создай собственный Шутер!

from pygame import *
from random import *
score = 0
coal = randint(50,200)
font.init()
font2 = font.Font(None, 36)
wight = 700
hight = 500
window = display.set_mode((wight,hight))
display.set_caption("Maze")
baskground = transform.scale(image.load("galaxy.jpg"),(700,500))
run = True
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
street = 0
inf_bullet = 'utka3310.jpg'
class GES(sprite.Sprite):
    def __init__(self,player_img,player_x,player_y,size_x,size_y,player_sp):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_img),(size_x,size_y))
        self.sp = player_sp
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GES):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.sp
        if keys[K_RIGHT] and self.rect.x < wight -80:
            self.rect.x += self.sp
    def fire (self):
        bullet = Bullet(inf_bullet,self.rect.centerx,self.rect.top,15,20,-15)
        bullets.add(bullet)
class Enemy(GES):
    def update(self):
        self.rect.y += self.sp
        global street
        if self.rect.y > hight:
            self.rect.x = randint(80,wight -80)
            self.rect.y = 0
            street += 1
class Bullet(GES):
    def update(self):
        self.rect.y += self.sp
        if self.rect.y < 0:
           self.kill()
mortis = Player('3f.jpg',5,hight -100, 80,100,50)
mortis2 = sprite.Group()
bullets = sprite.Group()
for i in range(1,6):
    mortis3 = Enemy('xoccey_mortis.jpg',randint(80,wight -80),-40,80,50,randint(5,10))
    mortis2.add(mortis3)
while score < coal and not sprite.spritecollide(mortis,mortis2,False) and run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                mortis.fire()
        window.blit(baskground,(0,0))
        mortis.update()
        mortis2.update()
        bullets.update()
        mortis2.draw(window)
        mortis.reset()
        bullets.draw(window)
        sprite_list = sprite.groupcollide(mortis2,bullets,True,True)
        for s in sprite_list:
            score += 1
            mortis3 = Enemy('xoccey_mortis.jpg',randint(80,wight -80),-40,80,50,randint(5,10))
            mortis2.add(mortis3)
        if sprite.spritecollide(mortis,mortis2,False):
            run = False
        if score >= coal:
            run = True
        text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        display.update()
        clock.tick(FPS)
    #mzaicev103
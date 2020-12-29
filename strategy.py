#ПОЛНОЭКРАННЫЙ РЕЖИМ В БЕТА-ТЕСТЕ. ВОЗМОЖНЫ БАГИ
import pygame
import random as r
import os
import time

pygame.init()

pygame.display.set_caption("EndToper's cross-zero")
WHITE = (255,255,255)
BLACK = (0,0,0)
some_BLUE = (0,255,255)
#рассчет отнасительных координат 2
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
WIDTH, HEIGHT = width, height
width, height = round(width/2), round(height/2)
#print(width, height)
screen = pygame.display.set_mode((width, height))
line_width = round(width / 100)
FPS = 60
run = True
money = 200
press_f = 0
base = pygame.image.load("strategy\home.png").convert_alpha()
base_size = 50
field = pygame.image.load("strategy\pole.png").convert_alpha()
field_size = 50
t1 = pygame.image.load("strategy/tower1.png").convert_alpha()
t1_size = 50
t2 = pygame.image.load("strategy/tower12.png").convert_alpha()
t2_size = 50
t3 = pygame.image.load("strategy/tower13.png").convert_alpha()
t3_size = 50
t4 = pygame.image.load("strategy/tower14.png").convert_alpha()
t4_size = 50
buy = pygame.image.load("strategy/buy.png").convert_alpha()
buy_size = 50
ar1 = pygame.image.load("strategy/arrow.png").convert_alpha()
ar1_size = 50
prop = 0
#print(base)
clock = pygame.time.Clock()
c = 5
go = False
game_run = True
mode = False
arrows = []
mnosh = 1
towers_pos = [[width-line_width*9,line_width*6.5],[width-line_width*9,line_width*13.5],[width-line_width*9,line_width*26.5],
              [width-line_width*9,line_width*33.5],[width/2+line_width*1.5,line_width*26.5],
              [width/2+line_width*1.5,line_width*33.5],[width/2-line_width*12.5,line_width*26.5],
              [width/2-line_width*12.5,line_width*13.5],[width/2-line_width*5.5,line_width*13.5],
              [width/2+line_width*1.5,line_width*13.5],[width/2-line_width*19.5,line_width*6.5],
              [width/2+line_width*8.5,line_width*6.5],[width/2+line_width*21.5,line_width*6.5],
              [width-line_width*23,line_width*26.5],[width-line_width*30,line_width*26.5],
              [width-line_width*30,line_width*33.5],[line_width*7.5,line_width*33.5],[line_width*7.5,line_width*26.5],
              [line_width*7.5,line_width*40.5],[line_width*7.5,line_width*13.5]]


#non-constant variables
def variables():
    global width, height, WIDTH, HEIGHT, line_width
    line_width = round(width / 100)

def trans():
    home.x = line_width/2
    home.y = height-base_trans.get_height()
    home.rect.x = home.x
    home.rect.y = home.y
    


#conversions
def conversions():
    global base_size, line_width, base_trans, prop, field_size, field_trans, t1_trans, t1, t1_size, t2_trans, t2, t2_size, t3_trans, t3, t3_size, t4_trans, t4, t4_size, buy, buy_size, buy_trans, ar1, ar1_size, ar1_trans
    if base_size > 3*line_width:
        prop = base_size/(3*line_width)
        base_trans = pygame.transform.scale(base, (round(base.get_width()/prop), round(base.get_height()/prop)))
    else:
        prop = 3*line_width/base_size
        base_trans = pygame.transform.scale(base, (round(base.get_width()*prop), round(base.get_height()*prop)))
    if field_size > 3*line_width:
        prop = base_size/(3*line_width)
        field_trans = pygame.transform.scale(field, (round(field.get_width()/prop), round(field.get_height()/prop)))
    else:
        prop = 3*line_width/field_size
        field_trans = pygame.transform.scale(field, (round(field.get_width()*prop), round(field.get_height()*prop)))
    if t1_size > 3*line_width:
        prop = t1_size/(3*line_width)
        t1_trans = pygame.transform.scale(t1, (round(t1.get_width()/prop), round(t1.get_height()/prop)))
    else:
        prop = 3*line_width/t1_size
        t1_trans = pygame.transform.scale(t1, (round(t1.get_width()*prop), round(t1.get_height()*prop)))
    if t2_size > 3*line_width:
        prop = t2_size/(3*line_width)
        t2_trans = pygame.transform.scale(t2, (round(t2.get_width()/prop), round(t2.get_height()/prop)))
    else:
        prop = 3*line_width/t2_size
        t2_trans = pygame.transform.scale(t2, (round(t2.get_width()*prop), round(t2.get_height()*prop)))
    if t3_size > 3*line_width:
        prop = t3_size/(3*line_width)
        t3_trans = pygame.transform.scale(t3, (round(t3.get_width()/prop), round(t3.get_height()/prop)))
    else:
        prop = 3*line_width/t3_size
        t3_trans = pygame.transform.scale(t3, (round(t3.get_width()*prop), round(t3.get_height()*prop)))
    if t4_size > 3*line_width:
        prop = t4_size/(3*line_width)
        t4_trans = pygame.transform.scale(t4, (round(t4.get_width()/prop), round(t4.get_height()/prop)))
    else:
        prop = 3*line_width/t14_size
        t4_trans = pygame.transform.scale(t4, (round(t4.get_width()*prop), round(t4.get_height()*prop)))
    if buy_size > 3*line_width:
        prop = buy_size/(3*line_width)
        buy_trans = pygame.transform.scale(buy, (round(buy.get_width()/prop), round(buy.get_height()/prop)))
    else:
        prop = 3*line_width/buy_size
        buy_trans = pygame.transform.scale(buy, (round(buy.get_width()*prop), round(buy.get_height()*prop)))
    if ar1_size > 3*line_width:
        prop = ar1_size/(3*line_width)
        ar1_trans = pygame.transform.scale(ar1, (round(ar1.get_width()/prop), round(ar1.get_height()/prop)))
    else:
        prop = 3*line_width/buy_size
        ar1_trans = pygame.transform.scale(ar1, (round(ar1.get_width()*prop), round(ar1.get_height()*prop)))

conversions()
#class for base
class Home_base(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((base_trans.get_width(), base_trans.get_height()))
        self.rect = self.image.get_rect()
        self.x = line_width/2
        self.y = height-base_trans.get_height()
        self.rect.x = self.x
        self.rect.y = self.y
        self.base_health = 20
        self.chosen = False
        
    def show(self):
        screen.blit(base_trans,(self.x,self.y))

home = Home_base()





#enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,health,speed,max_health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((line_width*4, line_width*4))
        self.rect = self.image.get_rect() 
        self.color = (0,255,0)
        self.image.fill(self.color)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.rect.center = (x,y)
        self.health = health * mnosh
        self.max_health = max_health * mnosh
        self.speed = speed
        self.motion = 'x'
        self.motion_type = -1
        self.delete = False
    def draw_enemy(self):
        self.image.fill(self.color)
        screen.blit(self.image,(self.x,self.y))
        if self.motion == "x":
            self.x = self.x + self.speed * self.motion_type
        if self.motion == "y":
            self.y += self.speed * self.motion_type
        if self.x <= line_width*1.5:
            self.motion = "y"
            self.motion_type = 1
        if width/2-line_width*5 <= self.x <= width/2-line_width*4.5 and line_width*40 <= self.y <= line_width*45:
            self.motion = "y"
            self.motion_type = -1
        if width/2-line_width*5 <= self.x <= width/2-line_width*4.5 and self.y <= line_width*21:
            self.motion = "x"
            self.motion_type = -1
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.max_health == 15:
            self.color = (255,255,0)
        if self.max_health == 20:
            self.color = (0,0,255)
        if self.max_health == 25:
            self.color = (125,0,125)
        if self.max_health == 30:
            self.color = (255,0,0)
        for arrow in arrows:
            if self.rect.colliderect(arrow.rect):
                self.health -= arrow.damage
                arrows.remove(arrow)
        if self.rect.colliderect(home.rect) and self.delete == False:
            home.base_health = home.base_health - 1
            self.delete = True
            self.x = 1000
            self.y = 1000
            self.rect.x = self.x
            self.rect.y = self.y
            print(home.base_health)







#tower
class Towers(pygame.sprite.Sprite):
    def __init__(self,x,y): 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((line_width*4, line_width*4))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.type = None
        self.type_image = field_trans
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        screen.blit(self.type_image,(self.x,self.y))
    def buy_tower(self):
        for tower in all_towers:
            if tower.type == None and tower.type_image != field_trans:
                tower.type_image = field_trans
        self.type_image = buy_trans
    def buy_update(self, typ):
        if self.type_image == buy_trans and typ == 1:
            self.type_image = t1_trans
            self.type = "archer"
            self.arrows = 2
            self.lvl = 1
            self.time = time.time()
        if self.type_image == buy_trans and typ == 1:
            self.type_image = t1_trans
            self.type = "archer"
        if self.type_image == buy_trans and typ == 1:
            self.type_image = t1_trans
            self.type = "archer"
        if self.type_image == buy_trans and typ == 1:
            self.type_image = t1_trans
            self.type = "archer"
    def update(self):
        if self.type == 'archer':
            for i in range(self.arrows):
                arrow = Arrow(self.x, self.y,'x' if i > 2 else 'y',1 if i == 1 or i == 3 else -1, self.lvl*2)
                arrows.append(arrow)
            self.time = time.time()
    def arch_upgrade(self):
        if self.lvl == 3:
            self.lvl = 4
            self.arrows = 6
            self.type_image = t4_trans
        if self.lvl == 2:
            self.lvl = 3
            self.type_image = t3_trans
        if self.lvl == 1:
            self.lvl = 2
            self.type_image = t2_trans
        



class Arrow(pygame.sprite.Sprite):
    def __init__(self,x,y,wd,direct,dam):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((line_width*4, line_width*4))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.dir_type = wd
        self.dir = direct
        self.damage = dam
        self.lvl = dam/2
    def draw(self):
        ar1_trans_left = pygame.transform.rotate(ar1_trans, 90)
        ar1_trans_right = pygame.transform.rotate(ar1_trans, -90)
        if self.dir_type ==  'y':
            screen.blit(ar1_trans_left if self.dir == -1 else ar1_trans_right,(self.x,self.y))
        ar1_trans_up = ar1_trans
        ar1_trans_down = pygame.transform.flip(ar1_trans, 0, 1)
        if self.dir_type == 'x':
            screen.blit(ar1_trans_up if self.dir == -1 else ar1_trans_down,(self.x,self.y))
        if self.dir_type ==  'x':
            self.x += self.dir * 20 * self.lvl/4
        elif self.dir_type == 'y':
            self.y += self.dir * 20 * self.lvl/4
        self.rect.x = self.x
        self.rect.y = self.y




all_towers =[]
for i in range(20):
    tower = Towers(towers_pos[i][0],towers_pos[i][1])
    all_towers.append(tower)











all_evil = []
def generator():
    global c
    sp = 1
    h = 0
    while h <= 0:
        h = r.choice((10,15,20,25,30))
        if h > 10 and press_f < 11:
            h = 0
        if h > 15 and press_f < 26:
            h = 0
    if h == 15:
        sp = 3
    if h >= 25:
        sp = 0.4
    m_h = h
    enemy = Enemy(width, r.choice((line_width*21,line_width,line_width*41)), h, sp,m_h)
    all_evil.append(enemy)



def game_reload():
    global all_evil, home, game_run,c2,c,go
    all_evil = []
    home.base_health = 20
    game_run = True
    c2 = 0
    c = 5
    go = False



#print(base_trans)
def draw_map():
    #1 road
    pygame.draw.line(screen, some_BLUE, [0+line_width, line_width/2], [width, line_width/2], line_width)
    pygame.draw.line(screen, some_BLUE, [0+line_width*6, line_width/2+line_width*5], [width, line_width/2+line_width*5], line_width)
    #2 road
    pygame.draw.line(screen, some_BLUE, [0+line_width*6, line_width/2+line_width*20], [width, line_width/2+line_width*20], line_width)
    pygame.draw.line(screen, some_BLUE, [width/2, line_width/2+line_width*25], [width, line_width/2+line_width*25], line_width)
    pygame.draw.line(screen, some_BLUE, [0+line_width*6, line_width/2+line_width*25], [width/2-line_width*6, line_width/2+line_width*25], line_width)
    #3 road
    pygame.draw.line(screen, some_BLUE, [width/2, line_width/2+line_width*40], [width, line_width/2+line_width*40], line_width)
    pygame.draw.line(screen, some_BLUE, [width/2-line_width*6, line_width/2+line_width*45], [width, line_width/2+line_width*45], line_width)
    #combining 2 and 3 roads
    pygame.draw.line(screen, some_BLUE, [(width+line_width)/2-1, line_width/2+line_width*40], [(width+line_width)/2-1, line_width/2+line_width*25], line_width)
    pygame.draw.line(screen, some_BLUE, [width/2-line_width*5.5-1, line_width*45], [width/2-line_width*5.5-1, line_width*25+1], line_width)
    #combining 1 and 2 roads
    pygame.draw.line(screen, some_BLUE, [line_width/2-1, 1], [line_width/2-1, height], line_width)
    pygame.draw.line(screen, some_BLUE, [line_width*6.5-1, line_width/2+line_width*5], [line_width*6.5-1, line_width/2+line_width*20], line_width)
    pygame.draw.line(screen, some_BLUE, [line_width*6.5-1, line_width/2+line_width*25], [line_width*6.5-1, height], line_width)
    
    
    
    
    


#img = pygame.transform.scale(img, (img.get_width()//3, img.get_height()//3))
c2 = 0
while run:
    screen.fill(BLACK)
    clock.tick(FPS)
    draw_map()
    home.show()
    if press_f % 10 == 0:
        mnosh = 1 + press_f//100
    if home.base_health <= 0:
        game_run = False
    for tower in all_towers:
        tower.draw()
        if tower.type =='archer' and time.time() - tower.time >= 1.25 - tower.lvl/4:
            tower.update()
    for arrow in arrows:
        if all_evil != []:
            arrow.draw()
        if all_evil == []:
            arrows = []
        if -line_width*4 >= arrow.x <= width or -line_width*4 >= arrow.y <= height:
            arrows.remove(arrow)
    for enemy in all_evil:
        enemy.draw_enemy()
        enemy.update()
        if enemy.delete == True:
            all_evil.remove(enemy)
        if enemy.health <= 0:
            money+=3
            #print(f"die, {10 * mnosh}")
            all_evil.remove(enemy)

    if go == True and time.time() - t >= 2 and c2 != c:
        c2 += 1
        generator()
        t = time.time()
    if go == True and time.time() - t >= 2 and c2 == c:
        c += 1
        c2 = 0
        go = False
        t = 0
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                run = False
            if i.key == pygame.K_f and go == False:
                go = True
                t = time.time() / 100
                press_f += 1
            elif pygame.key.get_pressed()[pygame.K_F5] and mode == False and game_run == True:
                width, height = WIDTH, HEIGHT
                pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
                mode =  True
                pygame.display.update()
                variables()
                conversions()
                trans()
            elif pygame.key.get_pressed()[pygame.K_F5] and mode == True and game_run == True:
                width, height = round(WIDTH/2), round(HEIGHT/2)
                pygame.display.set_mode((width, height))
                mode =  False
                pygame.display.update()
                variables()
                conversions()
                trans()
            elif pygame.key.get_pressed()[pygame.K_1] and money >= 50:
                for tower in all_towers:
                    tower.buy_update(1)
                money -= 50
        elif i.type == pygame.MOUSEBUTTONDOWN:
            for tower in all_towers:
                if tower.rect.collidepoint(pygame.mouse.get_pos()) and game_run == True:
                    if tower.type==None:
                        tower.buy_tower()
                    if tower.type == 'archer' and money >= 50 * tower.lvl and tower.lvl != 4:
                        money -= 50 * tower.lvl
                        tower.arch_upgrade()
    
    if i.type == pygame.MOUSEBUTTONDOWN and game_run == False:
            game_reload()
    if game_run == False:
        fontObj = pygame.font.Font('freesansbold.ttf', 25)
        textSurfaceObj = fontObj.render(f'Вы проиграли. Нажмите для рестарта. ', False, some_BLUE, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (width/2,height/2)
        screen.blit(textSurfaceObj, textRectObj)
        
    
    fontObj = pygame.font.Font('freesansbold.ttf', round(line_width* 2.5))
    textSurfaceObj = fontObj.render(f'жизни: {home.base_health}', False, some_BLUE, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (line_width*15,height-line_width*3)
    screen.blit(textSurfaceObj, textRectObj)
    
    fontObj = pygame.font.Font('freesansbold.ttf', round(line_width* 2.6))
    textSurfaceObj = fontObj.render(f'деньги: {money}', False, some_BLUE, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (line_width*30,height-line_width*3)
    screen.blit(textSurfaceObj, textRectObj)
    
    fontObj = pygame.font.Font('freesansbold.ttf', round(line_width* 2.6))
    textSurfaceObj = fontObj.render(f'прожито волн: {press_f}', False, some_BLUE, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (line_width*55,height-line_width*3)
    screen.blit(textSurfaceObj, textRectObj)
    pygame.display.flip()


pygame.quit()
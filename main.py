import pygame
import random
import os #Using to the best score
pygame.init()
f_l = os.listdir()
if "best_score.txt" not in f_l :
    doc = open("best_score.txt","w")
    doc.write('0$vvvv')
    doc.close()
    best_score = 0
    name_score = "vvvv"
else :
    doc = open("best_score.txt","r")
    ls = doc.read().split('$')
    best_score = int(ls[0])
    name_score = str(ls[1])
    doc.close()

clock = pygame.time.Clock()
FPS = 60
global Ecran_vr
class Animation:
    def __init__(self,taille,color) :
        self.y = random.randint(20,550)
        self.color = color
        self.snake_len = taille*30
        self.rect = pygame.Rect(600,self.y,self.snake_len,30)
    def move(self):
        self.rect.x -= 30
        if self.rect.x < self.snake_len*-1 :
            y = random.randint(20,550)
            self.rect.y = y
            self.rect.x = 600
    def afficher(self,ecran):
        pygame.draw.rect(ecran,self.color,self.rect)


class Player:
    def __init__(self,ecran_weight,ecran_height):
        self.ecran_weight = int(ecran_weight/30)
        self.ecran_height = int(ecran_height/30)
        self.long = 1
        self.color = (240, 136, 11)
        self.color2 = [(255,255,255),(34, 140, 81),(3, 229, 208),(240, 233, 11),(240, 136, 11),(212, 45, 45)]
        ls = []
        for i in range(self.ecran_height) :
            l = []
            for j in range(self.ecran_weight) :
                l.append(0)
            ls.append(l)
        mid = int(len(ls)/2)
        l = ls[mid]
        l[-1] = 1
        ls[mid] = l
        self.area = ls
        self.bille()
        print(self.area)
    
    def bille(self):
        self.color = random.choice(self.color2)
        place = True
        while place :
            nb = random.randint(0,len(self.area)*len(self.area[0]))
            y = 0
            tour = 0
            for i in range(self.ecran_height):
                x = 0
                for i in range(self.ecran_weight):
                    if tour == nb and self.area[y][x] == 0 :
                        self.area[y][x] = -1
                        place = False
                    tour += 1
                    x += 1
                y += 1

    def move(self, key):
        long_av = self.long
        y = 0
        r = 1
        deb = 0
        new = [0,0] #x,y du nouveau centre
        for i in range(self.ecran_height):
            x = 0
            for i in range(self.ecran_weight):
                el = self.area[y][x]
                if int(el) == 1 and deb == 0:
                    deb = 1
                    if str(key) == "key_left" :
                        if x > 0 : 
                            if self.area[y][x-1] == -1 :
                                self.long += 1
                                self.bille()
                                self.area[y][x-1] = 1
                                new = [x-1,y]
                            elif self.area[y][x-1] == 0 :
                                self.area[y][x-1] = 1
                                new = [x-1,y]
                            else :
                                r = 0
                        else :
                            r = 0
                            #print("stop")
                    if key == "key_right" :
                        if x+1 < self.ecran_weight : 
                            if self.area[y][x+1] == -1 :
                                self.long += 1
                                self.bille()
                                self.area[y][x+1] = 1
                                new = [x+1,y]
                            elif self.area[y][x+1] == 0 :
                                self.area[y][x+1] = 1
                                new = [x+1,y]
                            else :
                                r = 0
                        else :
                            r = 0
                            #print("stop")
                    if key == "key_up" :
                        if y > 0  : 
                            if self.area[y-1][x] == -1 :
                                self.long += 1
                                self.bille()
                                self.area[y-1][x] = 1
                                new = [x,y-1]
                            elif self.area[y-1][x] == 0 :
                                self.area[y-1][x] = 1
                                new = [x,y-1]
                            else :
                                r = 0
                        else :
                            r = 0
                            #print("stop")
                    if key == "key_down" :
                        if y+1 < self.ecran_height : 
                            if self.area[y+1][x] == -1 :
                                self.long += 1
                                self.bille()
                                self.area[y+1][x] = 1
                                new = [x,y+1]
                            elif self.area[y+1][x] == 0 :
                                self.area[y+1][x] = 1
                                new = [x,y+1]
                            else :
                                r = 0
                        else :
                            r = 0
                            #print("stop")
                x += 1
            y += 1
        y = 0
        for i in range(self.ecran_height) :
            x = 0
            for i in range(self.ecran_weight) :
                el = self.area[y][x]
                #print(el,new[0],x,new[1],y)
                if x == new[0] and y == new[1] :
                    #print('centre')
                    lm = 0
                else :
                    #print(el,int(self.area[y][x])+1,int(self.long)+1)
                    if int(el) !=0  and int(self.area[y][x])+1 < int(self.long)+1 and int(el) != -1:
                        self.area[y][x] = int(self.area[y][x]) + 1
                    elif int(self.area[y][x])+1 == int(self.long)+1 :
                        self.area[y][x] = 0 
                x +=1
            y += 1
        #print(self.area)
        #print(new)
        if r == 0 :
            ls = []
            for i in range(self.ecran_height) :
                l = []
                for j in range(self.ecran_weight) :
                    l.append(0)
                ls.append(l)
            mid = int(len(ls)/2)
            l = ls[mid]
            l[-1] = 1
            ls[mid] = l
            self.area = ls
            self.long = 1
            self.bille()
        return r,long_av

    def afficher(self,ecran):
        y = 0
        for i in range(self.ecran_height):
            x = 0
            for i in range(self.ecran_weight):
                el = self.area[int(y/30)][int(x/30)]
                if int(el) != 0 and int(el) != -1  :
                    r = pygame.Rect(x,y,30,30)
                    pygame.draw.rect(ecran,self.color,r)
                    #print(el,x,y)
                if int(el) == -1:
                    r = pygame.Rect(x+7,y+7,16,16)
                    pygame.draw.rect(ecran,(64, 181, 81),r)
                x += 30
            y += 30

        


#Color :
black = (0,0,0)
white = (255,255,255)
green = (64, 181, 81)
bleu = (3, 229, 208)
yellow = (240, 233, 11)
orange = (240, 136, 11)
red = (212, 45, 45)

ecran = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake")

animation1 = Animation(5,red)
snake = Player(600,600)

#Ecran Vr : cette varible sert a dire sur quel menu on se situe
Ecran_vr = 0 
game_play = True
tour = 0 #Util pour le "lag" du snake
last_key = "key_left"
last_move = "key_left"
Score = 0
last_score = 0
input_box = ""
print(best_score)
while game_play :
    if Ecran_vr == 0 :
        input_box = ""
        last_key = "key_left"
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                game_play = False
            if event.type == pygame.KEYDOWN:
                Ecran_vr = 1
        if tour == 15 :
            animation1.move()
            tour = 0
        animation1.afficher(ecran)
        myfont = pygame.font.SysFont("Impact", 33)
        texte = myfont.render(f"BEST :", 1, green)
        ecran.blit(texte, (266, 30))
        myfont = pygame.font.SysFont("Impact", 27)
        texte = myfont.render(f"{best_score} by {name_score} ", 1, green)
        ecran.blit(texte, (255, 70))
        myfont = pygame.font.SysFont("Impact", 50)
        texte = myfont.render("SNAKE", 1, yellow)
        ecran.blit(texte, (243, 230))
        myfont = pygame.font.SysFont("Impact", 15)
        texte = myfont.render("press one key", 1, orange)
        ecran.blit(texte, (260, 290))
        FPS = 60
        myfont = pygame.font.SysFont("Impact", 25)
        texte = myfont.render(str(Score), 1, white)
        ecran.blit(texte, (0, 0))
    elif Ecran_vr == 1 :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                game_play = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if last_move != "key_right":
                        last_key = "key_left"
                if event.key == pygame.K_RIGHT:
                    if last_move != "key_left":
                        last_key = "key_right"
                if event.key == pygame.K_UP:
                    if last_move != "key_down":
                        last_key = "key_up"
                if event.key == pygame.K_DOWN:
                    if last_move != "key_up":
                        last_key = "key_down"
        if tour == 15 :
            Ecran_vr, Score = snake.move(last_key)
            tour = 0
            last_move = last_key
        if last_score != Score :
            last_score = Score
            if last_score%3 == 0 :
                FPS += 15
        snake.afficher(ecran)
        myfont = pygame.font.SysFont("Impact", 25)
        texte = myfont.render(str(Score), 1, white)
        ecran.blit(texte, (0, 0))
        if Ecran_vr == 0 and Score > best_score-1 :
            Ecran_vr = 2
            best_score = Score
            #print(best_score,'bt')
    elif Ecran_vr == 2 :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_play = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_MINUS:
                    l = list(input_box)
                    #print(input_box)
                    del l[-1]
                    input_box = "".join(l)
                    #print(input_box)
                if event.unicode and event.key != pygame.K_MINUS: #pour -
                    input_box += event.unicode
        if len(input_box) > 3 :
            #print('ok')
            doc = open("best_score.txt","w")
            doc.write(f'{best_score}${input_box}')
            doc.close()
            name_score = input_box
            Ecran_vr = 0
            FPS = 60
            tour = 0
        myfont = pygame.font.SysFont("Impact", 27)
        texte = myfont.render(f"You have do the best score, enter 4l of your name :", 1, green)
        ecran.blit(texte, (25, 150))
        myfont = pygame.font.SysFont("Impact", 15)
        texte = myfont.render(f"To delete : -", 1,white)
        ecran.blit(texte, (25, 190))
        myfont = pygame.font.SysFont("Impact", 20)
        texte = myfont.render(str(input_box), 1, white)
        ecran.blit(texte, (25, 250))

    #fixer le nombre de fps
    clock.tick(FPS)

    pygame.display.flip()
    ecran.fill(black)
    tour += 1
    #print(FPS,end='')
pygame.quit()
quit()
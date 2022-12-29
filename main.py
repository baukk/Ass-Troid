import pygame
import sys
import random
from random import uniform
from threading import Timer
import time
#game init







pygame.init()


 
def meteor(meteor_list,speed=300):
    for meteortuple in meteor_list:
        # direction=pygame.math.Vector2(1 ,2)
        direction=meteortuple[2]
        meteortuple[1].center+=(direction)*speed*dt
        if (meteortuple[1].y>WINDOW_HEIGHT):
            meteor_list.remove(meteortuple)

font=pygame.font.Font('graphics/subatomic.ttf',50)

def display_score():
    score=f"Score:{pygame.time.get_ticks()//1000+(sscore)}"
    print(sscore)
    text_surf=font.render(score, True ,(255,255,255))
    text_rect=text_surf.get_rect(midbottom=(WINDOW_WIDTH*0.13,WINDOW_HEIGHT*0.12))
    display_surface.blit(text_surf,text_rect) 
    pygame.draw.rect(display_surface,(255,255,255),text_rect.inflate(30,30),width=8,border_radius=5)

def shootlaser(laser_list,speed=300):
    for rect in laser_list:
        rect.y-=(speed)*dt
        if(rect.y<0):
            laser_list.remove(rect)

def laser_timer(can_shoot,duration=500):
    if not can_shoot:
        current_time=pygame.time.get_ticks()-shoot_time
        if current_time>duration:
            can_shoot=True
    return can_shoot


WINDOW_WIDTH,WINDOW_HEIGHT=1920,1080
flags=pygame.RESIZABLE
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),flags)
pygame.display.set_caption("Asteroid by @baukk")
clock=pygame.time.Clock()

#load ship image and its initial position using rect
ship_surf=pygame.image.load('graphics/ship.png').convert_alpha()
ship_rect=ship_surf.get_rect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

#load bg
background_surf=pygame.image.load('graphics/background.png').convert_alpha()
background_surf = pygame.transform.scale(background_surf,(1920,1080))


#load a font and its pos
font=pygame.font.Font('graphics/subatomic.ttf',50)
text_surf=font.render('SPACE', True ,(255,255,255))
text_rect=text_surf.get_rect(midbottom=(WINDOW_WIDTH/2,WINDOW_HEIGHT-80))

#load laser
laser_surf=pygame.image.load('graphics/laser.png').convert_alpha()
laser_list=[]

gameover=pygame.image.load("graphics/gameover.jpeg").convert_alpha()
gameover=pygame.transform.scale(gameover,(1920,1080))
#load meteor
img1=pygame.image.load('graphics/meteor.png').convert_alpha()
img1 = pygame.transform.scale(img1,(100,100))
img2=pygame.image.load('graphics/choti.png').convert_alpha()
img2 = pygame.transform.scale(img2,(100,100))
img3=pygame.image.load('graphics/sibbi.png').convert_alpha()
img3 = pygame.transform.scale(img3,(100,100))
img4=pygame.image.load('graphics/sachu.png').convert_alpha()
img4 = pygame.transform.scale(img4,(100,100))
img5=pygame.image.load('graphics/ankita.png').convert_alpha()
img5 = pygame.transform.scale(img5,(100,100))

img6=pygame.image.load('graphics/sakshi.png').convert_alpha()
img6 = pygame.transform.scale(img6,(200,200))

metero_surface_list=[img1,img2,img3,img4,img5,img6]
meteor_list=[]


can_shoot=True
shoot_time=None
meteor_timer=pygame.event.custom_type()
pygame.time.set_timer(meteor_timer,500)


laser_sound=pygame.mixer.Sound("sounds/laser.ogg")
explosion_sound=pygame.mixer.Sound("sounds/explosion.wav")
music=pygame.mixer.Sound("sounds/music.wav")
music.play(loops=-1)
gameover_sound=pygame.mixer.Sound("sounds/gameover.wav")


while True: #run forever -> keeps game running

    # event loop

   

    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and can_shoot==True:

            laser_rect=laser_surf.get_rect(midbottom=ship_rect.midtop)
            laser_sound.play()
            laser_list.append(laser_rect)
            display_surface.blit(laser_surf,laser_rect)
            can_shoot=False
            shoot_time=pygame.time.get_ticks()
        if event.type==meteor_timer:
            direction=pygame.math.Vector2(uniform(-0.5,1.5),1)
            newsurf=random.choice(metero_surface_list)
            meteor_rect=newsurf.get_rect(center=(random.randint(50,WINDOW_WIDTH-50),random.randint(-10,0)))
            meteor_list.append((newsurf,meteor_rect,direction))
            # for i in meteor_list:
            #     print (i[1])
            # print("new")
            # print(meteor_list)
    #framerate limit
    dt=clock.tick(120)/1000
    


    # print(mm)
    # print(ship_rect)

    sscore=0
    print(laser_list)
    for i in laser_list:
        for j in meteor_list:
            if i.colliderect(j[1]):
                print("laser")
                meteor_list.remove(j)
                laser_list.remove(i)
                explosion_sound.play()
    # mouse movement         
    ship_rect.center=pygame.mouse.get_pos()
        
   
    #2 update
    shootlaser(laser_list)
    can_shoot=laser_timer(can_shoot,500)
    meteor(meteor_list,200)
   
#    blits
    display_surface.blit(background_surf,(0,0))
    
    text_surf=font.render("Ass-Troid", True ,(255,255,255))
    text_rect=text_surf.get_rect(midbottom=(WINDOW_WIDTH*0.5,WINDOW_HEIGHT*0.8))
    display_surface.blit(text_surf,text_rect)
    
    display_score()
    
    display_surface.blit(ship_surf,ship_rect)

    for laserrect in laser_list:
        display_surface.blit(laser_surf,laserrect)

    for meteorrect in meteor_list:
        display_surface.blit(meteorrect[0],meteorrect[1])
    for i in meteor_list:

        # print(mm)
        if ship_rect.colliderect(i[1])>0:
            print("collide")
            music.stop()
            gameover_sound.play()
            display_surface.blit(gameover,(0,0))
            # pygame.time.delay(2000)
            # sys.exit()

           
            
            
            
    # 3show frame/ updaye display
    pygame.display.update()

    
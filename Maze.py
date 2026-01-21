import pygame
import time
import threading
pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False
clock = pygame.time.Clock()
x = 67
y = 67
x2 = 650
y2 = 50
oldx = x
oldy = y
oldx2 = x2
oldy2 = y2
speed = 2
speed2 = 1.80
starttime1 = time.time()
duration1 = 0
duration2 = 0
starttime2 = time.time()


p1 = "player1-removebg-preview.png"
p2 = "player_2-removebg-preview.png"
surf1 = pygame.image.load(p1).convert_alpha()
surf1small = pygame.transform.scale(surf1, (40, 40))
surf2 = pygame.image.load(p2).convert_alpha()
surf2small = pygame.transform.scale(surf2, (40, 40))


Partwidth = 40
Partheight = 300

Partx = 550
Party = 40

def resize():
    global Partwidth, Partheight
    while True:
        for i in range(100):
            Partwidth+=1
            time.sleep(0.02)
        time.sleep(1)
        for i in range(100):
            Partwidth-=1
            time.sleep(0.02)

def move():
    global Partx, Party
    while True:
        for i in range(100):
            Partx+=1
            time.sleep(0.02)
        time.sleep(1)
        for i in range(100):
            Partx-=1
            time.sleep(0.02)


resize_thread = threading.Thread(target=resize)
resize_thread.daemon = True
resize_thread.start()

move_thread = threading.Thread(target=move)
move_thread.daemon = True
move_thread.start()




while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((3, 200, 67))

    finish = pygame.draw.rect(screen, (90, 130, 255), (700, 700 , 40, 40))
    player1= surf1small.get_rect(topleft=(x , y))
    screen.blit(surf1small, player1)
    player2 = surf2small.get_rect(topleft=(x2, y2))
    screen.blit(surf2small, player2)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=speed
    if keys[pygame.K_RIGHT]:
        x+=speed
    if keys[pygame.K_UP]:
        y-=speed
    if keys[pygame.K_DOWN]:
        y+=speed

    keys2 = pygame.key.get_pressed()
    if keys2[pygame.K_a]:
        x2-=speed2
    if keys2[pygame.K_d]:
        x2+=speed2
    if keys2[pygame.K_w]:
        y2-=speed2
    if keys2[pygame.K_s]:
        y2+=speed2



    wlUp = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 800, 40))  # top wall
    wlDown = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 760, 800, 40)) # down wall
    wlLeft = pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, 20, 40 , 800)) # left wall
    wlRight = pygame.draw.rect(screen, (255,0,0), pygame.Rect(760, 20, 40 , 800)) #right wall
    wlIns1 = pygame.draw.rect(screen, (255,0,0), pygame.Rect(320, 500, 40 , 200)) # wall inside n.1 (kath)
    wlIns2 = pygame.draw.rect(screen, (225,0,0), pygame.Rect(537, 260, Partwidth  , Partheight )) # wall inside n.2 (kath)
    wlIns3 = pygame.draw.rect(screen, (255,0,0), pygame.Rect(Partwidth , Partheight, 40 , 400)) # wall inside n.3 (kath)
    wlIns4 = pygame.draw.rect(screen, (255,0,0), pygame.Rect(250,140  , 30 , 200)) # wall inside n.4 (kath)
    wlIns5 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(430, 325, 30, 200))  # wall inside n.5 (kath)
    wlIns6 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(667, 100, 30, 400))  # wall inside n.6 (kath)
    wlIns7 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(667,500 , 30, 40))  # wall inside n.7 (oriz)
    wlIns8 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(377, 230 , 200 , 30))  # wall inside n.8 (oriz)
    wlIns9 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(537, 97 , 300 , 30))  # wall inside n.9 (oriz)
    wlIns10 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(130, 140 , 240 , 35))  # wall inside n.10 (oriz)
    wlIns11 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(250, 325 , 180 , 25))  # wall inside n.11 (oriz)
    wlIns12 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 670, Partx, Party))  # wall ins n.12 (oriz)

    Font = pygame.font.SysFont("consolas", 35, True , True)
    Gametitle = Font.render("sigma maze", True , (255, 255, 255))
    screen.blit(Gametitle, (300, 0))
    timer1 = Font.render("Timer1:"+ str(duration1), True , (0, 0, 0))
    screen.blit(timer1, (40, 0))
    timer2 = Font.render("Timer2:"+str(duration2), True, (0, 0, 0))
    screen.blit(timer2, (550, 0))





    walls = [wlIns1, wlIns2, wlIns3, wlIns4, wlIns5, wlIns6, wlIns7, wlIns8, wlIns9, wlIns10, wlIns11, wlIns12]

    for i in walls:
        if player1.colliderect(i):
            x= oldx
            y = oldy

    for i2 in walls:
        if player2.colliderect(i2):
            x2= oldx2
            y2 = oldy2

    if player1.colliderect(wlUp):
        y+=5
    if player1.colliderect(wlDown):
        y-=5
    if player1.colliderect(wlLeft):
        x+=5
    if player1.colliderect(wlRight):
        x-=5

    if player2.colliderect(wlUp):
        y2+=5
    if player2.colliderect(wlDown):
        y2-=5
    if player2.colliderect(wlLeft):
        x2+=5
    if player2.colliderect(wlRight):
        x2-=5

    if player1.colliderect(finish):
        x = oldx
        y = oldy
        endtime1 = time.time()
        duration1 = round(endtime1 - starttime1, 2)
        starttime1 = time.time()
    if player2.colliderect(finish):
        x2 = oldx2
        y2 = oldy2
        endtime2 = time.time()
        duration2 = round(endtime2 - starttime2, 2)
        starttime2 = time.time()








    pygame.display.flip()



pygame.quit()


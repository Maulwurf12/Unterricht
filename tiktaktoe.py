#tik tac toe
"""
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode([1200,595])
hintergrund = pygame.image.load("D:/Maulwurf/python/tik tak toe/Grafiken/hintergrund.png")
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame test")

def zeichnen():
    screen.blit(hintergrund,(0,0))
    pygame.draw.rect(screen, (0,0,255), (x,y,breite,höhe))
    pygame.display.update()

x = 500
y = 500
geschw = 9
breite = 100
höhe = 80

linkeWand = pygame.draw.rect(screen, (0,0,0), (-2,0,2,600),0)
rechteWand = pygame.draw.rect(screen, (0,0,0), (1201,0,2,600),0)
sprungvar = -16
go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    SpielerRechteck = pygame.Rect(x,y,40,80)
    gedrückt = pygame.key.get_pressed()
    if gedrückt [pygame.K_UP] and sprungvar == -16:
        sprungvar = 15
    if gedrückt [pygame.K_RIGHT] and not SpielerRechteck.colliderect(rechteWand):
        x += geschw
    if gedrückt [pygame.K_LEFT] and not SpielerRechteck.colliderect(linkeWand):
        x -= geschw
    if sprungvar >= -15:
        n = 1
        if sprungvar < 0:
            n = -1
        y -=(sprungvar**2)*0.17*n
        sprungvar -= 1

    zeichnen()
    clock.tick(60)
"""
import time
from typing import Tuple
import pygame
import sys

from pygame.constants import MOUSEBUTTONDOWN

pygame.init()
Bildschirm = pygame.display.set_mode([400, 400])
tictactoe_bild = pygame.image.load("D:/Maulwurf/python/tik tak toe/Grafiken/tictactoe.png")
clock = pygame.time.Clock()
pygame.display.set_caption ("tic tac toe")
def Kreis_setzen1():
    pygame.draw.ellipse(Bildschirm, (0,0,0), [1,1,130,130], 1)
def Kreis_setzen2():
    pygame.draw.ellipse(Bildschirm, (0,0,0), [134,1,130,130], 1)
def Kreis_setzen3():
    pygame.draw.ellipse(Bildschirm, (0,0,0), [267,1,130,130], 1)
def Kreis_setzen4():
    pygame.draw.ellipse(Bildschirm, (0,0,0), [1,134,130,130], 1)
def Kreis_setzen5():
    pygame.draw.ellipse(Bildschirm, (0,0,0), [134,134,130,130], 1)
def Kreis_setzen6():
    pygame.draw.ellipse(Bildschirm, (0,0,0), [267,134,130,130], 1)
def Kreis_setzen7():
    pygame.draw.ellipse(Bildschirm, (0,0,0), [1,267,130,130], 1)
def Kreis_setzen8():
    pygame.draw.ellipse(Bildschirm, (0,0,0), [134,267,130,130], 1)
def Kreis_setzen9():
    pygame.draw.ellipse(Bildschirm, (0,0,0), [267,267,130,130], 1)
def Kreuz_setzen1():
    pygame.draw.aaline(Bildschirm, (0,0,0), [15, 15], [110, 120])
    pygame.draw.aaline(Bildschirm, (0,0,0), [12, 119], [119, 12])
def Kreuz_setzen2():
    pygame.draw.aaline(Bildschirm, (0,0,0), [149, 15], [243, 120])
    pygame.draw.aaline(Bildschirm, (0,0,0), [146,119], [251, 12])
def Kreuz_setzen3():
    pygame.draw.aaline(Bildschirm, (0,0,0), [283, 15], [377, 120])
    pygame.draw.aaline(Bildschirm, (0,0,0), [280,119], [385, 12])
def Kreuz_setzen4():
    pygame.draw.aaline(Bildschirm, (0,0,0), [15, 149], [110, 254])
    pygame.draw.aaline(Bildschirm, (0,0,0), [12, 253], [119, 146])
def Kreuz_setzen5():
    pygame.draw.aaline(Bildschirm, (0,0,0), [149, 149], [243, 254])
    pygame.draw.aaline(Bildschirm, (0,0,0), [146,253], [251, 146])
def Kreuz_setzen6():
    pygame.draw.aaline(Bildschirm, (0,0,0), [283, 149], [377, 254])
    pygame.draw.aaline(Bildschirm, (0,0,0), [280,253], [385, 146])
def Kreuz_setzen7():
    pygame.draw.aaline(Bildschirm, (0,0,0), [15, 283], [110, 388])
    pygame.draw.aaline(Bildschirm, (0,0,0), [12, 387], [119, 280])
def Kreuz_setzen8():
    pygame.draw.aaline(Bildschirm, (0,0,0), [149, 283], [243, 388])
    pygame.draw.aaline(Bildschirm, (0,0,0), [146,387], [251, 280])
def Kreuz_setzen9():
    pygame.draw.aaline(Bildschirm, (0,0,0), [283, 283], [377, 388])
    pygame.draw.aaline(Bildschirm, (0,0,0), [280,387], [385, 280])
global Unentschieden
global Spiel_go
global siegesbild
global var1
global var2
global var3
global var4
global var5
global var6
global var7
global var8
global var9
global var1_1
global var2_2
global var3_3
global var4_4
global var5_5
global var6_6
global var7_7
global var8_8
global var9_9
x0 = 0
x1 = 134
x2 = 267
x3 = 400
y0 = 0
y1 = 134
y2 = 267
y3 = 400
Unentschieden = True
var1_1 = False
var2_2 = False
var3_3 = False
var4_4 = False
var5_5 = False
var6_6 = False
var7_7 = False
var8_8 = False
var9_9 = False
var1 = False
var2 = False
var3 = False
var4 = False
var5 = False
var6 = False
var7 = False
var8 = False
var9 = False
Game_start = True

siegesbild = pygame.image.load("D:/Maulwurf/python/tik tak toe/Grafiken/siegesbildschirm.jpg")

def win_X():
    global Unentschieden
    global Spiel_go
    global siegesbild
    global var1
    global var2
    global var3
    global var4
    global var5
    global var6
    global var7
    global var8
    global var9
    global var1_1
    global var2_2
    global var3_3
    global var4_4
    global var5_5
    global var6_6
    global var7_7
    global var8_8
    global var9_9
    Bildschirm.blit(siegesbild,(0,0))
    Kreuz_setzen5()
    Unentschieden = False
    var1_1 = False
    var2_2 = False
    var3_3 = False
    var4_4 = False
    var5_5 = False
    var6_6 = False
    var7_7 = False
    var8_8 = False
    var9_9 = False
    var1 = False
    var2 = False
    var3 = False
    var4 = False
    var5 = False
    var6 = False
    var7 = False
    var8 = False
    var9 = False
    Spiel_go = False
    

        
def win_O():
    global Unentschieden
    global Spiel_go
    global siegesbild
    global var1
    global var2
    global var3
    global var4
    global var5
    global var6
    global var7
    global var8
    global var9
    global var1_1
    global var2_2
    global var3_3
    global var4_4
    global var5_5
    global var6_6
    global var7_7
    global var8_8
    global var9_9
    Bildschirm.blit(siegesbild,(0,0))
    Kreis_setzen5()
    Unentschieden = True
    var1 = False
    var2 = False
    var3 = False
    var4 = False
    var5 = False
    var6 = False
    var7 = False
    var8 = False
    var9 = False
    var1_1 = False
    var2_2 = False
    var3_3 = False
    var4_4 = False
    var5_5 = False
    var6_6 = False
    var7_7 = False
    var8_8 = False
    var9_9 = False
    Spiel_go = False




EZ = True


Spiel_go=True


while Spiel_go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == MOUSEBUTTONDOWN and EZ:
            position = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            print(type(mouse_click), mouse_click)
            if position[0] <= x1 and position[1] <= y1:
                print(position)
                if not var1 and not var1_1:
                    var1 = True
                    EZ=False
                    Game_start = False
            if x1 <= position[0] <= x2 and position[1] <= y1:
                print(position)
                if not var2 and not var2_2: 
                    var2 = True
                    EZ=False
                    Game_start = False
            if position[0] >= x2 and position[1] <= y1:
                print(position)
                if not var3 and not var3_3: 
                    var3 = True
                    EZ=False
                    Game_start = False
            if position[0] <= x1 and y1 <= position[1] <= y2:
                print(position)
                if not var4 and not var4_4: 
                    var4 = True
                    EZ=False
                    Game_start = False
            if x1 <= position[0] <= x2 and y1 <= position[1] <= y2:
                print(position)
                if not var5 and not var5_5: 
                    var5 = True
                    EZ=False
                    Game_start = False
            if position[0] >= x2 and y1 <= position[1] <= y2:
                print(position)
                if not var6 and not var6_6: 
                    var6 = True
                    EZ=False
                    Game_start = False
            if position[0] <= x1 and position[1] >= y2:
                print(position)
                if not var7 and not var7_7: 
                    var7 = True
                    EZ=False
                    Game_start = False
            if x1 <= position[0] <= x2 and position[1] >= y2:
                print(position)
                if not var8 and not var8_8: 
                    var8 = True
                    EZ=False
                    Game_start = False
            if position[0] >= x2 and position[1] >= y2:
                print(position)
                if not var9 and not var9_9: 
                    var9 = True
                    EZ=False
                    Game_start = False
        if event.type == MOUSEBUTTONDOWN and not EZ:
            position = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            print(type(mouse_click), mouse_click)
            if position[0] <= x1 and position[1] <= y1:
                print(position)
                if not var1_1 and not var1: 
                    var1_1 = True
                    EZ = True
            if x1 <= position[0] <= x2 and position[1] <= y1:
                print(position)
                if not var2_2 and not var2: 
                    var2_2 = True
                    EZ = True
            if position[0] >= x2 and position[1] <= y1:
                print(position)
                if not var3_3 and not var3: 
                    var3_3 = True
                    EZ = True
            if position[0] <= x1 and y1 <= position[1] <= y2:
                print(position)
                if not var4_4 and not var4: 
                    var4_4 = True
                    EZ = True
            if x1 <= position[0] <= x2 and y1 <= position[1] <= y2:
                print(position)
                if not var5_5 and not var5: 
                    var5_5 = True
                    EZ = True
            if position[0] >= x2 and y1 <= position[1] <= y2:
                print(position)
                if not var6_6 and not var6: 
                    var6_6 = True
                    EZ = True
            if position[0] <= x1 and position[1] >= y2:
                print(position)
                if not var7_7 and not var7: 
                    var7_7 = True
                    EZ = True
            if x1 <= position[0] <= x2 and position[1] >= y2:
                print(position)
                if not var8_8 and not var8: 
                    var8_8 = True
                    EZ = True
            if position[0] >= x2 and position[1] >= y2:
                print(position)
                if not var9_9 and not var9: 
                    var9_9 = True
                    EZ = True

    #AllesZeichnen
    Bildschirm.blit(tictactoe_bild,(0,0))
    if var1 and var2 and var3:
        print("Das Spiel ist vorbei")   
        win_O() 
    if var1 and var4 and var7:
        print("Das Spiel ist vorbei")
        win_O()  
    if var1 and var5 and var9:
        print("Das Spiel ist vorbei")
        win_O()  
    if var4 and var5 and var6:
        print("Das Spiel ist vorbei")
        win_O()  
    if var7 and var8 and var9:
        print("Das Spiel ist vorbei")
        win_O()  
    if var2 and var5 and var8:
        print("Das Spiel ist vorbei")
        win_O()  
    if var3 and var6 and var9:
        print("Das Spiel ist vorbei")
        win_O()  
    if var3 and var5 and var7:
        print("Das Spiel ist vorbei")
        win_O()  
            

    if var1_1 and var2_2 and var3_3:
        print("Das Spiel ist vorbei")
        win_X()
    if var1_1 and var4_4 and var7_7:
        print("Das Spiel ist vorbei")
        win_X()
    if var1_1 and var5_5 and var9_9:
        print("Das Spiel ist vorbei")
        win_X()
    if var4_4 and var5_5 and var6_6:
        print("Das Spiel ist vorbei")
        win_X()
    if var7_7 and var8_8 and var9_9:
        print("Das Spiel ist vorbei")
        win_X()
    if var2_2 and var5_5 and var8_8:
        print("Das Spiel ist vorbei")
        win_X()
    if var3_3 and var6_6 and var9_9:
        print("Das Spiel ist vorbei")
        win_X()
    if var3_3 and var5_5 and var7_7:
        print("Das Spiel ist vorbei")
        win_X()

    if Unentschieden and not Game_start:
        Bildschirm.blit(siegesbild,(0,0))
        Kreuz_setzen5()
        Kreis_setzen5()
        Unentschieden = False
        var1_1 = False
        var2_2 = False
        var3_3 = False
        var4_4 = False
        var5_5 = False
        var6_6 = False
        var7_7 = False
        var8_8 = False
        var9_9 = False
        var1 = False
        var2 = False
        var3 = False
        var4 = False
        var5 = False
        var6 = False
        var7 = False
        var8 = False
        var9 = False
        Spiel_go = False

    if var1:
        Kreis_setzen1()
    if var2:
        Kreis_setzen2()
    if var3:
        Kreis_setzen3()
    if var4:
        Kreis_setzen4()
    if var5:
        Kreis_setzen5()
    if var6:
        Kreis_setzen6()
    if var7:
        Kreis_setzen7()
    if var8:
        Kreis_setzen8()
    if var9:
        Kreis_setzen9()

    if var1_1:
        Kreuz_setzen1()
    if var2_2:
        Kreuz_setzen2()
    if var3_3:
        Kreuz_setzen3()
    if var4_4:
        Kreuz_setzen4()
    if var5_5:
        Kreuz_setzen5()
    if var6_6:
        Kreuz_setzen6()
    if var7_7:
        Kreuz_setzen7()
    if var8_8:
        Kreuz_setzen8()
    if var9_9:
        Kreuz_setzen9()  
    pygame.display.update()
    clock.tick(60)
time.sleep(5)
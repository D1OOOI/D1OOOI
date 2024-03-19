import sys
import pygame
import random
import keyboard

w=900
h=800
FPS=60
t=0
td=0
x1=4
y1=0
pause=0
score=0
game=1
delay=False
space1=False
run=True

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((w, h))
#keys = pygame.key.get_pressed()

C=list([[255,0,0],[255,63,0],[255,183,0],[0,170,0],[0,69,255],[0,8,255],[255,18,63],[42,42,42]])
figures=list([
[ [[8,8,8,8,8],
[8,8,0,8,8],
[8,8,0,8,8],
[8,0,0,8,8],
[8,8,8,8,8]],

[[8,8,8,8,8],
[8,0,8,8,8],
[8,0,0,0,8],
[8,8,8,8,8],
[8,8,8,8,8]],

[[8,8,8,8,8],
[8,8,0,0,8],
[8,8,0,8,8],
[8,8,0,8,8],
[8,8,8,8,8]],

[[8,8,8,8,8],
[8,8,8,8,8],
[8,0,0,0,8],
[8,8,8,0,8],
[8,8,8,8,8]],

    [[8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8]] ],

[ [[8,8,8,8,8],
[8,8,1,8,8],
[8,8,1,8,8],
[8,8,1,1,8],
[8,8,8,8,8]],

[[8,8,8,8,8],
 [8,8,8,8,8],
[8,1,1,1,8],
[8,1,8,8,8],
[8,8,8,8,8]],

[[8,8,8,8,8],
[8,1,1,8,8],
[8,8,1,8,8],
[8,8,1,8,8],
[8,8,8,8,8]],

[[8,8,8,8,8],
[8,8,8,1,8],
[8,1,1,1,8],
[8,8,8,8,8],
[8,8,8,8,8]],

    [[8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8]] ],

[ [[8,8,8,8,8],
[8,8,8,8,8],
[8,2,2,2,8],
[8,8,2,8,8],
[8,8,8,8,8]],

[[8,8,8,8,8],
[8,8,2,8,8],
[8,2,2,8,8],
[8,8,2,8,8],
[8,8,8,8,8]],

[[8,8,8,8,8],
[8,8,2,8,8],
[8,2,2,2,8],
[8,8,8,8,8],
[8,8,8,8,8]],

[[8,8,8,8,8],
[8,8,2,8,8],
[8,8,2,2,8],
[8,8,2,8,8],
[8,8,8,8,8]],

    [[8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8]] ],

[ [[8,8,8,8,8],
[8,8,8,8,8],
[8,8,3,3,8],
[8,3,3,8,8],
[8,8,8,8,8]],

[[8,8,8,8,8],
[8,8,3,8,8],
[8,8,3,3,8],
[8,8,8,3,8],
[8,8,8,8,8]],

    [[8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8]] ],

[ [[8,8,8,8,8],
[8,8,8,8,8],
[8,4,4,8,8],
[8,8,4,4,8],
[8,8,8,8,8]],

[[8,8,8,8,8],
[8,8,4,8,8],
[8,4,4,8,8],
[8,4,8,8,8],
[8,8,8,8,8]],

    [[8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8]] ],

[ [[8,8,8,8,8],
[8,8,8,8,8],
[5,5,5,5,8],
[8,8,8,8,8],
[8,8,8,8,8]],

[[8,8,8,8,8],
[8,8,5,8,8],
[8,8,5,8,8],
[8,8,5,8,8],
[8,8,5,8,8]],

    [[8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8]] ],

[ [[8,8,8,8,8],
[8,8,8,8,8],
[8,8,6,6,8],
[8,8,6,6,8],
[8,8,8,8,8]],

    [[8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8],
    [8,8,8,8,8]]],])

# NF=list([ 7,1 ])
NF=[7,0]
T=list([ [-1 ,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, -1],

    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
    [-1 ,7,7,7,7,7,7,7,7,7,7, -1],
 
    [-1 ,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, -1],
    [-1 ,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, -1]
])

# Functions

def isPointInRectangle(x, y, rectX, rectY, rectW, rectH):
    return x > rectX and y > rectY and x < rectX+rectW and y < rectY+rectH ;

def res(row):
    T[row][1]=7
    T[row][2]=7
    T[row][3]=7
    T[row][4]=7
    T[row][5]=7
    T[row][6]=7
    T[row][7]=7
    T[row][8]=7
    T[row][9]=7
    T[row][10]=7;

def fig(nf,rot,row,y1,x1): #- nf=now figure, rot=rotation
    if figures[nf][rot][row][0]==nf : T[y1+row][x1+0]=figures[nf][rot][row][0]
    if figures[nf][rot][row][1]==nf : T[y1+row][x1+1]=figures[nf][rot][row][1]
    if figures[nf][rot][row][2]==nf : T[y1+row][x1+2]=figures[nf][rot][row][2]
    if figures[nf][rot][row][3]==nf : T[y1+row][x1+3]=figures[nf][rot][row][3]
    if figures[nf][rot][row][4]==nf : T[y1+row][x1+4]=figures[nf][rot][row][4];

def fig2(nf,rot,row,y1,x1):
    if figures[nf][rot][row][0]==nf : T[y1+row][x1+0]=7 ;
    if figures[nf][rot][row][1]==nf : T[y1+row][x1+1]=7 ;
    if figures[nf][rot][row][2]==nf : T[y1+row][x1+2]=7 ;
    if figures[nf][rot][row][3]==nf : T[y1+row][x1+3]=7 ;
    if figures[nf][rot][row][4]==nf : T[y1+row][x1+4]=7 ;

def fig3(nf,rot,row,col,y1,x1):
    if figures[nf][rot][row][col] > -1 and figures[nf][rot][row][col] < 7:
        if T[y1 + row][x1 + (col - 0)] == 7: return True;
        if T[y1 + row][x1 + (col - 0)] == -1: return False;
        if T[y1 + row][x1 + (col - 0)] == None: return False;
        if T[y1 + row][x1 + (col - 0)] < 7 and T[y1 + row][x1 + (col - 0)] > -1: return False;
    else: return True

def new_figure():
    NF[1]=0
    NF[0]=random.randint(0,6);

def del_figure(x1, y1, nf, rot):
    fig2(nf, rot, 0, y1, x1)
    fig2(nf, rot, 1, y1, x1)
    fig2(nf, rot, 2, y1, x1)
    fig2(nf, rot, 3, y1, x1)
    fig2(nf, rot, 4, y1, x1);

def now_figure(x1, y1, nf, rot):
    fig(nf, rot, 0, y1, x1)
    fig(nf, rot, 1, y1, x1)
    fig(nf, rot, 2, y1, x1)
    fig(nf, rot, 3, y1, x1)
    fig(nf, rot, 4, y1, x1);

def restart():
    del_figure(x1,y1,NF[0],NF[1])
    res(1), res(2), res(3), res(4), res(5), res(6), res(7), res(8), res(9), res(10), res(11), res(12), res(13), res(14), res(15), res(16), res(17), res(18)
    new_figure()
    now_figure(x1,y1,NF[0],NF[1])

def down(row,row1):
    if row<row1 :
        T[row + 1][1] = T[row][1]
        T[row + 1][2] = T[row][2]
        T[row + 1][3] = T[row][3]
        T[row + 1][4] = T[row][4]
        T[row + 1][5] = T[row][5]
        T[row + 1][6] = T[row][6]
        T[row + 1][7] = T[row][7]
        T[row + 1][8] = T[row][8]
        T[row + 1][9] = T[row][9]
        T[row + 1][10] = T[row][10]
        T[row][1] = 7
        T[row][2] = 7
        T[row][3] = 7
        T[row][4] = 7
        T[row][5] = 7
        T[row][6] = 7
        T[row][7] = 7
        T[row][8] = 7
        T[row][9] = 7
        T[row][10] = 7

def checkrow(row):
    global score
    if T[row][1]!=7\
        and T[row][2]!=7\
        and T[row][3]!=7\
        and T[row][4]!=7\
        and T[row][5]!=7\
        and T[row][6]!=7\
        and T[row][7]!=7\
        and T[row][8]!=7\
        and T[row][9]!=7\
        and T[row][10]!=7\
        :
        score=score+1
        T[row][2] = 8
        T[row][3] = 8
        T[row][4] = 8
        T[row][5] = 8
        T[row][6] = 8
        T[row][7] = 8
        T[row][8] = 8
        T[row][9] = 8
        T[row][10] = 8
        T[row][11] = 8
        down(18, row), down(17, row), down(16, row), down(15, row), down(14, row), down(13, row), down(12, row), down(11, row), down(10, row), down(9, row), down(8, row), down(7, row), down(6, row), down(5, row), down(4, row), down(3, row), down(2, row)

def checkT():
    checkrow(1), checkrow(2), checkrow(3), checkrow(4), checkrow(5), checkrow(6), checkrow(7), checkrow(8), checkrow(9),
    checkrow(10), checkrow(11), checkrow(12), checkrow(13), checkrow(14), checkrow(15), checkrow(16), checkrow(17), checkrow(18)

def checkpos(x1,y1,nf,rot):
    if  fig3(nf,rot,0,0,y1,x1) and\
        fig3(nf,rot,0,1,y1,x1) and\
        fig3(nf,rot,0,2,y1,x1) and\
        fig3(nf,rot,0,3,y1,x1) and\
        fig3(nf,rot,0,4,y1,x1) and\
        fig3(nf,rot,1,0,y1,x1) and\
        fig3(nf,rot,1,1,y1,x1) and\
        fig3(nf,rot,1,2,y1,x1) and\
        fig3(nf,rot,1,3,y1,x1) and\
        fig3(nf,rot,1,4,y1,x1) and\
        fig3(nf,rot,2,0,y1,x1) and\
        fig3(nf,rot,2,1,y1,x1) and\
        fig3(nf,rot,2,2,y1,x1) and\
        fig3(nf,rot,2,3,y1,x1) and\
        fig3(nf,rot,2,4,y1,x1) and\
        fig3(nf,rot,3,0,y1,x1) and\
        fig3(nf,rot,3,1,y1,x1) and\
        fig3(nf,rot,3,2,y1,x1) and\
        fig3(nf,rot,3,3,y1,x1) and\
        fig3(nf,rot,3,4,y1,x1) and\
        fig3(nf,rot,4,0,y1,x1) and\
        fig3(nf,rot,4,1,y1,x1) and\
        fig3(nf,rot,4,2,y1,x1) and\
        fig3(nf,rot,4,3,y1,x1) and\
        fig3(nf,rot,4,4,y1,x1)\
    :return True
    else: return False ;

def TR(r):
    pygame.draw.rect(screen, (C[T[r][1]][0],C[T[r][1]][1],C[T[r][1]][2]), (0*w/(w/h)/25+w/2-5*w/(w/h)/25, r*(h/25), w/(w/h)/25, h/25))
    pygame.draw.rect(screen, (C[T[r][2]][0],C[T[r][2]][1],C[T[r][2]][2]), (1*w/(w/h)/25+w/2-5*w/(w/h)/25, r*(h/25), w/(w/h)/25, h/25))
    pygame.draw.rect(screen, (C[T[r][3]][0],C[T[r][3]][1],C[T[r][3]][2]), (2*w/(w/h)/25+w/2-5*w/(w/h)/25, r*(h/25), w/(w/h)/25, h/25))
    pygame.draw.rect(screen, (C[T[r][4]][0],C[T[r][4]][1],C[T[r][4]][2]), (3*w/(w/h)/25+w/2-5*w/(w/h)/25, r*(h/25), w/(w/h)/25, h/25))
    pygame.draw.rect(screen, (C[T[r][5]][0],C[T[r][5]][1],C[T[r][5]][2]), (4*w/(w/h)/25+w/2-5*w/(w/h)/25, r*(h/25), w/(w/h)/25, h/25))
    pygame.draw.rect(screen, (C[T[r][6]][0],C[T[r][6]][1],C[T[r][6]][2]), (5*w/(w/h)/25+w/2-5*w/(w/h)/25, r*(h/25), w/(w/h)/25, h/25))
    pygame.draw.rect(screen, (C[T[r][7]][0],C[T[r][7]][1],C[T[r][7]][2]), (6*w/(w/h)/25+w/2-5*w/(w/h)/25, r*(h/25), w/(w/h)/25, h/25))
    pygame.draw.rect(screen, (C[T[r][8]][0],C[T[r][8]][1],C[T[r][8]][2]), (7*w/(w/h)/25+w/2-5*w/(w/h)/25, r*(h/25), w/(w/h)/25, h/25))
    pygame.draw.rect(screen, (C[T[r][9]][0],C[T[r][9]][1],C[T[r][9]][2]), (8*w/(w/h)/25+w/2-5*w/(w/h)/25, r*(h/25), w/(w/h)/25, h/25))
    pygame.draw.rect(screen, (C[T[r][10]][0],C[T[r][10]][1],C[T[r][10]][2]), (9*w/(w/h)/25+w/2-5*w/(w/h)/25, r*(h/25), w/(w/h)/25, h/25))

#

while run:
    while game == 1:
        clock.tick(FPS)
        pygame.event.get()
        TR(1), TR(2), TR(3), TR(4), TR(5), TR(6), TR(7), TR(8), TR(9), TR(10), TR(11), TR(12), TR(13), TR(14), TR(15), TR(16), TR(17), TR(18)
        font = pygame.font.Font(None, 50) # Score
        score1=font.render(str(score),True,(255,255,255))
        score2=font.render("Score",True,(255,255,255))
        pygame.draw.rect(screen, (40,40,40), (11*w/(w/h)/25+w/2-5*w/(w/h)/25, 17*(h/25), 100, 60))
        screen.blit(score1, [11*w/(w/h)/25+w/2-5*w/(w/h)/25, 18*(h/25)])
        screen.blit(score2, [11*w/(w/h)/25+w/2-5*w/(w/h)/25, 17*(h/25)])  # End Score
        if NF[0] == 7:
            new_figure()
            now_figure(x1, y1, NF[0], NF[1]);
        if keyboard.is_pressed('w') and NF[0] < 6 and not space1 and not delay:
            t=10
            del_figure(x1, y1, NF[0], NF[1])
            nf1=NF[1]
            NF[1]=NF[1]+1
            buildf=1
            if NF[0] < 3 :
                if NF[1] > 3 :
                    del_figure(x1, y1, NF[0], NF[1])
                    NF[1]=0
                    buildf=1;
            if 6 > NF[0] > 2:
                if NF[1] > 1:
                    del_figure(x1, y1, NF[0], NF[1])
                    NF[1]=0
                    buildf=1;
            if checkpos(x1, y1, NF[0], NF[1]) and buildf == 1 and not delay:
                t=10
                print("Rotate")
                checkT()
                now_figure(x1, y1, NF[0], NF[1])
                buildf=0
            else:
                t=10
                NF[1]=nf1
                now_figure(x1, y1, NF[0], NF[1])
                buildf=0 ;
        if keyboard.is_pressed('a') and not space1 and not delay:
            t=10
            del_figure(x1, y1, NF[0], NF[1])
            x1=x1-1
            if checkpos(x1, y1, NF[0], NF[1]):
                print("A")
                checkT()
                now_figure(x1, y1, NF[0], NF[1])
            else:
                x1=x1+1
                now_figure(x1, y1, NF[0], NF[1]);
        if keyboard.is_pressed('d') and not space1 and not delay:
            t=10
            del_figure(x1, y1, NF[0], NF[1])
            x1=x1+1
            if checkpos(x1, y1, NF[0], NF[1]):
                print("D")
                checkT()
                now_figure(x1, y1, NF[0], NF[1])
            else:
                x1=x1-1
                now_figure(x1, y1, NF[0], NF[1]);
        if (td==0 and not space1) or (keyboard.is_pressed('s') and not space1 and not delay):
            t=10
            td=80
            del_figure(x1, y1, NF[0], NF[1])
            y1=y1+1
            if y1 == 1 and not checkpos(x1, y1, NF[0], NF[1]):
                print("game over")
                game=0;
            if checkpos(x1, y1, NF[0], NF[1]):
                print("S")
                checkT()
                now_figure(x1, y1, NF[0], NF[1])
            else:
                y1=y1-1
                now_figure(x1, y1, NF[0], NF[1])
                x1=4
                y1=0
                new_figure()
            now_figure(x1, y1, NF[0], NF[1]);
        if keyboard.is_pressed('space') and y1 < 15 and not space1 and not delay:
            t=10
            del_figure(x1, y1, NF[0], NF[1])
            savey1=y1
            y1=0
            space1=True;
        if space1 == True:
            if not checkpos(x1, y1, NF[0], NF[1]):
                if y1>savey1:
                    y1=y1-1
                    print("Space")
                    space1=False
                    now_figure(x1, y1, NF[0], NF[1])
                else:
                    y1=savey1
                    space1=False
                    now_figure(x1, y1, NF[0], NF[1])
            else:
                y1=y1+1
                space1=True;
        if keyboard.is_pressed('backspace'):
            pygame.quit()
            sys.exit();
        if keyboard.is_pressed('p') and not delay:
            print("Pause")
            t=10
            pause=1
            game=0
        if t > 0:
            delay = True
            t = t - 1
        else:
            delay = False
        if td>0:
            td=td-1
        pygame.display.update()

    while game==0 and pause==0:
        clock.tick(FPS)
        pygame.event.get()
        restarttext = font.render("Restart", True, (255, 255, 255))
        pressr = font.render("Press 'R'", True, (255,255,255))
        pygame.draw.rect(screen,(10,10,10),(0,0,w,h))
        screen.blit(score1, [w/2-70,h/2+160])
        screen.blit(score2, [w/2-70,h/2+120])
        screen.blit(restarttext, [w/2-70,h/2])
        screen.blit(pressr,[w/2-70,h/2+40])
        if keyboard.is_pressed('R'):
            print("restart")
            x1 = 4
            y1 = 0
            restart()
            score = 0
            game=1
        if keyboard.is_pressed('backspace'):
            pygame.quit()
            sys.exit()
        pygame.display.update();

    while pause==1:
        clock.tick(FPS)
        pygame.event.get()
        game=0
        td=100
        pygame.draw.rect(screen,(10,10,10),(0,0,w,h))
        pygame.draw.rect(screen, (40, 40, 40),(11 * w / (w / h) / 25 + w / 2 - 5 * w / (w / h) / 25, 17 * (h / 25), 100, 60))
        TR(1), TR(2), TR(3), TR(4), TR(5), TR(6), TR(7), TR(8), TR(9), TR(10), TR(11), TR(12), TR(13), TR(14), TR(15), TR(16), TR(17), TR(18)
        pause1=font.render("Pause",True,(255,255,255))
        screen.blit(score1, [11*w/(w/h)/25+w/2-5*w/(w/h)/25, 18*(h/25)])
        screen.blit(score2, [11*w/(w/h)/25+w/2-5*w/(w/h)/25, 17*(h/25)])
        screen.blit(pause1, [10,10])
        if keyboard.is_pressed('p') and not delay:
            print("Unpause")
            pygame.draw.rect(screen, (0,0,0),(0,0,w,h))
            t = 50
            delay = True
            pause=0
            game=1
        if t > 0:
            delay = True
            t = t - 1
        else:
            delay = False
        if keyboard.is_pressed('backspace'):
            pygame.quit()
            sys.exit()
        pygame.display.update();
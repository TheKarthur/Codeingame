import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

x=x0
y=y0
tam_jump_x=0
tam_jump_y=0
x_anterior=-1
y_anterior=-1

if(w>h): 
    tam_jump_x=(w-1)/2
    tam_jump_y=(w-1)/2
else: 
    tam_jump_x= (h-1)/2
    tam_jump_y= (h-1)/2

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    if(bomb_dir[0]=='U'):
        if(y-tam_jump_y>0):
            y-=tam_jump_y
            if(tam_jump_y/2>=1):
                tam_jump_y/=2
            else:
                tam_jump_y=1
        else:
            while y-tam_jump_y<0:
                tam_jump_y/=2
                if(tam_jump_y/2>=1):
                    tam_jump_y/=2
                else:
                    tam_jump_y=1
            y-=tam_jump_y
            
        if(len(bomb_dir)>1):
            if(bomb_dir[1]=="R"):
                if(x+tam_jump_x<w-1):
                    x+=tam_jump_x
                    if(tam_jump_x/2>=1):
                        tam_jump_x/=2
                    else:
                        tam_jump_x=1
                else:
                    while x+tam_jump_x>w-1:
                        tam_jump_x/=2
                    if(tam_jump_x/2>=1):
                        tam_jump_x/=2
                    else:
                        tam_jump_x=1
                    x+=tam_jump_x

            if(bomb_dir[1]=="L"):
                if(x-tam_jump_x>0):
                    x-=tam_jump_x
                    if(tam_jump_x/2>=1):
                        tam_jump_x/=2
                    else:
                        tam_jump_x=1
                else:
                    while x-tam_jump_x<0:
                        tam_jump_x/=2
                    if(tam_jump_x/2>=1):
                        tam_jump_x/=2
                    else:
                        tam_jump_x=1
                    x-=tam_jump_x

    if(bomb_dir[0]=='D'):
        if(y+tam_jump_y<h-1):
            y+=tam_jump_y
            if(tam_jump_y/2>=1):
                tam_jump_y/=2
            else:
                tam_jump_y=1
        else:
            while y+tam_jump_y>h-1:
                tam_jump_y/=2
                if(tam_jump_y/2>=1):
                    tam_jump_y/=2
                else:
                    tam_jump_y=1
            y+=tam_jump_y

        if(len(bomb_dir)>1):
            if(bomb_dir[1]=="R"):
                if(x+tam_jump_x<w-1):
                    x+=tam_jump_x
                    if(tam_jump_x/2>=1):
                        tam_jump_x/=2
                    else:
                        tam_jump_x=1
                else:
                    while x+tam_jump_x>w-1:
                        tam_jump_x/=2
                    if(tam_jump_x/2>=1):
                        tam_jump_x/=2
                    else:
                        tam_jump_x=1
                    x+=tam_jump_x

            if(bomb_dir[1]=="L"):
                if(x-tam_jump_x>0):
                    x-=tam_jump_x
                    if(tam_jump_x/2>=1):
                        tam_jump_x/=2
                    else:
                        tam_jump_x=1
                else:
                    while x-tam_jump_x<0:
                        tam_jump_x/=2
                    if(tam_jump_x/2>=1):
                        tam_jump_x/=2
                    else:
                        tam_jump_x=1
                    x-=tam_jump_x

    if(bomb_dir[0]=='R'):
        if(x+tam_jump_x<w-1):
            x+=tam_jump_x
            if(tam_jump_x/2>=1):
                tam_jump_x/=2
            else:
                tam_jump_x=1
        else:
            while x+tam_jump_x>w-1:
                tam_jump_x/=2
            if(tam_jump_x/2>=1):
                tam_jump_x/=2
            else:
                tam_jump_x=1
            x+=tam_jump_x

    if(bomb_dir[0]=="L"):
        if(x-tam_jump_x>0):
            x-=tam_jump_x
            if(tam_jump_x/2>=1):
                tam_jump_x/=2
            else:
                tam_jump_x=1
        else:
            while x-tam_jump_x<0:
                tam_jump_x/=2
            if(tam_jump_x/2>=1):
                tam_jump_x/=2
            else:
                tam_jump_x=1
            x-=tam_jump_x
     
    
    print(math.ceil(x),math.ceil(y))

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.

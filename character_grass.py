from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

hide_lattice()

cnt=0
x=400
y=90
mode=0
angle=270
while (1):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    if cnt==0:
        if mode==0:
            x+=1
            if(x==700):
                mode=1
        elif mode==1:
            x-=1
            y+=1
            if(x==400):
                mode=2
        elif mode==2:
            x-=1
            y-=1
            if(x==100):
                mode=0

        if x==400:
            if y==90:
                cnt+=1

    else:
        x=400+210*math.cos(math.pi*(angle/180))
        y=300+210*math.sin(math.pi*(angle/180))
        angle+=1
        if angle==270+360:
            angle=270
            x=400
            y=90
            mode=0
            cnt=0

    delay(0.01)
    
    


close_canvas()

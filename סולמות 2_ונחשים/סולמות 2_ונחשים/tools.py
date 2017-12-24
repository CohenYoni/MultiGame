import pygame,random,time,pickle,array
#=====screen data======
pygame.init()
display_width = 800
display_height = 600
#======colors=======
colors={'black':(0,0,0),'white':(255,255,255),'red':(255,0,0),'red_l':(210,0,0),'gray':(102,102,102),'gray_l':(204,204,204),'blue':(0,0,255),'green':(0,255,0)}
#=============general Settings=======
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Group 4')
clock = pygame.time.Clock()

#================messages==============
def text(word,x,y,color=colors['black'],type_font=pygame.font.get_default_font(),size_font=30):
    font=pygame.font.SysFont(type_font,size_font) 
    text = font.render(format(word), True, color)
    gameDisplay.blit(text,(x,y))                    

def text_objects(text,font):
    textSurfrace=font.render(text,True,colors['black'])
    return textSurfrace,textSurfrace.get_rect()

def message_display(text):
    gameDisplay.fill(colors['white'])
    largeText=pygame.font.Font('freesansbold.ttf',60)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2,display_height/2-160))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(1)
def Message_(msg,x,y):
    w=150
    h=60
    smallText = pygame.font.SysFont("comicsansms",18)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
def Message_2(msg,x,y):   
    w=400
    h=80
    smallText = pygame.font.SysFont("comicsansms",30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)    

##pygame.font.init()
##myfont = pygame.font.SysFont('Comic Sans MS', 30)
    
#===שמירה של הנותנים====    
def SaveData(Name,LastName,p_1,Ques,level,row,ws):
        
        ws.append([Name,LastName,p_1,Ques,level])
        print(Name,LastName,p_1,Ques,level)
        row += 1
        
        return row

#==כפתורים =====      
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
def button_2(msg,x,y,w,h,ic,ac,num):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))

        if click[0] == 1 and num=='1':    
            return 1
        if click[0] == 1 and num=='2':   
            return 2
        if click[0] == 1 and num=='3':   
            return 3
        if click[0] == 1 and num=='4':   
            return 4
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

##def button_(msg,x,y,w,h,ic,ac,num,action=None):
##    mouse = pygame.mouse.get_pos()
##    click = pygame.mouse.get_pressed()
##    if x+w > mouse[0] > x and y+h > mouse[1] > y:
##        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
##        if num!='0':
##            if click[0] == 1 and num=='1':    
##                return 1
##            if click[0] == 1 and num=='2':   
##                return 2
##            if click[0] == 1 and num=='3':   
##                return 3
##            if click[0] == 1 and num=='4':   
##                return 4
##        elif click[0] == 1 and action != None:
##            action()
##    else:
##        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
##    smallText = pygame.font.SysFont("comicsansms",20)
##    textSurf, textRect = text_objects(msg, smallText)
##    textRect.center = ( (x+(w/2)), (y+(h/2)) )
##    gameDisplay.blit(textSurf, textRect)
            

##pygame.font.init()
##myfont = pygame.font.SysFont('Comic Sans MS', 30)
    


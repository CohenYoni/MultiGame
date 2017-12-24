import laddersandsnakes
from laddersandsnakes import*
from openpyxl import Workbook
from openpyxl import load_workbook

#===============================functions====================
def inpt(x):
    def keyboard(x,y):
        word=''
        pygame.display.flip()
        default_font=pygame.font.get_default_font()
        font=pygame.font.SysFont(default_font,30)
        done = True
        while done:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:                      
                    if event.key == pygame.K_a:
                        word+=chr(event.key)
                    if event.key == pygame.K_b:
                        word+=chr(event.key)
                    if event.key == pygame.K_c:
                        word+=chr(event.key)
                    if event.key == pygame.K_d:
                        word+=chr(event.key)
                    if event.key == pygame.K_e:
                        word+=chr(event.key)
                    if event.key == pygame.K_f:
                        word+=chr(event.key)
                    if event.key == pygame.K_g:
                        word+=chr(event.key)
                    if event.key == pygame.K_h:
                        word+=chr(event.key)
                    if event.key == pygame.K_i:
                        word+=chr(event.key)
                    if event.key == pygame.K_m:
                        word+=chr(event.key)
                    if event.key == pygame.K_l:
                        word+=chr(event.key)
                    if event.key == pygame.K_n:
                        word+=chr(event.key)
                    if event.key == pygame.K_o:
                        word+=chr(event.key)
                    if event.key == pygame.K_p:
                        word+=chr(event.key)
                    if event.key == pygame.K_q:
                        word+=chr(event.key)
                    if event.key == pygame.K_r:
                        word+=chr(event.key)
                    if event.key == pygame.K_s:
                        word+=chr(event.key)
                    if event.key == pygame.K_t:
                        word+=chr(event.key)
                    if event.key == pygame.K_w:
                        word+=chr(event.key)
                    if event.key == pygame.K_x:
                        word+=chr(event.key)
                    if event.key == pygame.K_y:
                        word+=chr(event.key)
                    if event.key == pygame.K_z:
                        word+=chr(event.key)
                    if event.key == pygame.K_0:
                        word+=chr(event.key)
                    if event.key == pygame.K_1:
                        word+=chr(event.key)
                    if event.key == pygame.K_2:
                        word+=chr(event.key)
                    if event.key == pygame.K_3:
                        word+=chr(event.key)
                    if event.key == pygame.K_4:
                        word+=chr(event.key)
                    if event.key == pygame.K_5:
                        word+=chr(event.key)
                    if event.key == pygame.K_6:
                        word+=chr(event.key)
                    if event.key == pygame.K_7:
                        word+=chr(event.key)
                    if event.key == pygame.K_8:
                        word+=chr(event.key)
                    if event.key == pygame.K_9:
                        word+=chr(event.key)
                    if event.key == pygame.K_KP_ENTER:
                        done = False         
                    if event.key == pygame.K_SPACE:
                        word+=chr(event.key)
                    if event.key == pygame.K_BACKSPACE:
                        word=""
                        pygame.draw.rect(gameDisplay, colors['gray_l'],(250,x,290,60))
                    if event.key == pygame.K_RETURN:
                        done = False                   
                    gameDisplay.blit(font.render(word,True,colors['black']),(270,y))
                    pygame.display.flip()
        return word
    word=""
    LastName=""
    pygame.draw.rect(gameDisplay, colors['gray_l'],(250,180,290,60))
    pygame.draw.rect(gameDisplay, colors['gray_l'],(250,250,290,60))
    if x==1:
     text("Player 1 enter your name :",270,200) #example asking name of player1
    if x==2:
     text("Player 2 enter your name:",270,200) #example asking name of player2
    if x==3:
     text("Enter the Password:",285,200) #example asking password
    if x==4:
     text("Enter your Kid name:",280,200) 
    if(x!=3):
            pygame.draw.rect(gameDisplay, colors['gray_l'],(250,320,290,60))
            word=keyboard(250,270)
            LastName=keyboard(320,340)
            return word,LastName
    else:
        return keyboard(250,270)  
 
#========= בחירת משחק ===========
def Select_a_game(level):
    Game_m = True
    p_1,p_2,Q_1,Q_2=0,0,0,0
    num=0
    while Game_m:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(colors['white'])
        gameDisplay.blit(Selectagame,(0,0))
        num= button_2("Ladders and snakes",500,410,200,60,colors['gray_l'],colors['gray'],'1')
        num= button_2("Checkers",130,410,125,60,colors['gray_l'],colors['gray'],'2')
        #num= button_2("Back",340,230,125,60,colors['gray_l'],colors['gray'],'3')
        #num= button_2("Exit",340,300,125,60,colors['red'],colors['red_l'],'4')
        print(num)
        if 1==num:
             print(1.1)
             level,p_1,p_2,Q_1,Q_2=game_loop(level,main_menu)
             return level,p_1,p_2,Q_1,Q_2
        if 2==num:
             #level,p_1,p_2,Q_1,Q_2=game_loop(level,main_menu)
             print(2)
             return level,p_1,p_2,Q_1,Q_2
        if 3==num:
             main_menu()
        if 4==num:
            gameDisplay.fill(colors['white'])
            gameDisplay.blit(PicExit,(0,0))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            quit()
        pygame.display.update()
        clock.tick(15)




                        
#================================               
#============שמירה של הנותנים====    
def SaveData(Name,LastName,p_1,Ques,level,row,ws):
        
       ws.append([Name,LastName,p_1,Ques,level])
       print(Name,LastName,p_1,Ques,level)
       row += 1
        
       return row
 
#===================התפריט=======================
def Kid_():
       
    wb = Workbook()
    ws1 = wb.active
    row=0            
    Game_m = True
    gameDisplay.fill(colors['white'])
    message_display("Hello Kids")
    Name_1,LastName_1=inpt(1)
    Name_2,LastName_2=inpt(2)
    p_1,p_2=0,0
    Q_1,Q_2=0,0
    level=1
    gameDisplay.fill(colors['white'])
    while Game_m:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameDisplay.fill(colors['white'])
                gameDisplay.blit(PicExit,(0,0))
                pygame.display.update()
                time.sleep(3)
                pygame.quit()
                quit()
                
        gameDisplay.fill(colors['white'])
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects("Select Level", largeText)
        TextRect.center = ((display_width/2),(display_height/2-200))
        gameDisplay.blit(TextSurf, TextRect)
        mouse = pygame.mouse.get_pos()
      
        
        #==(תפריט של ילד )====

        if 1==button_2("age 6-8",340,230,125,60,colors['gray_l'],colors['gray'],'1'):   
             level,p_1,p_2,Q_1,Q_2=Select_a_game(1)
             #p_1,p_2,Q_1,Q_2=12,10,9,8  
             row=SaveData(Name_1,LastName_1,p_1,Q_1,"age 6-8",row,ws1)
             row=SaveData(Name_2,LastName_2,p_2,Q_2,"age 6-8",row,ws1)
             wb.save("Date.xlsx")
        if 2==button_2("age 8-10",340,300,125,60,colors['gray_l'],colors['gray'],'2'):
             level,p_1,p_2,Q_1,Q_2=Select_a_game(2)
             row=SaveData(Name_1,LastName_1,p_1,Q_1,"age 8-10",row,ws1)
             row=SaveData(Name_2,LastName_2,p_2,Q_2,"age 8-10",row,ws1)
             wb.save("Date.xlsx")
        if 3==button_2("age 10-12",340,370,125,60,colors['gray_l'],colors['gray'],'3'):
             level,p_1,p_2,Q_1,Q_2=Select_a_game(3,main_menu)
             row=SaveData(Name_1,LastName_1,p_1,Q_2,"age 10-12",row,ws1)
             row=SaveData(Name_2,LastName_2,p_2,Q_2,"age 10-12",row,ws1)
             wb.save("Date.xlsx")
        if 4==button_2("Back",340,440,125,60,colors['red'],colors['red_l'],'4'):   
             main_menu()
             
        
        
        pygame.display.update()
        clock.tick(15)
        
    
def Parent_():
    Game_m = True
    gameDisplay.fill(colors['white'])
    message_display("Hello Parents")
    Name_1,LastName_1=inpt(4)
    gameDisplay.fill(colors['white'])
    
    workbook = load_workbook('Date.xlsx')
    first_sheet = workbook.get_sheet_names()[0]
    worksheet = workbook.get_sheet_by_name(first_sheet)
    row=0    
    
    for row in worksheet.iter_rows():      
     for cell in row:     
        print(cell.value)     
     print()   

    workbook.save("Date.xlsx")
    if Name_1== player_:
            gameDisplay.blit(data_P,(100,200))#טבלה
            while Game_m:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameDisplay.fill(colors['white'])
                        gameDisplay.blit(PicExit,(0,0))
                        pygame.display.update()
                        time.sleep(3)   
                        pygame.quit()
                        quit()
                gameDisplay.fill(colors['white'])
                largeText = pygame.font.SysFont("comicsansms",60)
                TextSurf, TextRect = text_objects("Your kids results:", largeText)
                TextRect.center = ((display_width/2),(display_height/2-250))
                gameDisplay.blit(TextSurf, TextRect)
                
               
                button(str(player_),100,120,150,60,colors['gray_l'],colors['gray'])
                Message_("snak and letter",480,250)        
                Message_(str(point_),220,250)
                Message_("100",90,250)
                        
                
                button("Back",100,500,125,60,colors['gray_l'],colors['gray'],main_menu)
                button("Exit",595,500,125,60,colors['gray_l'],colors['gray'],quit)
               
                pygame.display.update()
                clock.tick(15)
    else:
            message_display("WRONG Name Try Again")
            time.sleep(1)   
            
def Counselor_():
    Game_m = True
    gameDisplay.fill(colors['white'])
    message_display("Hello Counselor")
    Pass=inpt(3)
    gameDisplay.fill(colors['white'])
    #===)אימות סיסמא של יועץ חינוכי )====
    if (Pass=="12345"):
            while Game_m:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameDisplay.fill(colors['white'])
                        gameDisplay.blit(PicExit,(0,0))
                        pygame.display.update()
                        time.sleep(3)
                        pygame.quit()
                        quit()
                gameDisplay.fill(colors['white'])
                largeText = pygame.font.SysFont("comicsansms",60)
                TextSurf, TextRect = text_objects("The kids results:", largeText)
                TextRect.center = ((display_width/2),(display_height/2-250))
                gameDisplay.blit(TextSurf, TextRect)





                
                button("Back",130,500,125,60,colors['gray_l'],colors['gray'],main_menu)
                button("Exit",580,500,125,60,colors['gray_l'],colors['gray'],quit)
               
                pygame.display.update()
                clock.tick(15)
    else:
            message_display("WRONG PASSWORD!")
            time.sleep(1)
            
            
#==============================================

                
def main_menu():


    gameDisplay.fill(colors['white'])
    gameDisplay.blit(Logo,(0,0))
    pygame.display.update()
    time.sleep(4)
    Game_m = True    
    while Game_m:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameDisplay.fill(colors['white'])
                gameDisplay.blit(PicExit,(0,0))
                pygame.display.update()
                time.sleep(3)
                pygame.quit()
                quit()
                
        gameDisplay.fill(colors['white'])
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects("welcome", largeText)
        TextRect.center = ((display_width/2),(display_height/2-200))
        gameDisplay.blit(TextSurf, TextRect)
        mouse = pygame.mouse.get_pos()
        
        button("kid",340,230,125,60,colors['gray_l'],colors['gray'],Kid_)
        button("Parent",340,300,125,60,colors['gray_l'],colors['gray'],Parent_)                     
        button("Counselor",340,370,125,60,colors['gray_l'],colors['gray'],Counselor_)
        button("Exit",340,440,125,60,colors['red'],colors['red_l'],quit)


        pygame.display.update()
        clock.tick(15)
        
main_menu()
#game_loop()
pygame.quit()
quit()

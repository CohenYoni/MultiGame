from questions import*
import questions
#from openpyxl import Workbook
#from openpyxl import load_workbook


#======game_location======
row={1:display_height - 66,2:display_height - 123,3:display_height - 182,4:display_height - 238,5:display_height - 297,6:display_height - 353,7:display_height - 410,8:display_height - 468,9:display_height - 525,10:display_height - 583}
col={1:-5,2:52,3:109,4:165,5:224,6:279,7:339,8:395,9:452,10:510}

#====Images===
player1Img=pygame.image.load('Pic\player1.png')
player2Img=pygame.image.load('Pic\player2.png')
BoardGame=pygame.image.load('Pic\BoardGame.png')
PicExit=pygame.image.load('Pic\Exit.png')
Logo=pygame.image.load('Pic\Logo2.png')
Selectagame=pygame.image.load('Pic\Select_a_game.png')
cube1=pygame.image.load('Pic\cube_1.png')
cube2=pygame.image.load('Pic\cube_2.png')
cube3=pygame.image.load('Pic\cube_3.png')
cube4=pygame.image.load('Pic\cube_4.png')
cube5=pygame.image.load('Pic\cube_5.png')
cube6=pygame.image.load('Pic\cube_6.png')

#=============Functions=========
def new_player(playerImg):
        questions=0
        corranswers=0
        def place(x,y):
                gameDisplay.blit(playerImg,(x,y))
        def update_answers(was_currect):
                nonlocal corranswers
                if was_currect==True:
                        corranswers+=1   
        def update_questions(was_question):
                nonlocal questions
                if was_question==True:
                        questions+=1
        def get_num_of_questions():
                return questions
        def get_num_of_corranswers():
                return corranswers
        return {'update_questions':update_questions,'update_answers':update_answers,'place':place,'get_answers':get_num_of_corranswers,'get_questions':get_num_of_questions}
def Cube_(player=0):
    def display_cube(cube,player):
        gameDisplay.blit(cube,(630,90))
        if player==1:
                pygame.draw.rect(gameDisplay, colors['red'],[620, 200, 80, 20])
                text("Player 1",620,200,colors['white'])
        elif player==2:
                pygame.draw.rect(gameDisplay, colors['blue'],[620, 240, 80, 20])
                text("Player 2",620,240,colors['white']) 

        pygame.display.update()
        time.sleep(0.5)      
    k=random.randint(1,6)    
    for i in range(k):
        if i==1:
             display_cube(cube3,player)   
        if i==2:
             display_cube(cube3,player)   
        if i==3:
             display_cube(cube6,player)  
        if i==4:
             display_cube(cube2,player)   
        if i==5:
             display_cube(cube5,player)   
        if i==6:
             display_cube(cube4,player)  
    if k==1:
             display_cube(cube1,player)
    if k==2:
             display_cube(cube2,player)
    if k==3:
             display_cube(cube3,player)
    if k==4:
             display_cube(cube4,player)
    if k==5:
             display_cube(cube5,player)
    if k==6:
             display_cube(cube6,player)        
    return k
    
def move(curr_index,cube_value):
        curr_index=curr_index+cube_value
        if curr_index > 100:
                curr_index=curr_index-cube_value-cube_value
                y=row[curr_index//10+1]
                x=col[10]        
        elif curr_index==100:
                y=row[curr_index//10]
                x=col[1] 
        elif (curr_index//10+1)%2!=0 :
                if curr_index%10!=0:
                   y=row[curr_index//10+1]      
                   x=col[curr_index%10]
                else:
                    y=row[curr_index//10]    
                    x=col[1]  
        else:
                if curr_index%10!=0:
                    y=row[curr_index//10+1]
                    x=col[11-(curr_index%10)]
                else:
                    y=row[curr_index//10]   
                    x=col[10]
        return x,y,curr_index
def check_move(location,L):
        question=False
        currectanswer=False
        def moving(newlocation,mess):
                nonlocal question
                pygame.draw.rect(gameDisplay, colors['gray_l'],[250, 220, 200, 100])
                text(mess,260,250,colors['black'],"comicsansms",22) 
                pygame.display.update()
                question=True
                currectanswer=Question(L)
                return currectanswer,question,newlocation
#ladder               
        if location==6:
           return moving(27,"you step on ladder")
        elif location==9:
           return moving(50,"you step on ladder")
        elif location==25:
           return moving(57,"you step on ladder")
        elif location==20:
           return moving(39,"you step on ladder")
        elif location==54:
           return moving(85,"you step on ladder")
        elif location==53:
           return moving(72,"you step on ladder")
        elif location==61:
           return moving(82,"you step on ladder")
#snake
        elif location==96:
           return moving(82,"you step on snake")

        elif location==95:
           return moving(73,"you step on snake")
        elif location==78:
           return moving(42,"you step on snake")
        elif location==55:
           return moving(34,"you step on snake")
        elif location==70:
           return moving(48,"you step on snake")
        elif location==43:
           return moving(16,"you step on snake")
        else:
                return currectanswer,question,location
        

    
def game_loop(level=1,main_menu=None):    
    x=(display_width*0)
    y=(display_height - 65)
    z=(display_width*0)
    w=(display_height - 100)
    player1=new_player(player1Img)
    player2=new_player(player2Img)
    k=1 #current location player 1
    v=1 #current location player 2
    iscurrect=False 
    isquestion=False
    gameExit = False
    gameDisplay.fill(colors['white'])
    turn=0
    while not gameExit:    
        v_change = 0
        k_change = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                turn+=1
                if turn%2 != 0 and event.key == pygame.K_SPACE:
                    k_change = Cube_(1)
                if turn%2 == 0 and event.key == pygame.K_SPACE:
                    v_change =Cube_(2)
                    
        gameDisplay.fill(colors['white'])
        gameDisplay.blit(BoardGame,(0,0))

        player1['place'](x,y)  
        player2['place'](z+15,w-20 )
                
        if turn%2 !=0:  
          x,y,k = move(k,k_change)
        if turn%2 == 0:
          z,w,v = move(v,v_change)


        gameDisplay.blit(BoardGame,(0,0))
        player1['place'](x,y)  
        player2['place'](z+15,w-20 )
        button("Back",620,430,125,60,colors['gray_l'],colors['gray'],main_menu)
        button("Exit",620,520,125,60,colors['gray_l'],colors['gray'],pygame.quit)

        text("Player 1: {0}/{1}".format(player1['get_questions'](),player1['get_answers']()),620,200)
        text("Player 2: {0}/{1}".format(player2['get_questions'](),player2['get_answers']()),620,240)  

        pygame.display.update()
        
        #===chack letter and snak + update Display======
        
        if turn%2 !=0:
         iscurrect,isquestion,k=check_move(k,level)
         player1['update_answers'](iscurrect)
         player1['update_questions'](isquestion)
         x,y,k = move(k,0)
        if turn%2 == 0:
         iscurrect,isquestion,v =check_move(v,level)
         player2['update_answers'](iscurrect)
         player2['update_questions'](isquestion)
         z,w,v = move(v,0)
        gameDisplay.blit(BoardGame,(0,0))
        player1['place'](x,y)  
        player2['place'](z+15,w-20 )
        
        #===show who win the game===  
        if k==100: 
           message_display("Red you win")
           return level,player1['get_answers'](),player2['get_answers'](),player1['get_questions'](),player2['get_questions']()
        if v==100:
           message_display("white you win")    
           return level,player1['get_answers'](),player2['get_answers'](),player1['get_questions'](),player2['get_questions']()
        
        button("Back",620,430,125,60,colors['gray_l'],colors['gray'],main_menu)
        button("Exit",620,520,125,60,colors['gray_l'],colors['gray'],pygame.quit)
        text("Player 1: {0}/{1}".format(player1['get_questions'](),player1['get_answers']()),620,200)
        text("Player 2: {0}/{1}".format(player2['get_questions'](),player2['get_answers']()),620,240)  

        pygame.display.update()
        clock.tick(10) 


#main_menu()
#game_loop()
#pygame.quit()
#quit()
    
            
    

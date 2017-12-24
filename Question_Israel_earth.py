from tools import *
import tools
#=============images=======================
data_P=pygame.image.load('Pic\dataP.png')
Q_IMG=pygame.image.load('Pic\Q.png')
T_IMG=pygame.image.load('Pic\True.png')
F_IMG=pygame.image.load('Pic\False.png')

#==========================================
Ques={1:(pygame.image.load('pic_Question\Q_ (1).png'),4),
      2:(pygame.image.load('pic_Question\Q_ (2).png'),3),
      3:(pygame.image.load('pic_Question\Q_ (3).png'),1),
      4:(pygame.image.load('pic_Question\Q_ (4).png'),3),
      5:(pygame.image.load('pic_Question\Q_ (5).png'),4),
      6:(pygame.image.load('pic_Question\Q_ (6).png'),1),
      7:(pygame.image.load('pic_Question\Q_ (7).png'),1),
      8:(pygame.image.load('pic_Question\Q_ (8).png'),3),
      9:(pygame.image.load('pic_Question\Q_ (9).png'),2),
      10:(pygame.image.load('pic_Question\Q_ (10).png'),2),
      11:(pygame.image.load('pic_Question\Q_ (11).png'),1),
      12:(pygame.image.load('pic_Question\Q_ (12).png'),3),
      13:(pygame.image.load('pic_Question\Q_ (13).png'),1),
      14:(pygame.image.load('pic_Question\Q_ (14).png'),1),
      15:(pygame.image.load('pic_Question\Q_ (15).png'),3),
      16:(pygame.image.load('pic_Question\Q_ (16).png'),2),
      17:(pygame.image.load('pic_Question\Q_ (17).png'),1),   
      18:(pygame.image.load('pic_Question\Q_ (18).png'),3),
      19:(pygame.image.load('pic_Question\Q_ (19).png'),1),
      20:(pygame.image.load('pic_Question\Q_ (20).png'),2),
      21:(pygame.image.load('pic_Question\Q_ (21).png'),3),
      22:(pygame.image.load('pic_Question\Q_ (22).png'),2),
      23:(pygame.image.load('pic_Question\Q_ (23).png'),3),
      24:(pygame.image.load('pic_Question\Q_ (24).png'),3),
      25:(pygame.image.load('pic_Question\Q_ (25).png'),1),
      26:(pygame.image.load('pic_Question\Q_ (26).png'),2),
      27:(pygame.image.load('pic_Question\Q_ (27).png'),1),
      28:(pygame.image.load('pic_Question\Q_ (28).png'),2),
      29:(pygame.image.load('pic_Question\Q_ (29).png'),1),
      30:(pygame.image.load('pic_Question\Q_ (30).png'),2),
      31:(pygame.image.load('pic_Question\Q_ (31).png'),1),
      32:(pygame.image.load('pic_Question\Q_ (32).png'),1),
      33:(pygame.image.load('pic_Question\Q_ (33).png'),1),
      34:(pygame.image.load('pic_Question\Q_ (34).png'),1),
      35:(pygame.image.load('pic_Question\Q_ (35).png'),2),
      36:(pygame.image.load('pic_Question\Q_ (36).png'),4),
      37:(pygame.image.load('pic_Question\Q_ (37).png'),2),   
      38:(pygame.image.load('pic_Question\Q_ (38).png'),2),
      39:(pygame.image.load('pic_Question\Q_ (39).png'),1),
      40:(pygame.image.load('pic_Question\Q_ (40).png'),2),
      41:(pygame.image.load('pic_Question\Q_ (41).png'),2),
      42:(pygame.image.load('pic_Question\Q_ (42).png'),4),
      43:(pygame.image.load('pic_Question\Q_ (43).png'),1),
      44:(pygame.image.load('pic_Question\Q_ (44).png'),3),
      45:(pygame.image.load('pic_Question\Q_ (45).png'),2),
      46:(pygame.image.load('pic_Question\Q_ (46).png'),1),
      47:(pygame.image.load('pic_Question\Q_ (47).png'),3),
      48:(pygame.image.load('pic_Question\Q_ (48).png'),3),
      49:(pygame.image.load('pic_Question\Q_ (49).png'),4),
      50:(pygame.image.load('pic_Question\Q_ (50).png'),4),
      51:(pygame.image.load('pic_Question\Q_ (51).png'),1),
      52:(pygame.image.load('pic_Question\Q_ (52).png'),4),
      53:(pygame.image.load('pic_Question\Q_ (53).png'),1),
      54:(pygame.image.load('pic_Question\Q_ (54).png'),3),
      55:(pygame.image.load('pic_Question\Q_ (55).png'),4),
      56:(pygame.image.load('pic_Question\Q_ (56).png'),2),
      57:(pygame.image.load('pic_Question\Q_ (57).png'),1),   
      58:(pygame.image.load('pic_Question\Q_ (58).png'),2),
      59:(pygame.image.load('pic_Question\Q_ (59).png'),3),
      60:(pygame.image.load('pic_Question\Q_ (60).png'),3)}


      
#==============(פונקציות שאלות)============

def question_Israel_earth(level):
        time.sleep(0.2)
        loop= True
        Ans=0
        
        if level==1:
          Q=random.randint(1,20)
        elif level==2:
          Q=random.randint(21,40)
        elif level==3:
          Q=random.randint(41,60)
        while loop:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()        

                gameDisplay.blit(Q_IMG,(0,0))
                pygame.draw.rect(gameDisplay, colors['gray_l'],(200,170,390,280))
                gameDisplay.blit(Ques[Q][0],(220,190))
                
                if button_2('1',130,470,125,60,colors['gray_l'],colors['gray'],'1'):
                                Ans=1
                if button_2('2',270,470,125,60,colors['gray_l'],colors['gray'],'2'):
                                Ans=2
                if button_2('3',410,470,125,60,colors['gray_l'],colors['gray'],'3'):
                                Ans=3
                if button_2('4',550,470,125,60,colors['gray_l'],colors['gray'],'4'):
                                Ans=4
                if Ans!=0:
                        if Ans==Ques[Q][1]:
                                gameDisplay.blit(T_IMG,(0,0))
                                pygame.display.update()
                                return True
                        else:
                                gameDisplay.blit(F_IMG,(0,0))
                                pygame.display.update()
                                gameDisplay.blit(F_IMG,(0,0))
                                pygame.display.update()
                                time.sleep(2)
                                gameDisplay.fill(colors['white'])
                                gameDisplay.blit(Ques[Q][0],(220,190))
                                largeText = pygame.font.Font('freesansbold.ttf',80)
                                TextSurf, TextRect = text_objects("The right answer", largeText)
                                TextRect.center = ((display_width/2),(display_height/2-200))
                                gameDisplay.blit(TextSurf, TextRect)
                                
                                button(str(Ques[Q][1]),350,440,125,60,colors['gray'],colors['gray'],)
                                
                                pygame.display.update()
                                time.sleep(2)
                                return False
                pygame.display.update()
                clock.tick(20)

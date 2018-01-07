from tools import *

######################## images ########################
correct_ansImg = pygame.image.load('pic_Question\correct_answer.png')
trueAnsImg = pygame.image.load(r'pic_Question\true_answer.png')
falseAnsImg = pygame.image.load(r'pic_Question\false_answer.png')
Pic_Qus = {1:pygame.image.load('pic_Question\Qus_ (1).png'),
      2:pygame.image.load('pic_Question\Qus_ (2).png'),
      3:pygame.image.load('pic_Question\Qus_ (3).png'),
      4:pygame.image.load('pic_Question\Qus_ (4).png'),
      5:pygame.image.load('pic_Question\Qus_ (5).png'),
      6:pygame.image.load('pic_Question\Qus_ (6).png'),
      7:pygame.image.load('pic_Question\Qus_ (7).png'),
      8:pygame.image.load('pic_Question\Qus_ (8).png'),
      9:pygame.image.load('pic_Question\Qus_ (9).png'),
      10:pygame.image.load('pic_Question\Qus_ (10).png')}

######################## mathematic questions ########################
math_questions = {1:("1 + 3 = ?",{1:"2",2:"3",3:"4",4:"1"},3),
      2:("9 + 1 = ?",{1:"12",2:"7",3:"6",4:"10"},4),
      3:("4 + 10 = ?",{1:"14",2:"13",3:"-14",4:"16"},1),
      4:("6 + 13 = ?",{1:"11",2:"19",3:"14",4:"13"},2),
      5:("8 + 9 = ? ",{1:"17",2:"20",3:"14",4:"10"},1),
      6:("9 + 11 = ?",{1:"19",2:"11",3:"20",4:"17"},3),
      7:("5 + 2 = ?",{1:"6",2:"5",3:"4",4:"7"},4),
      8:("6 + 3 = ?",{1:"7",2:"8",3:"9",4:"10"},3),
      9:("12 + 4 = ?",{1:"16",2:"15",3:"14",4:"17"},1),
      10:("10 + 3 = ?",{1:"18",2:"13",3:"19",4:"10"},2),
      11:("9 - 11 = ?",{1:"-19",2:"-1",3:"-20",4:"-2"},4),
      12:("5 - 2 = ?",{1:"6",2:"5",3:"4",4:"3"},4),
      13:("6 - 3 = ?",{1:"3",2:"8",3:"9",4:"1"},1),
      14:("12 - 4 = ?",{1:"16",2:"8",3:"4",4:"7"},2),
      15:("10 - 3 = ?",{1:"8",2:"3",3:"7",4:"10"},3),
      16:("1 - 3 = ?",{1:"-2",2:"-3",3:"-4",4:"-1"},1),
      17:("9 - 1 = ?",{1:"8",2:"7",3:"6",4:"9"},1),
      18:("4 - 10 = ?",{1:"14",2:"-14",3:"-6",4:"6"},3),
      19:("6 - 13 = ?",{1:"-11",2:"-7",3:"9",4:"10"},2),
      20:("7 - 9 = ?",{1:"-3",2:"2",3:"3",4:"-2"},4),
      21:("3 * 1 = ?",{1:"2",2:"3",3:"4",4:"1"},2),
      22:("9 * 2 = ?",{1:"12",2:"18",3:"16",4:"10"},2),
      23:("4 * 5 = ?",{1:"14",2:"15",3:"20",4:"16"},3),
      24:("6 * 2 = ?",{1:"11",2:"12",3:"14",4:"13"},2),
      25:("8 * 4 = ?",{1:"24",2:"30",3:"32",4:"10"},3),
      26:("3 * 3 = ?",{1:"9",2:"11",3:"12",4:"7"},1),
      27:("5 * 2 = ?",{1:"5",2:"13",3:"14",4:"10"},4),
      28:("7 * 3 = ?",{1:"23",2:"18",3:"21",4:"20"},3),
      29:("12 * 4 = ?",{1:"24",2:"48",3:"23",4:"27"},2),
      30:("10 * 3 = ?",{1:"30",2:"33",3:"31",4:"29"},1),
      31:("4 / 2 = ?",{1:"3",2:"4",3:"5",4:"2"},4),
      32:("10 / 2 = ?",{1:"6",2:"5",3:"4",4:"3"},2),
      33:("9 / 3 = ?",{1:"3",2:"8",3:"9",4:"1"},1),
      34:("12 / 4 = ?",{1:"6",2:"8",3:"3",4:"7"},3),
      35:("30 / 3 = ?",{1:"18",2:"13",3:"7",4:"10"},4),
      36:("14 / 2 = ?",{1:"-7",2:"7",3:"13",4:"11"},2),
      37:("9 / 1 = ?",{1:"8",2:"7",3:"6",4:"9"},4),
      38:("24 / 6 = ?",{1:"-4",2:"4",3:"-6",4:"6"},2),
      39:("33 / 11 = ?",{1:"11",2:"7",3:"3",4:"10"},3),
      40:("6 / 2 = ?",{1:"3",2:"2",3:"6",4:"4"},1),
      41:("(1 / 3) + 1 = ?",{1:"2.5",2:"3.3",3:"4.2",4:"1.3"},4),
      42:("(9 * 2) - 3 = ?",{1:"12",2:"18",3:"16",4:"15"},4),
      43:("(4 * 5) + 0.5 = ?",{1:"14.4",2:"15.5",3:"20.5",4:"16.5"},3),
      44:("(6 * 2) - 12 + 0.75 = ?",{1:"1.75",2:"12.75",3:"0.75",4:"13.75"},3),
      45:("[( 8 * 4) - 12] * 0.5=?",{1:"15.5",2:"10",3:"32",4:"13"},2),
      46:("[(3 * 3) / 2] + 1 = ?",{1:"5.5",2:"10.5",3:"9.2",4:"4.6"},1),
      47:("[(5 * 2) - 3] * 3 = ?",{1:"21",2:"13.5",3:"23.5",4:"10"},1),
      48:("(30 - 7 * 3) / 3 = ?",{1:"23",2:"3",3:"6",4:"30"},2),
      49:("(12 + 12 * 2) / 3 = ?",{1:"14",2:"22",3:"23",4:"12"},4),
      50:("(10 * 3 - 5) / 5 = ?",{1:"30",2:"23",3:"5",4:"19"},3),
      51:("(-6 + 4 / 2) + 0.5 = ?",{1:"-13.5",2:"14.4",3:"-3.5",4:"2.6"},3),
      52:("(10 / 2 + 0.5) * 0 = ?",{1:"6",2:"0",3:"4.5",4:"3.1"},2),
      53:("(-3 + 9 / 3) + 0.4 = ?",{1:"0.4",2:"8.4",3:"9.4",4:"1.4"},1),
      54:("(-1 + 2 / 4) -0.5 = ?",{1:"-1.4",2:"3.5",3:"-1",4:"1"},3),
      55:("(30 / 3 + 0.6) + 0.4 = ?",{1:"18.6",2:"13.4",3:"10",4:"11"},4),
      56:("(14 / 2 -20) * 0.5 = ?",{1:"-7",2:"-6.5",3:"3",4:"7"},2),
      57:("(9 / 2) + 0.5) * 2 = ?",{1:"8.5",2:"7.5",3:"12",4:"10"},4),
      58:("(-8 + 24 / 6) / 2 = ?",{1:"-4",2:"-2",3:"-24",4:"-6"},2),
      59:("(33 / 11 - 5.5) * 2 = ?",{1:"11",2:"7.5",3:"-5",4:"10"},3),
      60:("[(2*3+20)*0]+0.3=?",{1:"0.1",2:"0",3:"0.3",4:"0.4"},3)}

######################## Knowledge of the Land of Israel questions ########################
israel_questions = {1:(pygame.image.load('pic_Question\Q_ (1).png'),4),
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

# ques_type can be 'math' or 'israel'
def show_question(level, ques_type):
    ''' show quastion screen '''
    time.sleep(0.4)
    ans = 0
    loop = True
    j = random.randint(1,10) # pick background image for the questions randomly
    if level == 1: # age 6-8
        i = random.randint(1,20)
    elif level == 2: # age 8-10
        i = random.randint(21,40)
    elif level == 3: # age 10-12
        i = random.randint(41,60)
    pressed = False
    gameDisplay.blit(Pic_Qus[j], (0, 0))
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitTheGame()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == left:
                pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                pressed = False
        if ques_type == 'math':
            pygame.draw.rect(gameDisplay, colors['gray_l'], (80, 240, 640, 130))
            text_center(math_questions[i][0], 400, 300, 70) # show question

            # 4 possible answers
            if button(math_questions[i][1][1], 130, 440, 125, 60, pressed, colors['gray_l'], colors['gray']):
                ans = 1
                pressed = False
            if button(math_questions[i][1][2], 270, 440, 125, 60, pressed, colors['gray_l'], colors['gray']):
                ans = 2
                pressed = False
            if button(math_questions[i][1][3], 410, 440, 125, 60, pressed, colors['gray_l'], colors['gray']):
                ans = 3
                pressed = False
            if button(math_questions[i][1][4], 550, 440, 125, 60, pressed, colors['gray_l'], colors['gray']):
                ans = 4
                pressed = False

            if ans == math_questions[i][2]: # the answer is correct
                gameDisplay.blit(trueAnsImg, (0, 0))
                pygame.display.update()
                time.sleep(1)
                return True
            elif ans != 0: # the answer is not correct. show the correct answer.
                gameDisplay.blit(falseAnsImg, (0, 0))
                pygame.display.update()
                time.sleep(1)
                gameDisplay.blit(correct_ansImg, (0, 0))
                pygame.draw.rect(gameDisplay, colors['gray_l'], (100, 240, 600, 130))
                text_center(math_questions[i][0], 380, 300, 80)
                text_center('The right', 400, 120, 70)
                text_center('answer is {0}'.format(math_questions[i][1][math_questions[i][2]]), 400, 200, 70)
                pygame.display.update()
                time.sleep(4)
                return False

        if ques_type == 'israel':
            pygame.draw.rect(gameDisplay, colors['gray_l'], (200, 180, 390, 280))
            gameDisplay.blit(israel_questions[i][0], (220, 200)) # show question

            # 4 possible answers
            if button('1', 130, 470, 125, 60, pressed, colors['gray_l'], colors['gray']):
                ans = 1
                pressed = False
            if button('2', 270, 470, 125, 60, pressed, colors['gray_l'], colors['gray']):
                ans = 2
                pressed = False
            if button('3', 410, 470, 125, 60, pressed, colors['gray_l'], colors['gray']):
                ans = 3
                pressed = False
            if button('4', 550, 470, 125, 60, pressed, colors['gray_l'], colors['gray']):
                ans = 4
                pressed = False

            if ans == israel_questions[i][1]: # the answer is correct
                gameDisplay.blit(trueAnsImg, (0, 0))
                pygame.display.update()
                time.sleep(1)
                return True
            elif ans != 0: # the answer is not correct. show the correct answer.
                gameDisplay.blit(falseAnsImg, (0, 0))
                pygame.display.update()
                time.sleep(1)
                gameDisplay.blit(correct_ansImg, (0, 0))
                pygame.draw.rect(gameDisplay, colors['gray_l'], (200, 180, 390, 280))
                gameDisplay.blit(israel_questions[i][0], (220, 200))
                text_center('The right answer', 400, 140, 70)
                text_center('is {0}'.format(israel_questions[i][1]), 400, 500, 70)
                pygame.display.update()
                time.sleep(4)
                return False
        pygame.display.update()
        clock.tick(60)
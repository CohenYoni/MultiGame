from laddersandsnakes import *
from checkers import *

######################## images ########################
SelectGameImg = pygame.image.load('Pic_menu\Select_a_game.png')
consulerImg = pygame.image.load('Pic_menu\consulerTable.png') # consuler table data
parentImg = pygame.image.load('Pic_menu\parentTable.png') # parent table data
Parent_instructionImg = pygame.image.load('Pic_menu\parent_instruction.png')
Counselor_instructionImg = pygame.image.load('Pic_menu\consuler_instruction.png')
Background_menusLargeImg = pygame.image.load('Pic_menu\BackgroundMainLarge.png')

######################## passwords ########################
parent_pass = ('1234', '1111')
counselor_pass = ('12345', '11111')

######################## functions ########################

def main_menu():
    ''' main menu screen '''
    end_loop = False
    pressed = False
    while not end_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitTheGame()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                pressed = False
        gameDisplay.blit(Background_menusImg, (0, 0))
        text_center("Welcome", display_width / 2, display_height / 2 - 180, 150)
        button("Kid", 310, 230, 180, 60, pressed, colors['gray_l'], colors['gray'], Kid_)
        button("Parent", 310, 300, 180, 60, pressed, colors['gray_l'], colors['gray'], Parent_)
        button("Counselor", 310, 370, 180, 60, pressed, colors['gray_l'], colors['gray'], Counselor_)
        button("Exit", 310, 440, 180, 60, pressed, colors['red_l'], colors['red'], QuitTheGame)
        if image_button(helpImg, 255, 305, pressed):
            instruction(Parent_instructionImg)
            pressed = False
        if image_button(helpImg, 255, 375, pressed):
            instruction(Counselor_instructionImg)
            pressed = False


        pygame.display.update()
        clock.tick(60)

def Kid_():
    ''' kid screen '''
    name2 = None # a list. if there is another player- append to the list [first_name, last_name]
    gameDisplay.blit(Background_menusImg, (0, 0))
    text_center("Hello Kids!", display_width / 2, 50, 70)

    #input firs name
    text_center('Enter the first name and then press Enter', display_width / 2, 120, 40)
    first_name1 = input_keybord(250, 150)
    text_center('Enter the last name and then press Enter', display_width / 2, 220, 40)
    last_name1 = input_keybord(250, 250)
    loop_end = False
    text_display('select level of quastion', 40, 420, 60)
    player2_recorded = False # check if the child entered another player name
    pressed = False
    while not loop_end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitTheGame()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                pressed = False
        if not player2_recorded and button('press here if there is another player', 90, 320, 620, 60, pressed,
                  colors['gray_l'], colors['gray']):
            gameDisplay.blit(Background_menusImg, (0, 0))
            pygame.display.update()
            name2 = []
            text_center('Enter the first name and then press Enter', display_width / 2, 120, 40)
            name2.append(input_keybord(250, 150))
            text_center('Enter the last name and then press Enter', display_width / 2, 220, 40)
            name2.append(input_keybord(250, 250))
            text_display('select level of quastion', 40, 420, 60)
            player2_recorded = True
            pressed = False
        button('age 6-8', 50, 500, 170, 60, pressed, colors['gray_l'], colors['gray'],
               Select_a_game, 1, (first_name1, last_name1), name2)
        button('age 8-10', 230, 500, 170, 60, pressed, colors['gray_l'], colors['gray'],
               Select_a_game, 2, (first_name1, last_name1), name2)
        button('age 10-12', 410, 500, 170, 60, pressed, colors['gray_l'], colors['gray'],
               Select_a_game, 3, (first_name1, last_name1), name2)
        button("Back", 650, 450, 125, 60, pressed, colors['gray_l'], colors['gray'], main_menu)
        button("Exit", 650, 520, 125, 60, pressed, colors['red_l'], colors['red'], QuitTheGame)
        pygame.display.update()
        clock.tick(60)

def Select_a_game(level_quastions, name1, name2 = None):
    ''' select a game screen '''
    end_loop = False
    pressed = False
    while not end_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitTheGame()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                pressed = False

        gameDisplay.blit(SelectGameImg,(0, 0))
        if button("Ladders and snakes", 403, 410, 350, 60, pressed, colors['gray_l'],colors['gray']):
            pressed = False
            if name2 == None: # prevent situation that the child entered just one name
                name2 = []
                gameDisplay.blit(Background_menusImg, (0, 0))
                text_center('Please enter the name of the second player', display_width / 2, 50, 44)
                text_center('Enter the first name and then press Enter', display_width / 2, 120, 40)
                name2.append(input_keybord(250, 150))
                text_center('Enter the last name and then press Enter', display_width / 2, 220, 40)
                name2.append(input_keybord(250, 250))
            LaddersAndSnakes(level_quastions, name1, name2, main_menu)
        button("Checkers", 45, 410, 350, 60, pressed, colors['gray_l'],colors['gray'],
               rival, level_quastions, name1, name2, main_menu)
        button("Back", 340, 230, 125, 60, pressed, colors['gray_l'], colors['gray'], main_menu)
        button("Exit", 340, 300, 125, 60, pressed, colors['red_l'], colors['red'], QuitTheGame)
        if image_button(helpImg, -2, 415, pressed):
            instruction(Checkers_instructionImg)
            pressed = False
        if image_button(helpImg, 750, 415, pressed):
            instruction(Ledders_instructionImg)
            pressed = False
        pygame.display.update()
        clock.tick(60)

def Counselor_():
    ''' counselor screen '''
    ages = ('6-8', '8-10', '10-12')
    games = ('Checkers', 'Ladders And Snakes')

    for _ in range(3): # can try 3 times to enter a password
        gameDisplay.blit(Background_menusImg, (0, 0))
        text_center('Hello Counselor', display_width / 2, 100, 80)
        text_center('enter a password', display_width / 2, 250, 60)
        text_center('press Enter to finish', display_width / 2, 400, 30)
        password = input_keybord(250, 300)

        if password in counselor_pass:
            loop_end = False
            pressed = False
            while not loop_end:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        QuitTheGame()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pressed = True
                    elif event.type == pygame.MOUSEBUTTONUP:
                        pressed = False
                gameDisplay.blit(Background_menusImg, (0, 0))
                gameDisplay.blit(consulerImg, (25, 0))

                for i in range(3):
                    text_display(str(i + 1), 730, 100 + (i * 100)) # serial namber of the rows
                    text_display(str(ages[i]), 590, 100 + (i * 100)) # show the ages
                    text_display(str(avg_per_age(ages[i], games[1], data_base)), 400, 100 + (i * 100)) # show average for each age for checkers
                    text_display(str(avg_per_age(ages[i], games[0], data_base)), 150, 100 + (i * 100)) # show average for each age for ledders and snakes


                text_display('average of math questions: ' + str(avg_per_game(games[1], data_base)), 100, 450, 30)
                text_display('average of land of Israel questions: ' + str(avg_per_game(games[0], data_base)), 100, 500, 30)
                button("Back", 650, 450, 125, 60, pressed, colors['gray_l'], colors['gray'], main_menu)
                button("Exit", 650, 520, 125, 60, pressed, colors['red_l'], colors['red'], QuitTheGame)

                pygame.display.update()
                clock.tick(60)
        else:
            gameDisplay.blit(Background_menusImg, (0, 0))
            text_center("WRONG PASSWORD!", display_width / 2, display_height / 2, 80)
            pygame.display.update()
            time.sleep(1)

    gameDisplay.blit(Background_menusImg, (0, 0))
    text_center("you tried", display_width / 2, display_height / 2 - 50, 80)
    text_center("too many times", display_width / 2, display_height / 2 + 50, 80)
    pygame.display.update()
    time.sleep(1.5)
    QuitTheGame()

def Parent_():
    ''' parent screen '''
    ages = ('6-8', '8-10', '10-12')
    for _ in range(3): # can try 3 times to enter a password
        gameDisplay.blit(Background_menusImg, (0, 0))
        text_center('Hello Parents', display_width / 2, 100, 80)
        text_center('enter a password', display_width / 2, 250, 60)
        text_center('press Enter to finish', display_width / 2, 400, 30)
        password = input_keybord(250, 300)

        if password in parent_pass:
            gameDisplay.blit(Background_menusImg, (0, 0))
            text_center('enter first name', display_width / 2, 100, 60)
            text_center('press Enter to finish', display_width / 2, 250, 30)
            first_name = input_keybord(250, 150)
            text_center('enter last name', display_width / 2, 350, 60)
            text_center('press Enter to finish', display_width / 2, 500, 30)
            last_name = input_keybord(250, 400)
            pygame.display.set_mode((800, 700)) # for more space if there is a lot of grades
            gameDisplay.blit(Background_menusLargeImg, (0, 0))
            text_display("{0} {1}".format(first_name, last_name), 20, 5, 30) # show the name of the child
            gameDisplay.blit(parentImg, (0, 40))
            kid_games = find_kid_games(first_name, last_name, data_base) # list of all games of the child
            text_display("average Math: {0}".format(int(avg_per_game('Ladders And Snakes', kid_games))), 300, 5, 30)
            text_display("average Israel: {0}".format(int(avg_per_game('Checkers', kid_games))), 550, 5, 30)
            i = 0
            for row in kid_games:
                i += 1
                text_display(str(i), 770, 50 + (i * 30)) # serial number of the game
                text_display(str(row[6]), 400, 50 + (i * 30)) # show the type of the quastions
                text_display('{0}/{1}'.format(row[4], row[3]), 200, 50 + (i * 30)) # show the number of correct answers from the questions
                text_display(str(int(grade_one_game(row))), 50, 50 + (i * 30)) # show the grade of one game
            pressed = False
            loop_end = False
            while not loop_end:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.display.set_mode((display_width, display_height))
                        QuitTheGame()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pressed = True
                    elif event.type == pygame.MOUSEBUTTONUP:
                        pressed = False
                if image_button(menuButtonImg, 760, 45, pressed):
                    pressed = False
                    pygame.display.set_mode((display_width, display_height))
                    main_menu()
                pygame.display.update()
                clock.tick(60)
        else:
            gameDisplay.blit(Background_menusImg, (0, 0))
            text_center("WRONG PASSWORD!", display_width / 2, display_height / 2, 80)
            pygame.display.update()
            time.sleep(1)

    gameDisplay.blit(Background_menusImg, (0, 0))
    text_center("you tried", display_width / 2, display_height / 2 - 50, 80)
    text_center("too many times", display_width / 2, display_height / 2 + 50, 80)
    pygame.display.update()
    time.sleep(1.5)
    QuitTheGame()

main_menu()
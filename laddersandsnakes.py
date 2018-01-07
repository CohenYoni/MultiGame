from questions import*
import questions

######################## dimensions ########################
row = {1:display_height - 66, 2:display_height - 123, 3:display_height - 182,
       4:display_height - 238, 5:display_height - 297, 6:display_height - 353,
       7:display_height - 410, 8:display_height - 468, 9:display_height - 525, 10:display_height - 583}
col = {1:-5, 2:52, 3:109, 4:165, 5:224, 6:279, 7:339, 8:395, 9:452, 10:510}

######################## images ########################
player1Img = pygame.image.load('Pic_laddersAndSnakes\player1.png')
player2Img = pygame.image.load('Pic_laddersAndSnakes\player2.png')
BoardGame = pygame.image.load('Pic_laddersAndSnakes\BoardGame.png')
rollDiceImg = pygame.image.load(r'Pic_laddersAndSnakes\roll_dice.png')
cubeImgs = {1:pygame.image.load('Pic_laddersAndSnakes\cube_1.png'),
            2:pygame.image.load('Pic_laddersAndSnakes\cube_2.png'),
            3:pygame.image.load('Pic_laddersAndSnakes\cube_3.png'),
            4:pygame.image.load('Pic_laddersAndSnakes\cube_4.png'),
            5:pygame.image.load('Pic_laddersAndSnakes\cube_5.png'),
            6:pygame.image.load('Pic_laddersAndSnakes\cube_6.png')}

######################## functions ########################

# create new player. dispatch dictionary and message passing.
# API: 'update_questions', 'update_answers', 'place', 'get_answers', 'get_questions'.
def new_player(playerImg = None):

    questions=0
    corranswers=0

    def place(x,y):
        if playerImg:
            gameDisplay.blit(playerImg,(x,y))

    def update_answers(was_currect):
        nonlocal corranswers
        if was_currect == True:
            corranswers += 1

    def update_questions(was_question):
        nonlocal questions
        if was_question == True:
            questions += 1

    def get_num_of_questions():
        return questions

    def get_num_of_corranswers():
        return corranswers

    return {'update_questions':update_questions, 'update_answers':update_answers, 'place':place,
            'get_answers':get_num_of_corranswers, 'get_questions':get_num_of_questions}

# Draw a cube with a random value
#---player can be 1 (player one) or 2 (player two)---
def Cube(player = 0):

    def display_cube(cube, player):
        gameDisplay.blit(cube,(630,90))
        if player == 1:
            pygame.draw.rect(gameDisplay, colors['red'],[620, 200, 100, 30])
            text_display("Player 1", 620, 200, 30, colors['white'])
        elif player == 2:
            pygame.draw.rect(gameDisplay, colors['blue'],[620, 240, 100, 30])
            text_display("Player 2", 620, 240,30 ,colors['white'])
        pygame.display.update()

    for _ in range(6): # rolling the dice
        i = random.randint(1,6)
        display_cube(cubeImgs[i], player)
        time.sleep(0.2)

    val = random.randint(1, 6)
    display_cube(cubeImgs[val], player)
    time.sleep(1)
    return val

# the function map the location to new position by cube valu
#---curr_index is current position---
#---cube_value is value of cube---
def move(curr_index, cube_value):

    if curr_index + cube_value > 100: # The player does not step on 100
        curr_index = 100 - (cube_value - (100 - curr_index)) # reverse the rest of the steps
        y = row[10]
        x = col[curr_index % 10] # 94 < curr_index < 100 => 4 < col < 10
    else: # the new position is not out of board
        curr_index = curr_index + cube_value
        if curr_index == 100: # the game is ended
            y = row[10]
            x = col[1]
        elif (curr_index//10 + 1) % 2 != 0: # if the new position is even row. the direction of the steps is reverse.
            if curr_index % 10 != 0: # if the new position is not the end of the row
                y = row[curr_index//10 + 1]
                x = col[curr_index % 10]
            else:
                y = row[curr_index//10]
                x = col[1]
        else: # if the new position is odd row.
            if curr_index % 10 != 0: # if the position is end of the line
                y = row[curr_index//10 + 1]
                x = col[11 - (curr_index % 10)]
            else:
                y = row[curr_index//10]
                x = col[10]
    return x, y, curr_index

# check if player hit in snake or ladder
#---location is the current position of player---
def check_move(location, level):
    question = False
    currectanswer = False
    # if there are hit -> get question and display new position
    def moving(newlocation, message):
        nonlocal question
        pygame.draw.rect(gameDisplay, colors['gray_l'], [250, 220, 250, 100])
        text_display(message, 260, 250,30 ,colors['black'])
        pygame.display.update()
        time.sleep(1.5)
        question = True
        currectanswer = show_question(level, 'math')
        return currectanswer, question, newlocation

    # key: first position, value: position after the move.
    ladders = {6:27, 9:50, 25:57, 20:39, 54:85, 53:72, 61:82}
    snakes = {96: 82, 95: 73, 78: 42, 55: 34, 70: 48, 43: 16}

    # move according to the ladder or the snake
    if location in ladders:
        return moving(ladders[location], "you step on ladder")
    elif location in snakes:
        return moving(snakes[location], "you step on snake")
    else: # return False, False, on the quastions, and the currect position.
        return currectanswer, question, location


def LaddersAndSnakes(level, player1_name, player2_name, back = None):
    ''' play ladders and snakes '''

    # place the pieces on the first position
    player1_x = 0
    player1_y = display_height - 60
    player2_x = 0
    player2_y = (display_height - 70)

    # get new players. each player is a dictionary, with API: 'update_questions', 'update_answers', 'place', 'get_answers', 'get_questions'.
    player1 = new_player(player1Img)
    player2 = new_player(player2Img)
    locPlayer1 = 1 #first location player 1
    locPlayer2 = 1 #first location player 2
    iscurrect = False
    isquestion = False
    gameEnded = False
    pressed = False
    gameDisplay.fill(colors['white'])
    turn = 0 # odd number is player 1 turn, even number is player 2 turn.
    while not gameEnded:
        locPlayer1_change = 0
        locPlayer2_change = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitTheGame()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                pressed = False

        # place the board and the pieces on the screen
        gameDisplay.blit(BoardGame, (0, 0))
        player1['place'](player1_x, player1_y)
        player2['place'](player2_x + 15, player2_y - 20)

        text_display("Player 1: {0}/{1}".format(player1['get_answers'](), player1['get_questions']()), 620, 200)
        text_display("Player 2: {0}/{1}".format(player2['get_answers'](), player2['get_questions']()), 620, 240)

        button("Back", 620, 430, 125, 60, pressed, colors['gray_l'], colors['gray'], back)
        button("Exit", 620, 520, 125, 60, pressed, colors['red_l'], colors['red'], QuitTheGame)
        if image_button(helpImg, 675, 5, pressed):
            instruction(Ledders_instructionImg)
            pressed = False

        # rolling the dice functionality
        if image_button(rollDiceImg, 630, 300, pressed):
            pressed = False
            turn += 1
            # ===make a move, check ladder or snake and update Display======
            if turn % 2 != 0: # player 1 turn
                locPlayer1_change = Cube(1)
                player1_x, player1_y, locPlayer1 = move(locPlayer1, locPlayer1_change)
                gameDisplay.blit(BoardGame, (0, 0))
                player1['place'](player1_x, player1_y)
                player2['place'](player2_x + 15, player2_y - 20)
                iscurrect, isquestion, locPlayer1 = check_move(locPlayer1, level)
                if isquestion: # if was a question
                    player1['update_questions'](isquestion)
                    player1['update_answers'](iscurrect)
                    player1_x, player1_y, locPlayer1 = move(locPlayer1, 0)
            if turn % 2 == 0: # player 2 turn
                locPlayer2_change = Cube(2)
                player2_x, player2_y, locPlayer2 = move(locPlayer2, locPlayer2_change)
                gameDisplay.blit(BoardGame, (0, 0))
                player1['place'](player1_x, player1_y)
                player2['place'](player2_x + 15, player2_y - 20)
                iscurrect, isquestion, locPlayer2 = check_move(locPlayer2, level)
                if isquestion: # if was a question
                    player2['update_questions'](isquestion)
                    player2['update_answers'](iscurrect)
                    player2_x, player2_y, locPlayer2 = move(locPlayer2, 0)

        # ===show who win the game===
        if locPlayer1 == 100:
            text_center("Red you win!", display_width / 2, display_height / 2, 140)
            gameEnded = True
        if locPlayer2 == 100:
            text_center("White you win!", display_width / 2, display_height / 2, 140)
            gameEnded = True

        pygame.display.update()
        clock.tick(60)

    # add the game data to the database
    if level == 1:
        age = 'age 6-8'
    elif level == 2:
        age = 'age 8-10'
    else:
        age = 'age 10-12'
    add_game_data_to_DB(player1_name[0], player1_name[1], age, player1['get_questions'](),
                        player1['get_answers'](), 'Ladders And Snakes', 'Math')
    add_game_data_to_DB(player2_name[0], player2_name[1], age, player2['get_questions'](),
                        player2['get_answers'](), 'Ladders And Snakes', 'Math')
    if back != None:
        back()

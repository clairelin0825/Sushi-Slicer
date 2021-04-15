import pygame
import os
import random
pygame.init()

player_lives = 3                                                #keep track of lives
score = 0                                                       #keeps track of score
ingredients = ['Riceglob', 'Tamago', 'Avocado', 'Carrot', 'Crab', 'Cucumber', 'Eel', 'Salmon', 'Shrimp', 'Tuna']    #entities in the game
fruits = ['bomb', 'guava', 'melon', 'orange', 'pomegranate']

# initialize pygame and create window
WIDTH = 800
HEIGHT = 500
FPS = 12                                                 #controls how often the gameDisplay should refresh. In our case, it will refresh every 1/12th second
pygame.init()
pygame.display.set_caption('Sushi Slicer/Fruit Ninja Game -- Yannie & Claire')
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))   #setting game display size
clock = pygame.time.Clock()

# Define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

background1 = pygame.image.load('sushi/background.jpeg')
background1 = pygame.transform.scale(background1, (800,500))
font = pygame.font.Font(os.path.join(os.getcwd(), 'sushi/comic.ttf'), 42)
score_text = font.render('Score : ' + str(score), True, (255, 255, 255))    #score display
lives_icon = pygame.image.load('sushi/images/white_lives.png')                    #images that shows remaining lives

# Generalized structure of the fruit Dictionary
data = {}
def generate_random_ingredients(ingredient):
    ingredient_path = "sushi/images/" + ingredient + ".png"
    data[ingredient] = {
        'img': pygame.image.load(ingredient_path),
        'x' : random.randint(100,500),          #where the fruit should be positioned on x-coordinate
        'y' : 800,
        'speed_x': random.randint(-10,10),      #how fast the fruit should move in x direction. Controls the diagonal movement of fruits
        'speed_y': random.randint(-80, -60),    #control the speed of fruits in y-directionn ( UP )
        'throw': False,                         #determines if the generated coordinate of the fruits is outside the gameDisplay or not. If outside, then it will be discarded
        't': 0,                                 #manages the
        'hit': False,
    }

    if random.random() >= 0.75:     #Return the next random floating point number in the range [0.0, 1.0) to keep the fruits inside the gameDisplay
        data[ingredient]['throw'] = True
    else:
        data[ingredient]['throw'] = False

def hide_cross_lives(x, y):
    gameDisplay.blit(pygame.image.load("sushi/images/red_lives.png"), (x, y))

# Generic method to draw fonts on the screen
font_name = pygame.font.match_font('comic.ttf')
def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)

# draw players lives
def draw_lives(display, x, y, lives, image) :
    for i in range(lives) :
        img = pygame.image.load(image)
        img_rect = img.get_rect()       #gets the (x,y) coordinates of the cross icons (lives on the the top rightmost side)
        img_rect.x = int(x + 35 * i)    #sets the next cross icon 35pixels awt from the previous one
        img_rect.y = y                  #takes care of how many pixels the cross icon should be positioned from top of the screen
        display.blit(img, img_rect)

# show game over display & front display
key1 = ''
def show_gameover_screen():
    global key1
    global background
    global data
    gameDisplay.blit(background1, (0,0))
    draw_text(gameDisplay, "Fruit Ninja/Sushi Slicer!", 90, WIDTH / 2, HEIGHT / 4)
    if not game_over :
        draw_text(gameDisplay,"Score : " + str(score), 50, WIDTH / 2, HEIGHT /2)

    draw_text(gameDisplay, "Press RETURN to begin Sushi Slicer mode!", 40, WIDTH / 2, HEIGHT * 3 / 4)
    draw_text(gameDisplay, "Press SPACE to begin Fruit Ninja mode!", 40, WIDTH / 2, HEIGHT * 2 / 3)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #fruit ninja mode
                    key1 = 'fruits'
                    background = pygame.image.load('sushi/back.jpg')
                    data = {}
                    for i in range(0, 3):
                        generate_random_ingredients(fruits[i])
                    waiting = False
                if event.key == pygame.K_RETURN: #sushi slicer mode
                    key1 = 'ingredients'
                    background = pygame.image.load('sushi/seaweed.jpeg')
                    data = {}
                    for i in range(0, 3):
                        generate_random_ingredients(ingredients[i])
                    waiting = False

# Game Loop
first_round = True
game_over = True        #terminates the game While loop if a bomb/riceglob is sliced or three lives have been lost
game_running = True

#used to manage the game loop
while game_running:
    # easy loop

    while score < 4:
        if game_over:
            if first_round:
                show_gameover_screen()
                first_round = False
            game_over = False
            player_lives = 3
            draw_lives(gameDisplay, 690, 5, player_lives, 'sushi/images/red_lives.png')
            score = 0
        for event in pygame.event.get():
            # checking for closing window
            if event.type == pygame.QUIT:
                game_running = False

        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(score_text, (0, 0))
        draw_lives(gameDisplay, 690, 5, player_lives, 'sushi/images/red_lives.png')

        for key, value in data.items():
            if value['throw']:
                value['x'] += value['speed_x']              #moving the fruits in x-coordinates
                value['y'] += value['speed_y']              #moving the fruits in y-coordinate
                value['speed_y'] += (.75 * value['t'])      #increasing y-coordinate
                value['t'] += 0.9                           #increasing speed_y for next loop

                if value['y'] <= 800:
                    gameDisplay.blit(value['img'], (value['x'], value['y']))    #displaying the fruit inside screen dynamically
                else:
                    #fruit has disappeared at this point
                    if (not value['hit'] and key != 'Riceglob' and key1 == 'ingredients') or (not value['hit'] and key != 'bomb' and key1 == 'fruits'):
                        player_lives -= 1
                        if player_lives == 0:
                            hide_cross_lives(690, 15)
                        elif player_lives == 1 :
                            hide_cross_lives(725, 15)
                        elif player_lives == 2 :
                            hide_cross_lives(760, 15)
                        #if the user misses fruits, GAME OVER message should be displayed and the window should be reset
                        if player_lives < 0 :
                            show_gameover_screen()
                            game_over = True
                            score = 0
                    generate_random_ingredients(key)

                current_position = pygame.mouse.get_pos()   #gets the current coordinate (x, y) in pixels of the mouse

                if not value['hit'] and current_position[0] > value['x']-70 and current_position[0] < value['x']+70 \
                        and current_position[1] > value['y'] -70 and current_position[1] < value['y']+70:

                        #if the user clicks bombs for three time, GAME OVER message should be displayed and the window should be reset
                    if key == 'Riceglob' or key == 'bomb':
                        show_gameover_screen()
                        game_over = True
                        score = 0
                    else:
                        cut_ingredient_path = "sushi/images/cut_" + key + ".png"
                        value['img'] = pygame.image.load(cut_ingredient_path)
                        value['speed_x'] += 10
                        if key != 'Riceglob' or key != 'bomb':
                            if key == 'Tamago':
                                score += 2
                            else:
                                score += 1
                        score_text = font.render('Score : ' + str(score), True, (255, 255, 255))
                        value['hit'] = True
            else:
                generate_random_ingredients(key)

        pygame.display.update()
        clock.tick(FPS) # keep loop running at the right speed (manages the frame/second. The loop should update afer every 1/12th pf the sec

    #medium loop
    data = {}
    if key1 == 'fruits':
        for i in range(0, 5):
            generate_random_ingredients(fruits[i])
    else:
        for i in range(0, 5):
            generate_random_ingredients(ingredients[i])

    game_running = True

    while score >= 4 and score < 10:
        for event in pygame.event.get():
            # checking for closing window
            if event.type == pygame.QUIT:
                game_running = False
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(score_text, (0, 0))
        draw_lives(gameDisplay, 690, 5, player_lives, 'sushi/images/red_lives.png')

        for key, value in data.items():
            if value['throw']:
                value['x'] += value['speed_x']          #moving the fruits in x-coordinates
                value['y'] += value['speed_y']          #moving the fruits in y-coordinate
                value['speed_y'] += (.75 * value['t'])    #increasing y-coordinate
                value['t'] += 0.9                        #increasing speed_y for next loop

                if value['y'] <= 800:
                    gameDisplay.blit(value['img'], (value['x'], value['y']))    #displaying the fruit inside screen dynamically
                else:
                    #fruit has disappeared at this point
                    if (not value['hit'] and key != 'Riceglob' and key1 == 'ingredients') or (not value['hit'] and key != 'bomb' and key1 == 'fruits'):
                        player_lives -= 1
                        if player_lives == 0:
                            hide_cross_lives(690, 15)
                        elif player_lives == 1 :
                            hide_cross_lives(725, 15)
                        elif player_lives == 2 :
                            hide_cross_lives(760, 15)
                        #if the user misses fruits, GAME OVER message should be displayed and the window should be reset
                        if player_lives < 0 :
                            show_gameover_screen()
                            game_over = True
                            score = 0

                    generate_random_ingredients(key)

                current_position = pygame.mouse.get_pos()   #gets the current coordinate (x, y) in pixels of the mouse

                if not value['hit'] and current_position[0] > value['x']-70 and current_position[0] < value['x']+70 \
                        and current_position[1] > value['y'] -70 and current_position[1] < value['y']+70:

                        #if the user clicks bombs for three time, GAME OVER message should be displayed and the window should be reset
                    if key == 'Riceglob' or key == 'bomb':
                        show_gameover_screen()
                        game_over = True
                        score = 0
                    else:
                        cut_ingredient_path = "sushi/images/cut_" + key + ".png"
                        value['img'] = pygame.image.load(cut_ingredient_path)
                        value['speed_x'] += 10

                    if key != 'Riceglob' or key != 'bomb':
                        if key == 'Tamago':
                            score += 2
                        else:
                            score += 1
                    score_text = font.render('Score : ' + str(score), True, (255, 255, 255))
                    value['hit'] = True
            else:
                generate_random_ingredients(key)

        pygame.display.update()
        clock.tick(FPS) # keep loop running at the right speed (manages the frame/second. The loop should update afer every 1/12th pf the sec

    # hard loop
    data = {}
    if key1 == 'fruits':
        for fruit in fruits:
            generate_random_ingredients(fruit)
    else:
        for ingredient in ingredients:
            generate_random_ingredients(ingredient)

    game_running = True
    while score >= 10:
        for event in pygame.event.get():
            # checking for closing window
            if event.type == pygame.QUIT:
                game_running = False
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(score_text, (0, 0))
        draw_lives(gameDisplay, 690, 5, player_lives, 'sushi/images/red_lives.png')

        for key, value in data.items():
            if value['throw']:
                value['x'] += value['speed_x']          #moving the fruits in x-coordinates
                value['y'] += value['speed_y']          #moving the fruits in y-coordinate
                value['speed_y'] += (.75 * value['t'])    #increasing y-coordinate
                value['t'] += 0.9                        #increasing speed_y for next loop

                if value['y'] <= 800:
                    gameDisplay.blit(value['img'], (value['x'], value['y']))    #displaying the fruit inside screen dynamically
                else:
                    #fruit has disappeared at this point
                    if (not value['hit'] and key != 'Riceglob' and key1 == 'ingredients') or (not value['hit'] and key != 'bomb' and key1 == 'fruits'):
                        player_lives -= 1
                        if player_lives == 0:
                            hide_cross_lives(690, 15)
                        elif player_lives == 1 :
                            hide_cross_lives(725, 15)
                        elif player_lives == 2 :
                            hide_cross_lives(760, 15)
                        #if the user misses fruits, GAME OVER message should be displayed and the window should be reset
                        if player_lives < 0 :
                            show_gameover_screen()
                            game_over = True
                            score = 0

                    generate_random_ingredients(key)

                current_position = pygame.mouse.get_pos()   #gets the current coordinate (x, y) in pixels of the mouse

                if not value['hit'] and current_position[0] > value['x']-70 and current_position[0] < value['x']+70 \
                        and current_position[1] > value['y'] -70 and current_position[1] < value['y']+70:

                        #if the user clicks bombs for three time, GAME OVER message should be displayed and the window should be reset
                    if key == 'Riceglob' or key == 'bomb':
                        show_gameover_screen()
                        game_over = True
                        score = 0
                    else:
                        cut_ingredient_path = "sushi/images/cut_" + key + ".png"
                        value['img'] = pygame.image.load(cut_ingredient_path)
                        value['speed_x'] += 10

                    if key != 'Riceglob' or key != 'bomb':
                        if key == 'Tamago':
                            score += 2
                        else:
                            score += 1
                    score_text = font.render('Score : ' + str(score), True, (255, 255, 255))
                    value['hit'] = True
            else:
                generate_random_ingredients(key)

        pygame.display.update()
        clock.tick(FPS)

pygame.quit()

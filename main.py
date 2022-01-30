from helper import *
from objects import *
import os

# Centers the Pygame window on the user's screen
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100)

# Initializes the Pygame module
pygame.init()

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("iQuHack-2022")




loop = True
intro = True
main_menu = False
instructions = False
game = True
over = False
scoreboard = False

score = 500
cube = gate(white, (241, 20), "H")
gates_list = []
gates_list.append(cube)
virus = mob(red, (30, height // 2))
virus.init_virus()
person = mob(green, (1200, height // 2))
textbox = inputbox(60, 650, 140, 32)

'''
def checkForCollision(virus, gate):
    print(virus.pos, " and ", cube.rect.x, cube.rect.y)
    if virus.pos[0] == cube.rect.x and cube.rect.y == 320:
        print("Yes!")
        if gate.type == "H":
            question_text = "Enter qubit no this gate will be applied on:"
            words(question_text,32,white,210,650,gameDisplay)
            hadmad(gatenum, score, textbox)
        if gate.type == "N":
            contnot(gatenum,score)
        if gate.type == "R":
            rotz(gatenum, score)
        if gate.type == "X":
            paulx(gatenum,score)
        if gate.type == "Y":
            pauly(gatenum,score)
        if gate.type == "Z":
            paulz(gatenum,score)
'''
# Main game loop
while loop:
    while intro:
        checkforexit()
        gameDisplay.fill(black)
        words("Welcome!", 83, white, width // 2, height // 2, gameDisplay)
        pygame.display.update()
        pygame.time.delay(1000)
        intro = False
        main_menu = True

    while main_menu:
        checkforexit()
        gameDisplay.fill(black)
        words("iQuHack", 55, white, (width // 2) + 150, (height // 2) - 50, gameDisplay)
        words("a game about quantum gates, made with quantum gates", 25, (100, 100, 100), (width // 2) + 55, (height // 2), gameDisplay)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 510 < mouse[0] < 710 and 500 < mouse[1] < 550:
            drawbutton(white, (510, 500, 200, 50), "Play", black, 20, gameDisplay)
            if click[0] == 1:
                main_menu = False
                game = True
        else:
            drawbutton(black, (510, 500, 200, 50), "Play", white, 20, gameDisplay)

        if 510 < mouse[0] < 710 and 550 < mouse[1] < 600:
            drawbutton(white, (510, 550, 200, 50), "Instructions", black, 20, gameDisplay)
            if click[0] == 1:
                main_menu = False
                instructions = True
        else:
            drawbutton(black, (510, 550, 200, 50), "Instructions", white, 20, gameDisplay)
        pygame.display.update()

    while instructions:
        checkforexit()
        gameDisplay.fill(black)
        words("FIXME: Instructions", 70, white, width // 2, height // 2, gameDisplay)
        pygame.display.update()
        pygame.time.delay(1000)
        instructions = False

    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if textbox.rect.collidepoint(event.pos):
                    # Toggle the active variable.
                    textbox.active = not textbox.active
                else:
                    textbox.active = False
                # Change the current color of the input box.
                textbox.color = white if textbox.active else (255, 0, 0)

                if cube.rect.collidepoint(event.pos):
                    cube.drag = True
                    mouse_x, mouse_y = event.pos
                    cube.offset_x = cube.rect.x - mouse_x
                    cube.offset_y = cube.rect.y - mouse_y
            cube.move(event)
            textbox.handle_event(event)
            textbox.update()

        pygame.time.delay(10)
        clock.tick()
        gameDisplay.fill(black)
        textbox.draw(gameDisplay)
        drawGrid(width, rows, gameDisplay)
        virus.move()
        score_count(20, 90, 20, score, gameDisplay)
        person.draw(gameDisplay)
        virus.draw(gameDisplay)
        cube.draw(gameDisplay)
        if virus.pos == person.pos:
            game = False
        pygame.display.update()
        clock.tick()

    while over:
        checkforexit()
        gameDisplay.fill(black)
        words("Game over!", 70, white, width // 2, height // 2, gameDisplay)
        pygame.display.update()

    loop = False

pygame.quit()
sys.exit()

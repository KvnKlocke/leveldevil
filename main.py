
# Importing modules
import pygame, sys
from settings import *
from level import Level
from button import Button

# pygame setup
pygame.init()
# setup screen and Clock
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TrapdoorTango')
clock = pygame.time.Clock()

# function for getting the font
def getFont(size):
    return pygame.font.Font('assets/font.ttf', size)


def play():
    # creating the level object
    level = Level(screen)

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
        
        screen.fill('#d6d0b8')

        clock.tick(60)

        level.run()
        
        if level.checkForGameOver():
            game_over()

        if level.checkForWin():
            level_ending()
        
        pygame.display.update()

def main_menu():
    while True:
        screen.fill('#0e677d')

        # Getting the Mouse Position in the Title Screen
        menu_mouse_pos = pygame.mouse.get_pos()

        # Setting up the Text for the Title Screen
        menu_text = getFont(80).render('TrapdoorTango', True, '#b68f40')
        menu_rect = menu_text.get_rect(center=(640, 200))

        screen.blit(menu_text, menu_rect)

        # Creating the Button Objects for the Title Screen
        play_button = Button(pos=(640, 400), text_input='PLAY', font=getFont(70), base_color='#b68f40', hovering_color='#e8b754')
        
        quit_button = Button(pos=(640, 550), text_input='QUIT', font=getFont(70), base_color='#b68f40', hovering_color='#e8b754')

        
        # draw buttons on screen and change Color on Hover
        for button in [play_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.draw(screen)
        
        # Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForMouseCollision(menu_mouse_pos):
                    play()
                if quit_button.checkForMouseCollision(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def game_over():
    while True:
        screen.fill('black')

        gameover_text = getFont(80).render('Game Over', True, 'White')
        gameover_rect = gameover_text.get_rect(center=(640, 250))

        continue_text = getFont(30).render('Press Enter To Try Again!', True, 'White')
        continue_rect = continue_text.get_rect(center=(640, 380))

        cancel_text = getFont(30).render('Press ESC To Get To The Title Screen', True, 'White')
        cancel_rect = cancel_text.get_rect(center=(640, 450))

        screen.blit(gameover_text, gameover_rect)
        screen.blit(continue_text, continue_rect)
        screen.blit(cancel_text, cancel_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play()
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        pygame.display.update()

def level_ending():
    while True:
        screen.fill('#0e677d')

        success_text = getFont(50).render('Level 1 Completed', True, 'Green')
        success_rect = success_text.get_rect(center=(640, 250))

        continue_text = getFont(30).render('Press ENTER For The Next Level!', True, 'White')
        continue_rect = continue_text.get_rect(center=(640, 380))

        cancel_text = getFont(30).render('Press ESC To Get To The Title Screen', True, 'White')
        cancel_rect = cancel_text.get_rect(center=(640, 450))

        screen.blit(success_text, success_rect)
        screen.blit(continue_text, continue_rect)
        screen.blit(cancel_text, cancel_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play()
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        pygame.display.update()


main_menu()
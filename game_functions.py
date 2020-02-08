import sys
import pygame

def check_events(ship):
    #Respond to keyboord and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydowm_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydowm_events(event, ship):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_DOWN:
            ship.moving_down = True
        elif event.key == pygame.K_UP:
            ship.moving_up = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False

def update_screen(ai_settings, screen, ship):
    #Update images on the screen and flip to the new screen
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bd_color)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    #Respond to keyboord and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydowm_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydowm_events(event, ai_settings, screen, ship, bullets):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_DOWN:
            ship.moving_down = True
        elif event.key == pygame.K_UP:
            ship.moving_up = True
        elif event.key == pygame.K_SPACE:
            #create a new bullet and add it to the bullets group
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False

def update_screen(ai_settings, screen, ship, bullets):
    #Update images on the screen and flip to the new screen
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bd_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

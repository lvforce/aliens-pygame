import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        #movment flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        #Update the ship's possition based on the movment flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up:
            self.rect.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down:
            self.rect.bottom += self.ai_settings.ship_speed_factor

        #update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        #Draw the ship at its current location.
        self.screen.blit(self.image, self.rect)

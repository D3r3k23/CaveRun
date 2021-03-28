
from Colors   import *
from Player   import Player
from Asteroid import Asteroid
from App      import exit, handle_app_event

import time
import pygame

class Game:
    def __init__(self, screen):
        self.screen    = screen
        self.running   = False
        self.player    = Player(screen)
        self.asteroids = []
        self.score     = 0

    def play(self):
        self.running = True
        prevTime = time.time()

        while self.running:
            newTime = time.time()
            ts = newTime - prevTime
            prevTime = newTime
            
            self.player.move(ts)

            for asteroid in self.asteroids:
                asteroid.move(ts)
            
            self.handle_collisions()

            self.handle_events()
            
            self.draw()

    def draw(self):
        self.screen.fill(BLACK) # Or space background

        for asteroid in self.asteroids:
            asteroid.draw()
        
        self.player.draw()

        # Draw score

        pygame.display.flip()

    def handle_collisions(self):
        if not self.screen.get_rect().colliderect(self.player.rect):
            self.running = False
        
        for asteroid in self.asteroids:
            if asteroid.rect.colliderect(self.player.rect):
                self.running = False
        
    def handle_events(self):
        for event in pygame.event.get():
            if not handle_app_event(event):
                if event.type == pygame.QUIT:
                    # Close application
                    exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    # Return to menu
                    self.running = False

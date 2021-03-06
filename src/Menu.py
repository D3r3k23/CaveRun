
import App
import Screen
import Resources
import Util
import Colors
from Background import Background
from Button import Button
from Text import Text

from time import time
from enum import Enum
import pygame

background = Background(Background.ScrollDir.DOWN, 15)

titleText = Text('Space Run', 'SpaceSquadron', 108, Colors.GREEN, 640, 250, center=True)
playButton = Button('Play', 540, 420)
exitButton = Button('Exit', 740, 420)

class Menu:
    class Choice(Enum):
        NONE = 0
        PLAY = 1
        EXIT = 2
    
    def __init__(self):
        self.running = False
        self.choice  = Menu.Choice.NONE
        
    # Runs the app menu
    def run(self):
        self.running = True
        while self.running:
            for e in pygame.event.get():
                self.handle_event(e)
    
            background.scroll()
            self.render()

        return self.choice

    def render(self):
        background.draw()
        titleText.draw()
        playButton.draw()
        exitButton.draw()

        Screen.display()
        
    def handle_event(self, event):
        if App.handle_event(event):
            return

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.choose_item(Menu.Choice.PLAY)

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = Util.get_mouse_pos()

            if playButton.contains(pos):
                self.choose_item(Menu.Choice.PLAY)

            elif exitButton.contains(pos):
                self.choose_item(Menu.Choice.EXIT)

    def choose_item(self, choice):
        self.choice  = choice
        self.running = False

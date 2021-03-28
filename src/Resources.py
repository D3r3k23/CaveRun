
from Music import Music

import os.path
import pygame

resource_dir = 'resources'

images = {}
sounds = {}
music = Music()

# Loads single image
def load_image(fn):
    dir = os.path.join(resource_dir, 'images')
    fp  = os.path.join(dir, fn)
    try:
        surf = pygame.image.load(fp)
    except (pygame.error, FileNotFoundError):
        raise SystemExit(f'Could not load image: {fp}, {pygame.get_error}')

    return surf.convert_alpha() if surf.get_alpha() else surf.convert()

# Loads single sound
def load_sound(fn):
    dir = os.path.join(resource_dir, 'sounds')
    fp  = os.path.join(dir, fn)
    try:
        sound = pygame.mixer.Sound(fp)
    except (pygame.error, FileNotFoundError):
        raise SystemExit(f'Could not load sound: {fp}, {pygame.get_error}')
    
    return sound

def get_song_path(fn):
    dir = os.path.join(resource_dir, 'music')
    fp  = os.path.join(dir, fn)
    return fp


# Loads all resources
def load():
    images['Start'    ] = load_image('start_button.png')
    images['Exit'     ] = load_image('exit_button.png')
    images['Spaceship'] = load_image('spaceship.png')

    # sounds['PlayerDeath'] = load_sound('explosion1')

    music.add_song(get_song_path('The Prototypes - Pale Blue Dot.mp3'))
    music.add_song(get_song_path('Teddy Killerz - Outer Space.mp3'))
    music.add_song(get_song_path('Phace & Misanthrop - Desert Orgy.mp3'))
    music.add_song(get_song_path('Mefjus & Break - Out Of Time.mp3'))
    music.add_song(get_song_path('Current Value - Dark Rain.mp3'))
    music.add_song(get_song_path('Noisia - Facade.mp3'))
    music.add_song(get_song_path('Fortran - Alien Girl.mp3'))
    music.add_song(get_song_path('Ed Rush & Optical - Mystery Machine.mp3'))
    music.add_song(get_song_path('Ed Rush & Optical - Fixation.mp3'))
    music.add_song(get_song_path('Andy C - Quest (Bladerunner Remix).mp3'))

    music.shuffle()

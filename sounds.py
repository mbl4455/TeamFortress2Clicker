import pygame
pygame.mixer.init()
critical_hit_sound = pygame.mixer.Sound("sounds/sfx/critical-hit-sounds-effect.mp3")
reload = pygame.mixer.Sound("sounds/sfx/AWPRELOAD.mp3")
shot = pygame.mixer.Sound("sounds/sfx/AWPSHOT.mp3")
shotcrit = pygame.mixer.Sound("sounds/sfx/AWPSHOTCRIT.mp3")
scope = pygame.mixer.Sound("sounds/sfx/AWPZOOM.mp3")
reload = pygame.mixer.Sound("sounds/sfx/AWPRELOAD.mp3")
mainmenusoundtrack = pygame.mixer.Sound("sounds/music/MainMenu.mp3")
buttonpress = pygame.mixer.Sound("sounds/sfx/tf2button.mp3")

voicelines = [
    pygame.mixer.Sound("sounds/voicelines/voiceline1.mp3"),
    pygame.mixer.Sound("sounds/voicelines/voiceline2.mp3"),
    pygame.mixer.Sound("sounds/voicelines/voiceline3.mp3"),
    pygame.mixer.Sound("sounds/voicelines/voiceline4.mp3"),
    pygame.mixer.Sound("sounds/voicelines/voiceline5.mp3"),
    pygame.mixer.Sound("sounds/voicelines/voiceline6.mp3"),
    pygame.mixer.Sound("sounds/voicelines/voiceline7.mp3")
]
import pygame
pygame.init()
screensizex = 800
screensizey = 600

screen = pygame.display.set_mode((screensizex, screensizey))
spy_image = pygame.image.load(".\images\spy.png").convert_alpha()
pyro_image = pygame.image.load(".\images\pyro.png").convert_alpha()
heavy_image = pygame.image.load(".\images\heavy.png").convert_alpha()
sniper_image = pygame.image.load(".\images\sniper.png").convert_alpha()
scout_image = pygame.image.load(".\images\scout.png").convert_alpha()
demoman_image = pygame.image.load(".\images\demoman.png").convert_alpha()
medic_image = pygame.image.load(".\images\medic.png").convert_alpha()
main_menu_bg = pygame.image.load(".\images\mainmenubackground.jpeg").convert_alpha()
engineer_image = pygame.image.load(".\images\engineer.png").convert_alpha()
soldier_image = pygame.image.load(".\images\soldier.png").convert_alpha()
original_logo = pygame.image.load(".\images\logo.png").convert_alpha()
gameicon_image = pygame.image.load(".\images\icon.jpeg").convert_alpha()
scope_image = pygame.image.load(".\images\scope.png").convert_alpha()
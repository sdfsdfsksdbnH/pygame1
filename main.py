import pygame, hotkey
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scorres

def start():
    pygame.init()
    screen = pygame.display.set_mode((600, 700))
    pygame.display.set_caption('space defender')
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    hotkey.createarmy(screen, inos)
    stats = Stats()
    sc = Scorres(screen, stats)

    while True:
        hotkey.events(screen, gun, bullets)
        if stats.rungame:
            gun.update_gun()
            hotkey.update(screen, stats, sc, gun, inos, bullets)
            hotkey.updateb(inos, bullets,screen, stats, sc)
            hotkey.updatei(stats, screen, sc, gun, inos, bullets)

start()
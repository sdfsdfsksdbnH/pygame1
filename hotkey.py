import pygame
import sys
from bullet import Bullet
from ino import Ino
import time

def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.mright = True
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            elif event.key == pygame.K_LEFT:
                gun.mleft = False

def update(screen, stats, sc, gun, inos, bullets):
    screen.fill((147,126,187))
    sc.show()
    for bullet in bullets.sprites():
        bullet.draw()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def updateb(inos, bullets, screen, stats, sc):
    bullets.update()
    for i in bullets.copy():
        if i.rect.bottom <= 0:
            bullets.remove()
    col = pygame.sprite.groupcollide(bullets, inos, True, True)
    if col:
        for inos in col.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_score()
    if len(inos) == 0:
        bullets.empty()
        createarmy(screen, inos)

def gun_die(stats, screen, sc,  gun, inos, bullets):
    if stats.gun_left > 0:
        stats.gun_left -= 1

        inos.empty()
        bullets.empty()
        createarmy(screen, inos)
        gun.create_gun()
        time.sleep(2)
    else:
        stats.rungame=False
        sys.exit()

def updatei(stats, screen,sc, gun, inos, bullets):
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_die(stats, screen, sc,  gun, inos, bullets)
    inoscheck(stats, screen, sc, gun, inos, bullets)

def inoscheck(stats, screen, gun,sc, inos, bullets):
    screemn_rect = screen.get_rect()
    for i in inos.sprites():
        if i.rect.bottom >= screemn_rect.bottom:
            gun_die(stats, screen,sc, gun, inos, bullets)
            break

def createarmy(screen, inos):
    ino = Ino(screen)
    ino_w = ino.rect.width
    nix = int((600 - 2 * ino_w) / ino_w)
    ino_h = ino.rect.height
    niy = int((700 - 100 - 2 * ino_h) / ino_h)

    for j in range(niy):
        for i in range(nix):
            ino = Ino(screen)
            ino.x = ino_w + ino_w * i
            ino.y = ino_h + ino_h * j
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * j
            inos.add(ino)

def check_high_score(stats, sc):
    """проверка новых рекордов"""
    if stats.score > stats.record:
        stats.record = stats.score
        sc.imagerc()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.record))
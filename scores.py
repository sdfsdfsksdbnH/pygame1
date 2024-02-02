import pygame.font
from gun import Gun
from pygame.sprite import Group

class Scorres():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = 0,0,0
        self.font = pygame.font.SysFont(None, 20)
        self.image_score()
        self.imagerc()


    def image_score(self):
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (147,126,187))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def imagerc(self):
        self.hs = self.font.render(str(self.stats.record), True, self.text_color,(147,126,187))
        self.high_score_rect = self.hs.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def show(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.hs, self.high_score_rect)

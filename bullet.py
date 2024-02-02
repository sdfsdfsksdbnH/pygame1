import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self,screen,gun):
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,2,13)
        self.color = 12,36,45
        self.speed = 10
        self.rect.centerx=gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= 5
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """外星人类"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # 设置外星人飞船的初始位置在左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)

    def update(self):
        """更新外星人的位置（向右移动外星人）"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x


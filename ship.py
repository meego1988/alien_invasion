import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # 飞船的位置设置在屏幕底部的中间
        self.rect.midbottom = self.screen_rect.midbottom

        # 设置飞船向右移动的标志位
        self.moving_right = False
        # 设置飞船向左移动的标志位
        self.moving_left = False
        # 引入主游戏的settings类
        self.settings = ai_game.settings
        # 因为rect.x只能是int，所以设置一个x属性和ship_speed相加减
        self.x = float(self.rect.x)

    def update(self):
        """更新飞船位置"""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        # rect.x只接收浮点数的整数部分
        self.rect.x = self.x
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
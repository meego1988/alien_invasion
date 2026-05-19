class Settings:
    """alien_invasion游戏的设置类"""
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 设置飞船的移动速度
        self.ship_speed = 1.5
class Settings:
    """alien_invasion游戏的设置类"""
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 设置飞船的移动速度
        self.ship_speed = 3.0

        # 子弹参数设置
        self.bullet_speed = 6.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # 外星人参数设置
        self.alien_speed = 1.0
        self.alien_drop_speed = 10
        # 设置外星人向左右移动的标志（1为向右移动，-1为向左移动）
        self.fleet_direction = 1

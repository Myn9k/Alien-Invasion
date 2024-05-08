

class Settings:
    def __init__(self):
        """Инициализируем статические настройки игры"""
        self.screen_width = 1000
        self.screen_height = 600

        self.Title_Game ="Alien Invasion"
        self.background_image = 'Image/background.jpg'

        # Цвета
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255, 255, 255)
        self.bg_color = self.BLACK

        # Настройки корабля
        self.ship_limit = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 3
        self.bullet_color = self.WHITE

        # Настройки пришельцев
        self.fleet_drop_speed = 10

        # Темп ускорения игры
        self.speedup_scale = 1.1

        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""

        # Настройки скорости
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Направление движения флота пришельцев (1 - вправо, -1 - влево)
        self.fleet_direction = 1

        # Очки за уничтожение одного пришельца
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев при увеличении уровня игры."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        # Увеличение стоимости пришельцев
        self.alien_points = int(self.alien_points * self.score_scale)

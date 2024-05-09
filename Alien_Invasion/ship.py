import pygame.font


class Ship():
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.stats = game.stats
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Загружаем изображение корабля и получаем прямоугольник.
        self.image = pygame.image.load('Image/Ship.png')
        self.original_image = self.image.copy()  # Сохраняем оригинальное изображение корабля
        self.rect = self.image.get_rect()

        # Построение объекта rect корабля и выравнивание по низу экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y = self.screen_rect.y+520
        self.rect.x = self.screen_rect.x+450

        # Сохранение вещественной координаты центра корабля для более точного перемещения.
        self.x = float(self.rect.x)

        # Флаги перемещения корабля.
        self.moving_right = False
        self.moving_left = False

        # Уменьшаем изображение корабля до 25% его исходного размера
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * 0.05), int(self.rect.height * 0.05)))

    def update(self):
        """Обновляем позицию корабля с учетом флагов"""
        # Обновление атрибута x, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right + 1125:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновление атрибута rect на основании self.x.
        self.rect.x = self.x

    def blitme(self):
        """Отображение корабля"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещаем корабль в нижней стороне экрана"""
        self.rect.bottom = self.screen_rect.bottom
        self.x = float(self.rect.x)

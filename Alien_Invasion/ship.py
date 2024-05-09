import pygame.font


class Ship():
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.stats = game.stats
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Загружаем изображение корабля и получаем прямоугольник.
        self.original_image = pygame.image.load('Image/Ship.png')
        self.image = pygame.transform.scale(self.original_image, (int(self.original_image.get_width() * 0.05), int(self.original_image.get_height() * 0.05)))
        self.rect = self.image.get_rect()

        # Построение объекта rect корабля и выравнивание по низу экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля для более точного перемещения.
        self.x = float(self.rect.x)

        # Флаги перемещения корабля.
        self.moving_right = False
        self.moving_left = False

        # Границы для корабля
        self.left_boundary = self.screen_rect.left
        self.right_boundary = self.screen_rect.right

    def update(self):
        """Обновляем позицию корабля с учетом флагов"""
        # Обновление атрибута x, не rect
        if self.moving_right and self.rect.right < self.right_boundary:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.left_boundary:
            self.x -= self.settings.ship_speed

        # Обновление атрибута rect на основании self.x.
        self.rect.x = self.x

    def blitme(self):
        """Отображение корабля"""
        self.screen.blit(self.image, self.rect)

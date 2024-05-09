import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Загрузка изображения пришельца и настройка прямоугольника.
        self.original_image = pygame.image.load('Image/alien.png')
        self.image = pygame.transform.scale(self.original_image, (
        int(self.original_image.get_width() * 0.75), int(self.original_image.get_height() * 0.75)))
        self.rect = self.image.get_rect()


        # Появление пришельца в левом верхнем углу экрана.
        self.rect.x = self.screen.get_rect().left
        self.rect.y = self.screen.get_rect().top
        self.screen_rect = self.screen.get_rect()

        # Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)

        # Границы для прищельца
        self.left_boundary = self.screen_rect.left
        self.right_boundary = self.screen_rect.right

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= self.screen_rect.left:
            return True
        return False

    def update(self):
        """Перемещает пришельца вправо или влево."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

        if self.check_edges():
            # Если пришелец достиг края экрана, меняем направление движения
            self.settings.fleet_direction *= -1

    def blitme(self):
        """Рисует пришельца в текущей позиции."""
        self.screen.blit(self.image, self.rect)

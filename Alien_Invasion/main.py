import sys
import pygame
import settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    def __init__(self):
        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(f"{self.settings.Title_Game}")
        self.BG = pygame.image.load(f'{self.settings.background_image}')
        self.stats = GameStats(self)  # Передача объекта настроек игры в GameStats
        self.sb = Scoreboard(self)
        self.play_button = Button(self, "Play")
        self.ship = Ship(self)
        self.alien = Alien(self)
        self.bullets = pygame.sprite.Group()  # Группа для хранения снарядов

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()  # Обновление позиции корабля
            self.bullets.update()  # Обновление позиции снарядов
            self.alien.update()  # Обновление позиции снарядов
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:  # Если нажата клавиша вправо
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:  # Если нажата клавиша влево
                    self.ship.moving_left = True
                elif event.key == pygame.K_SPACE:  # Если нажата клавиша влево
                    self._fire_bullet()  # Выстрел при нажатии пробела
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:  # Если отпущена клавиша вправо
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:  # Если отпущена клавиша влево
                    self.ship.moving_left = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        # Заполнение экрана изображением
        self.screen.blit(self.BG, (0, 0))  # Отображаем изображение фона
        self.sb.show_score()
        # Отображение корабля
        self.ship.blitme()
        self.alien.blitme()
        # Отображение снарядов
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    Game = AlienInvasion()
    Game.run_game()

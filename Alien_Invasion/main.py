import sys

import pygame
import settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship


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

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()  # Обновление позиции корабля
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
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:  # Если отпущена клавиша вправо
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:  # Если отпущена клавиша влево
                    self.ship.moving_left = False


    def _update_screen(self):
        # Заполнение экрана изображением
        self.screen.blit(self.BG, (0, 0))  # Отображаем изображение
        self.sb.show_score()
        self.play_button.draw_button()
        # Отображение корабля
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    Game = AlienInvasion()
    Game.run_game()

import pygame
import settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button


class AlienInvasion:
    def __init__(self):
        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(f"{self.settings.Title_Game}")
        self.BG = pygame.image.load(f'{self.settings.background_image}')
        self.stats = GameStats(self)  # Передача объекта настроек игры в GameStats
        self.sb = Scoreboard(self)
        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def _update_screen(self):
        # Заполнение экрана изображением
        self.screen.blit(self.BG, (0, 0))  # Отображаем изображение
        self.sb.show_score()
        self.play_button.draw_button()
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    Game = AlienInvasion()
    Game.run_game()

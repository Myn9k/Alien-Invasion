import pygame
import Settings
from game_stats import GameStats


class AlienInvasion:
    def __init__(self):
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption(f"{self.settings.Title_Game}")
        self.BG = pygame.image.load(f'{self.settings.background_image}')
        self.settings = Settings()
        self.stats = GameStats(self)  # Передача объекта настроек игры в GameStats


if __name__ == '__main__':
    pygame.init()
    Game = AlienInvasion()
    Game.run()
    pygame.quit()



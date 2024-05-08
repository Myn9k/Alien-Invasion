import pygame
import settings
from game_stats import GameStats


class AlienInvasion:
    def __init__(self):
        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(f"{self.settings.Title_Game}")
        self.BG = pygame.image.load(f'{self.settings.background_image}')
        self.stats = GameStats(self)  # Передача объекта настроек игры в GameStats

    def run(self):
        """Запуск основного игрового цикла."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Заполнение экрана изображением
            self.screen.blit(self.BG, (0, 0))  # Отображаем изображение BG в координатах (0, 0)

            # Отрисовка других элементов игры

            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    pygame.init()
    Game = AlienInvasion()
    Game.run()
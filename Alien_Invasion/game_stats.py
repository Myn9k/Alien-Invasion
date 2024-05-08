class GameStats:
    """Класс для отслеживания статистики в игре Alien Invasion."""

    def __init__(self, game):
        """Инициализируем статистику."""
        self.settings = game.settings
        self.reset_stats()

        # Игра начинается в неактивном состоянии
        self.game_active = False

        # Рекордный результат не должен сбрасываться
        self.high_score = 0

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
import pygame.font
from pygame.sprite import Group, Sprite


class Heart(Sprite):
    def __init__(self, screen, x, y):
        #Python автоматически определяет родительский класс и вызывает его метод __init__()
        super().__init__()
        self.image = pygame.image.load('Image/Heart.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Scoreboard:
    def __init__(self, game):
        """Инициализируем статические настройки игры"""
        self.game = game
        self.settings = game.settings
        self.stats = game.stats
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Настройки текста
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 40)

        # Подготовка изображений счета, рекордного счета, уровня и кораблей
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        # Вывод счета в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Выводит текущий счет, рекордный счет, уровень и количество оставшихся кораблей на экран."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        # Рекордный счет выравнивается по центру верхней стороны экрана
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Проверяет, появился ли новый рекорд."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Преобразует уровень в графическое изображение."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        # Уровень выравнивается под текущим счетом на экране
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Подготавливает изображения жизней и отображает их на экране.
        heart_spacing устанавливает расстояние между сердечками.
        total_widthвычисляет общую ширину, занимаемую сердцами, и расстояние между ними.
        start_xопределяет стартовую позицию для первого сердца на основе общей ширины.
Каждое сердце позиционируется с помощью start_x + life_number * (heart_width + heart_spacing), обеспечивая их расположение рядом с нужным расстоянием.
self.screen_rect.bottom - 100 высота сердце(Y координата)"""
        self.ships = Group()  # Создаем группу для хранения изображений жизней
        heart_spacing = -300
        heart_width = Heart(self.screen, 0, 0).rect.width
        total_width = heart_width * self.stats.ships_left + heart_spacing * (self.stats.ships_left - 1)
        start_x = (self.screen_rect.width - total_width) * 1.5
        for life_number in range(self.stats.ships_left):
            heart = Heart(self.screen, start_x + life_number * (heart_width + heart_spacing), self.screen_rect.bottom - 100)
            heart.image = pygame.transform.scale(heart.image,(int(heart.rect.width * 0.15), int(heart.rect.height * 0.15)))
            self.ships.add(heart)


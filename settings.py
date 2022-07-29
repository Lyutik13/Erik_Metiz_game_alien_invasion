class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 1600
        self.screen_heigh = 900
        self.bg_color = (51, 140, 229)

        # Настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 1

        # Параметры снаряда
        self.bullet_speed = 1.5
        self.bullet_width = 2.8
        self.bullet_height = 25
        self.bullet_color = (211,211,211)
        self.bullets_allowed = 3

        # Настройки пришельцев
        # self.alien_speed = 0.6
        self.fleet_drop_speed = 25
        # # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        # self.fleet_direction = 0.6

        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        # Подсчет очков
        self.alien_points = 50

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        # self.ship_speed = 1.5
        # self.bullet_speed = 1.5
        self.alien_speed = 0.5

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 0.6

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        # self.ship_speed *= self.speedup_scale
        # self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)

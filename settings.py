class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
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
        self.alien_speed = 0.6
        self.fleet_drop_speed = 25
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 0.6

        # Подсчет очков
        self.alien_points = 50
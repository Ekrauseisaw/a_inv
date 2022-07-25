import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from star import Star
from game_stats import GameStats
from button import Button


def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание экземпляра для хранения игровой статистики.
    stats = GameStats(ai_settings)

    # Создание корабля.
    ship = Ship(ai_settings, screen)

    # Создание группы для хранения пуль.
    bullets = Group()

    # Создание пришельца и группы пришельцев
    alien = Alien(ai_settings, screen)
    aliens = Group()

    # Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # Создание звезды и группы звезд
    star = Star(ai_settings, screen)
    stars = Group()

    # Создание звездного неба
    gf.create_stars_sky(ai_settings, screen, stars)

    # Создание кнопки play
    #play_button = Button(ai_settings, screen, "Play")

    # Запуск основного цикла игры.
    while True:
        # Вызываем модуль с функциями
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, stats, ship, aliens, stars, bullets)


run_game()

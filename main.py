import random
from os import listdir
from os.path import isfile, join

import pygame
import pygame_gui
import pygame_widgets

import navigation_bar
import menu_ui
import gamelogic.network
import army_ui
import save_ui
import town_ui
import journal_ui
import storage_ui
import settings_ui
import world_ui
import workers_ui
import gamelogic.game
import gamelogic.config
from gamelogic.config import *


def insert_into_playlist(pl, music_file):
    pl.append(music_file)


class Start:
    def __init__(self, net):
        pygame.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        self.is_running = True
        self.network = net
        self.window_surface = pygame.display.set_mode((800, 600))
        self.background = pygame.Surface((800, 600))
        self.background.fill(pygame.Color(43, 43, 43))
        pygame.display.set_caption("Build on field")
        self.manager = pygame_gui.UIManager(pygame.display.get_window_size(), 'theme.json')
        icon = pygame.image.load('img/f5.png')
        pygame.display.set_icon(icon)
        self.game = gamelogic.game.Game(self.background)
        menu = menu_ui.Menu(self.manager, self.background, self.window_surface, self.network)
        menu.hide_all_menu()
        del menu
        music = ['music/' + g for g in listdir("music") if isfile(join("music", g)) and g.endswith('.mp3' or '.wav')]
        random.shuffle(music)
        self.playlist = music
        self.playlist_original = music.copy()
        pygame.mixer.music.load(self.playlist[0])
        self.playlist.pop(0)
        pygame.mixer.music.play()
        pygame.mixer.music.queue(self.playlist[0])
        self.playlist.pop(0)
        pygame.mixer.music.set_volume(gamelogic.config.VOLUME)
        pygame.mixer.music.set_endevent(pygame.K_PAUSE)

        self.town = town_ui.Town(self.manager, self.background, self.game, self)
        self.army = army_ui.Army(self.manager, self.background, self.game)
        self.journal = journal_ui.Journal(self.manager, self.background)
        self.settings = settings_ui.Settings(self.manager, self.background, False)
        self.storage = storage_ui.Storage(self.manager, self.background, self.game)
        self.workers = workers_ui.Workers(self.manager, self.background, self.game)
        self.world = world_ui.World(self.manager, self.background, self.game)
        self.save = save_ui.Save(self.manager, self.background, False)
        self.navigation = navigation_bar.NavigationBar(self.manager)
        self.navigation.hide_all_navigation()
        self.hide_all()

    def start(self):
        self.navigation.show_all_navigation()
        self.town.show_side_buttons()
        self.navigation.town.disable()
        self.game.new()
        while self.is_running:
            pygame.mixer.music.set_volume(gamelogic.config.VOLUME)
            if not pygame.mixer.music.get_busy():
                self.playlist = self.playlist_original.copy()
                pygame.mixer.music.load(self.playlist[0])
                self.playlist.pop(0)
                pygame.mixer.music.play()
                pygame.mixer.music.queue(self.playlist[0])
                self.playlist.pop(0)
            if self.game.save_data.check_cooldown():
                self.game.save_data.save(self.game)

            time_delta = self.navigation.clock.tick(FPS) / 1000.0
            if not self.town.details.is_enabled or self.town.details.pressed:
                self.town.details.disable()
                self.navigation.enable_all_navigation()
                self.town.stop_build()
                self.game.delete_places()
                self.hide_all()
                self.town.show_details()
            if not self.navigation.journal.is_enabled:
                self.town.stop_build()
                self.game.delete_places()
                self.hide_all()
                self.journal.show_all_journal()
                self.journal.start()
            elif not self.navigation.army.is_enabled:
                self.town.stop_build()
                self.hide_all()
                self.army.show_all_army()
                self.army.start()
            elif not self.navigation.town.is_enabled:
                self.hide_all()
                self.town.show_side_buttons()
                self.town.start()
                self.game.draw()
            elif not self.navigation.world.is_enabled:
                self.town.stop_build()
                self.hide_all()
                self.world.show_all_world()
                self.world.start()
            elif not self.navigation.storage.is_enabled:
                self.town.stop_build()
                self.hide_all()
                self.storage.show_all_storage()
                self.storage.start()
            elif not self.navigation.workers.is_enabled:
                self.town.stop_build()
                self.hide_all()
                self.workers.show_all_workers()
                self.workers.start()
            elif not self.navigation.settings.is_enabled:
                self.town.stop_build()
                self.hide_all()
                self.settings.show_all_settings()
                self.settings.start()
            elif not self.navigation.save.is_enabled:
                self.town.stop_build()
                self.hide_all()
                self.save.show_all_save()
                self.save.start()
            if self.navigation.town.pressed:
                self.navigation.enable_all_navigation()
                self.navigation.town.disable()
            elif self.navigation.journal.pressed:
                self.navigation.enable_all_navigation()
                self.navigation.journal.disable()
            elif self.navigation.storage.pressed:
                self.navigation.enable_all_navigation()
                self.navigation.storage.disable()
            elif self.navigation.workers.pressed:
                self.navigation.enable_all_navigation()
                self.navigation.workers.disable()
            elif self.navigation.army.pressed:
                self.navigation.enable_all_navigation()
                self.navigation.army.disable()
            elif self.navigation.world.pressed:
                self.navigation.enable_all_navigation()
                self.navigation.world.disable()
            elif self.navigation.settings.pressed:
                self.navigation.enable_all_navigation()
                self.navigation.settings.disable()
            elif self.navigation.save.pressed:
                self.navigation.enable_all_navigation()
                self.navigation.save.disable()
            elif self.navigation.exit.pressed:
                self.game.save_data.save(self.game)
                self.is_running = False
            for event in pygame.event.get():

                if event.type == pygame.K_PAUSE:
                    if len(self.playlist) > 0:
                        print(self.playlist)
                        pygame.mixer.music.queue(self.playlist[0])
                        self.playlist.pop(0)
                    else:
                        self.playlist = self.playlist_original.copy()
                        pygame.mixer.music.queue(self.playlist[0])
                        self.playlist.pop(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and not self.town.house.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[HOUSE])
                    elif event.button == 1 and not self.town.gold_mine.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[GOLD_MINE])
                    elif event.button == 1 and not self.town.stone_mine.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[STONE_MINE])
                    elif event.button == 1 and not self.town.iron_mine.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[IRON_MINE])
                    elif event.button == 1 and not self.town.sawmill.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[SAWMILL])
                    elif event.button == 1 and not self.town.storage.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[STORAGE])
                    elif event.button == 1 and not self.town.fishing.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[FISHERMAN])
                    elif event.button == 1 and not self.town.wheat_field.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[WHEAT_FIELD])
                    elif event.button == 1 and not self.town.mill.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[MILL])
                    elif event.button == 1 and not self.town.bakery.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[BAKERY])
                    elif event.button == 1 and not self.town.hunting.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[HUNTER])
                    elif event.button == 1 and not self.town.blacksmith.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[BLACKSMITH])
                    elif event.button == 1 and not self.town.gunsmith.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[GUNSMITH])
                    elif event.button == 1 and not self.town.barracks.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[BARRACKS])
                    elif event.button == 1 and not self.town.shipyard.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[SHIPYARD])
                    elif event.button == 1 and not self.town.tailor.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[TAILOR])
                    elif event.button == 1 and not self.town.iron_melt.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[IRON_MELT])
                    elif event.button == 1 and not self.town.gold_melt.is_enabled:
                        x = event.pos[0] // TILESIZE
                        y = event.pos[1] // TILESIZE
                        self.game.build_building(x, y, BUILDINGS[GOLD_MELT])
                if event.type == pygame.QUIT:
                    self.game.save_data.save(self.game)
                    menu_ui.set_username('Not logged in')
                    exit()

                self.manager.process_events(event)
                pygame_widgets.update(event)
            self.game.update()
            self.manager.update(time_delta)
            self.window_surface.blit(self.background, (0, 0))
            self.manager.draw_ui(self.window_surface)
            pygame.display.update()

    def hide_all(self):
        self.town.hide_all_town()
        self.army.hide_all_army()
        self.journal.hide_all_journal()
        self.settings.hide_all_settings()
        self.storage.hide_all_storage()
        self.workers.hide_all_workers()
        self.world.hide_all_world()
        self.save.hide_all_save()


network = gamelogic.network.Network()
while True:
    a = Start(network)
    a.start()
    del a

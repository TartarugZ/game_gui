import pygame
from pygame_widgets.progressbar import ProgressBar
import navigation_bar
import pygame_widgets


class Storage:
    def __init__(self, manager, background):
        self.manager = manager
        self.background = background
        self.population = 0
        self.storage = 1
        self.storage_max = self.storage * 1000
        self.wood = 1000
        self.gold = 0
        self.stone = 500
        self.iron = 0
        self.iron_ore = 0
        self.gold_ore = 0
        self.fish = 0
        self.wheat = 0
        self.flour = 0
        self.bread = 0
        self.meat = 0
        self.skin = 0
        self.armor = 0
        self.weapon = 0
        self.clothes = 0

        self.wood_check = 0
        self.gold_check = 0
        self.stone_check = 0
        self.iron_check = 0
        self.iron_ore_check = 0
        self.gold_ore_check = 0
        self.fish_check = 0
        self.wheat_check = 0
        self.flour_check = 0
        self.meat_check = 0
        self.skin_check = 0
        self.armor_check = 0
        self.weapon_check = 0
        self.clothes_check = 0
        self.bread_check = 0
        self.all_storage = []
        self.text_needed = True

        self.wood_bar = ProgressBar(self.background,
                                    130, 100, 100, 40,
                                    lambda: self.wood / self.storage_max)
        self.gold_ore_bar = ProgressBar(self.background,
                                        130, 150, 100, 40,
                                        lambda: self.gold_ore / self.storage_max)
        self.stone_bar = ProgressBar(self.background,
                                     130, 200, 100, 40,
                                     lambda: self.stone / self.storage_max)
        self.iron_ore_bar = ProgressBar(self.background,
                                        130, 250, 100, 40,
                                        lambda: self.iron_ore / self.storage_max)
        self.fish_bar = ProgressBar(self.background,
                                    130, 300, 100, 40,
                                    lambda: self.fish / self.storage_max)
        self.wheat_bar = ProgressBar(self.background,
                                     130, 350, 100, 40,
                                     lambda: self.wheat / self.storage_max)
        self.flour_bar = ProgressBar(self.background,
                                     130, 400, 100, 40,
                                     lambda: self.flour / self.storage_max)
        self.meat_bar = ProgressBar(self.background,
                                    130, 450, 100, 40,
                                    lambda: self.meat / self.storage_max)
        self.skin_bar = ProgressBar(self.background,
                                    380, 100, 100, 40,
                                    lambda: self.skin / self.storage_max)
        self.armor_bar = ProgressBar(self.background,
                                     380, 150, 100, 40,
                                     lambda: self.armor / self.storage_max)
        self.weapon_bar = ProgressBar(self.background,
                                      380, 200, 100, 40,
                                      lambda: self.weapon / self.storage_max)
        self.clothes_bar = ProgressBar(self.background,
                                       380, 250, 100, 40,
                                       lambda: self.clothes / self.storage_max)
        self.bread_bar = ProgressBar(self.background,
                                     380, 300, 100, 40,
                                     lambda: self.bread / self.storage_max)
        self.gold_bar = ProgressBar(self.background,
                                    380, 350, 100, 40,
                                    lambda: self.gold / self.storage_max)
        self.iron_bar = ProgressBar(self.background,
                                    380, 400, 100, 40,
                                    lambda: self.iron / self.storage_max)
        self.all_storage.append(self.iron_bar)
        self.all_storage.append(self.gold_bar)
        self.all_storage.append(self.bread_bar)
        self.all_storage.append(self.clothes_bar)
        self.all_storage.append(self.weapon_bar)
        self.all_storage.append(self.armor_bar)
        self.all_storage.append(self.skin_bar)
        self.all_storage.append(self.meat_bar)
        self.all_storage.append(self.flour_bar)
        self.all_storage.append(self.wheat_bar)
        self.all_storage.append(self.fish_bar)
        self.all_storage.append(self.iron_ore_bar)
        self.all_storage.append(self.gold_ore_bar)
        self.all_storage.append(self.stone_bar)
        self.all_storage.append(self.wood_bar)

        # start_time = time.time()
        # a = (time.time() - start_time) / 20
        # test = ProgressBar(self.background,
        #                    380, 450, 100, 40,
        #                    lambda: 0 + (time.time() - start_time) / 20)

    def start(self):
        if self.wood < self.wood_check:
            self.wood_bar.completedColour = "#e61919"
        elif self.wood > self.wood_check:
            self.wood_bar.completedColour = "#0d730d"
        else:
            self.wood_bar.completedColour = "#e5e619"

        if self.gold < self.gold_check:
            self.gold_bar.completedColour = "#e61919"
        elif self.wood > self.wood_check:
            self.gold_bar.completedColour = "#0d730d"
        else:
            self.gold_bar.completedColour = "#e5e619"

        if self.stone < self.stone_check:
            self.stone_bar.completedColour = "#e61919"
        elif self.stone > self.stone_check:
            self.stone_bar.completedColour = "#0d730d"
        else:
            self.stone_bar.completedColour = "#e5e619"

        if self.iron < self.iron_check:
            self.iron_bar.completedColour = "#e61919"
        elif self.iron > self.iron_check:
            self.iron_bar.completedColour = "#0d730d"
        else:
            self.iron_bar.completedColour = "#e5e619"

        if self.gold_ore < self.gold_ore_check:
            self.gold_ore_bar.completedColour = "#e61919"
        elif self.gold_ore > self.gold_ore_check:
            self.gold_ore_bar.completedColour = "#0d730d"
        else:
            self.gold_ore_bar.completedColour = "#e5e619"

        if self.iron_ore < self.iron_ore:
            self.iron_ore_bar.completedColour = "#e61919"
        elif self.iron_ore > self.iron_ore:
            self.iron_ore_bar.completedColour = "#0d730d"
        else:
            self.iron_ore_bar.completedColour = "#e5e619"

        if self.fish < self.fish_check:
            self.fish_bar.completedColour = "#e61919"
        elif self.fish > self.fish_check:
            self.fish_bar.completedColour = "#0d730d"
        else:
            self.fish_bar.completedColour = "#e5e619"

        if self.wheat < self.wheat_check:
            self.wheat_bar.completedColour = "#e61919"
        elif self.wheat > self.wheat_check:
            self.wheat_bar.completedColour = "#0d730d"
        else:
            self.wheat_bar.completedColour = "#e5e619"

        if self.flour < self.flour_check:
            self.flour_bar.completedColour = "#e61919"
        elif self.flour > self.flour_check:
            self.flour_bar.completedColour = "#0d730d"
        else:
            self.flour_bar.completedColour = "#e5e619"

        if self.bread < self.bread_check:
            self.bread_bar.completedColour = "#e61919"
        elif self.bread > self.bread_check:
            self.bread_bar.completedColour = "#0d730d"
        else:
            self.bread_bar.completedColour = "#e5e619"

        if self.meat < self.meat_check:
            self.meat_bar.completedColour = "#e61919"
        elif self.meat > self.meat_check:
            self.meat_bar.completedColour = "#0d730d"
        else:
            self.meat_bar.completedColour = "#e5e619"

        if self.skin < self.skin_check:
            self.skin_bar.completedColour = "#e61919"
        elif self.skin > self.skin_check:
            self.skin_bar.completedColour = "#0d730d"
        else:
            self.skin_bar.completedColour = "#e5e619"

        if self.armor < self.armor_check:
            self.armor_bar.completedColour = "#e61919"
        elif self.armor > self.armor_check:
            self.armor_bar.completedColour = "#0d730d"
        else:
            self.armor_bar.completedColour = "#e5e619"

        if self.weapon < self.weapon_check:
            self.weapon_bar.completedColour = "#e61919"
        elif self.weapon > self.weapon_check:
            self.weapon_bar.completedColour = "#0d730d"
        else:
            self.weapon_bar.completedColour = "#e5e619"

        if self.clothes < self.clothes_check:
            self.clothes_bar.completedColour = "#e61919"
        elif self.clothes > self.clothes_check:
            self.clothes_bar.completedColour = "#0d730d"
        else:
            self.clothes_bar.completedColour = "#e5e619"

        self.background.fill(pygame.Color(43, 43, 43))
        if self.text_needed:
            navigation_bar.draw_text(self.background, f'Wood {self.wood} / {self.storage_max}',
                                     15, 55, 115)
            navigation_bar.draw_text(self.background, f'Gold ore {self.gold} / {self.storage_max}',
                                     15, 55, 165)
            navigation_bar.draw_text(self.background, f'Stone {self.stone} / {self.storage_max}',
                                     15, 55, 215)
            navigation_bar.draw_text(self.background, f'Iron ore {self.iron} / {self.storage_max}',
                                     15, 55, 265)
            navigation_bar.draw_text(self.background, f'Fish {self.fish} / {self.storage_max}',
                                     15, 55, 315)
            navigation_bar.draw_text(self.background, f'Wheat {self.wheat} / {self.storage_max}',
                                     15, 55, 365)
            navigation_bar.draw_text(self.background, f'Flour {self.flour} / {self.storage_max}',
                                     15, 55, 415)
            navigation_bar.draw_text(self.background, f'Meat {self.meat} / {self.storage_max}',
                                     15, 55, 465)
            navigation_bar.draw_text(self.background, f'Skin {self.skin} / {self.storage_max}',
                                     15, 300, 115)
            navigation_bar.draw_text(self.background, f'Armor {self.armor} / {self.storage_max}',
                                     15, 300, 165)
            navigation_bar.draw_text(self.background, f'Weapon {self.weapon} / {self.storage_max}',
                                     15, 300, 215)
            navigation_bar.draw_text(self.background, f'Clothes {self.clothes} / {self.storage_max}',
                                     15, 300, 265)
            navigation_bar.draw_text(self.background, f'Bread {self.bread} / {self.storage_max}',
                                     15, 300, 315)
            navigation_bar.draw_text(self.background, f'Gold {self.gold} / {self.storage_max}',
                                     15, 300, 365)
            navigation_bar.draw_text(self.background, f'Iron {self.iron} / {self.storage_max}',
                                     15, 300, 415)
            navigation_bar.draw_text(self.background, f'Population {self.population}',
                                     20, 700, 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            self.manager.process_events(event)

        self.wood_check = self.wood
        self.gold_check = self.gold
        self.stone_check = self.stone
        self.iron_check = self.iron
        self.iron_ore_check = self.iron_ore
        self.gold_ore_check = self.gold_ore
        self.fish_check = self.fish
        self.wheat_check = self.wheat
        self.flour_check = self.flour
        self.meat_check = self.meat
        self.skin_check = self.skin
        self.armor_check = self.armor
        self.weapon_check = self.weapon
        self.clothes_check = self.clothes
        self.bread_check = self.bread
        self.bread += 1
        self.wood -= 1
        pygame_widgets.update(pygame.event.get())

    def hide_all_storage(self):
        self.background.fill(pygame.Color(43, 43, 43))
        self.text_needed = False
        for element in self.all_storage:
            element.hide()

    def show_all_storage(self):
        self.text_needed = True
        for element in self.all_storage:
            element.show()

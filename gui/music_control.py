import random
from os import listdir
from os.path import isfile, join

import pygame
import gamelogic.config


class Music:
    def __init__(self):
        pygame.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        music = ['./resources/music/' + g for g in listdir("./resources/music") if
                 isfile(join("./resources/music", g)) and g.endswith('.mp3' or '.wav')]
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

    def music_check(self):
        if not pygame.mixer.music.get_busy():
            self.playlist = self.playlist_original.copy()
            random.shuffle(self.playlist)
            pygame.mixer.music.load(self.playlist[0])
            self.playlist.pop(0)
            pygame.mixer.music.play()
            pygame.mixer.music.queue(self.playlist[0])
            self.playlist.pop(0)

    def music_playlist(self, event):
        if event.type == pygame.K_PAUSE:
            if len(self.playlist) > 0:
                print(self.playlist)
                pygame.mixer.music.queue(self.playlist[0])
                self.playlist.pop(0)
            else:
                self.playlist = self.playlist_original.copy()
                pygame.mixer.music.queue(self.playlist[0])
                self.playlist.pop(0)

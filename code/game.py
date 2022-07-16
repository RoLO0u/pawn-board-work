import pygame
import sys
from code.map import Map
from code.player import Player

class Game:

    def __init__(self, settings: dict) -> None:

        pygame.init()
        
        self.FPS = settings["FPS"]
        self.TILE_SIZE = settings["TILE_SIZE"]
        
        self.screen = pygame.display.set_mode(settings["WINDOW_SIZE"])
        pygame.display.set_caption("Roll to die")

        self.clock = pygame.time.Clock()
        self.game = True
        self.is_active = False

        self.map = Map(settings["paths"], self.TILE_SIZE, settings["ORIGINAL_TILE_SIZE"])
        self.player = pygame.sprite.GroupSingle( Player((64, 64), self.TILE_SIZE) )

        self.bg_music = pygame.mixer.Sound("sounds/CaveLoop.wav")
        self.bg_music.set_volume(0.5)
        self.bg_music.play(loops = -1)

    def run(self):

        while self.game:

            self.screen.fill("black")

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if self.is_active:
                    pass
                
                else:

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_SPACE:

                            self.is_active = True
                
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            if self.is_active:

                for group in self.map.bg_groups + self.map.fg_groups:
                    group.draw(self.screen)
                self.player.update(self.map.fg_groups)
                self.player.draw(self.screen)

                # Update screen
                pygame.display.update()

                # Set game framerate (FPS)
                self.clock.tick(self.FPS)
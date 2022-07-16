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

        self.map = Map('map/map01_floor.csv', self.TILE_SIZE, settings["ORIGINAL_TILE_SIZE"])
        self.player = pygame.sprite.GroupSingle( Player((32, 32), self.TILE_SIZE) )

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

            if self.is_active:

                self.map.terrain_sprites.draw(self.screen)
                self.map.wall_sprites.draw(self.screen)
                self.player.update()
                self.player.draw(self.screen)

                # Update screen
                pygame.display.update()

                # Set game framerate (FPS)
                self.clock.tick(self.FPS)
import pygame
import sys
from code.map import Map
from code.player import Player

class Game:

    def __init__(self, settings: dict) -> None:

        pygame.init()
        
        self.FPS = settings["FPS"]
        self.TILE_SIZE = settings["TILE_SIZE"]
        self.settings = settings
        
        self.screen = pygame.display.set_mode(settings["WINDOW_SIZE"])
        pygame.display.set_caption("Roll to die")
        pygame.display.set_icon(pygame.image.load(r"images\player_stand.png", "icon"))

        self.clock = pygame.time.Clock()
        self.game = True
        self.is_active = False

        self.map = Map(settings["paths"], self.TILE_SIZE, settings["ORIGINAL_TILE_SIZE"])
        self.player = pygame.sprite.GroupSingle( Player((64, 64), self.TILE_SIZE) )

        self.bg_image = pygame.image.load("images/bg_image.png")

        self.bg_music = pygame.mixer.Sound("sounds/CaveLoop.wav")
        self.bg_music.set_volume(0.5)
        self.bg_music.play(loops = -1)

    def restart_game(self):
        self.map = Map(self.settings["paths"], self.TILE_SIZE, self.settings["ORIGINAL_TILE_SIZE"])
        self.player = pygame.sprite.GroupSingle( Player((64, 64), self.TILE_SIZE) )

        self.game = True
        self.is_active = False

    def win_game(self):
        
        print(f"Here you win")
        self.restart_game()

    def run(self):

        while self.game:

            self.screen.blit(self.bg_image, (0, 0))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if self.is_active:
                    pass
                    # I will do something here (maybe)
                
                else:

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_SPACE:

                            self.is_active = True
                
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    if event.key == pygame.K_r:

                        self.restart_game()

            if self.is_active:

                self.player.update(self.map.fg_groups)
                self.map.fg_groups[1].update(self.map.fg_groups[0:1])
                self.map.bg_groups[1].update(self.map.fg_groups[1].sprites()[0].rect.center)
                
                if self.map.bg_groups[1].sprites()[0].end_game:

                    self.win_game()

                for group in self.map.bg_groups + self.map.fg_groups:
                    group.draw(self.screen)                
                self.player.draw(self.screen)

            # Update screen
            pygame.display.update()

            # Set game framerate (FPS)
            self.clock.tick(self.FPS)
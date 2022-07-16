import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, cords: tuple|list, TILE_SIZE: tuple|list) -> None:
        super().__init__()

        self.frames = [pygame.image.load(r"images\player_stand.png")]

        self.frames = [pygame.transform.scale(image.convert_alpha(), TILE_SIZE) for image in self.frames]

        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=cords)

        self.TILE_SIZE = TILE_SIZE
        self.speed = 5

        self.facing = pygame.Vector2()

    def get_input(self) -> None:

        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_LEFT]:
            self.facing.x = -1
            self.image = self.frames[0]
        elif self.keys[pygame.K_RIGHT]:
            self.facing.x = 1
            self.image = self.frames[0]
        else: self.facing.x = 0
        if self.keys[pygame.K_UP]:
            self.facing.y = -1
            self.image = self.frames[0]
        elif self.keys[pygame.K_DOWN]:
            self.facing.y = 1
            self.image = self.frames[0]
        else: self.facing.y = 0

    def move(self) -> None:

        if self.facing.magnitude() != 0:
            self.facing = self.facing.normalize()

        self.rect.x += self.facing.x * self.speed
        self.rect.y += self.facing.y * self.speed

    # def check_collisions(self, collide_group: pygame.sprite.Group) -> None:

    #     for colliding_rect in collide_group.sprites():
    #         if self.rect.colliderect(colliding_rect):
    #             self.facing.xy = 0, 0

    def update(self) -> None:
        
        self.get_input()
        # self.check_collisions(collide_group)
        self.move()
import pygame

from engine import Engine
from map import Map
from aabb import AABB
from input_handler import InputHandler

from config import load_config

class TopViewGame(Engine):
    def __init__(self, config):
        super().__init__(config)
        self.tile_size = config['tile_size']
        self.map = Map(config)

    def on_start(self):
        self.player_rect = AABB(100, 100, 10, 10)
        self.enemy_rect = AABB(150, 150, 10, 10)

    def on_update(self):
        keys = InputHandler.get_keys()

        if keys[pygame.K_w]:
            self.player_rect.y -= 5
        if keys[pygame.K_s]:
            self.player_rect.y += 5
        if keys[pygame.K_a]:
            self.player_rect.x -= 5
        if keys[pygame.K_d]:
            self.player_rect.x += 5

        self.check_collision_with_map()

        if self.player_rect.intersects(self.enemy_rect):
            print("Collision with enemy!")
        
    def check_collision_with_map(self):
        for y in range(len(self.map.tiles)):
            for x in range(len(self.map.tiles[0])):
                if self.map.is_wall(x, y):
                    tile_rect = AABB(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                    if self.player_rect.intersects(tile_rect):
                        overlap_x = min(self.player_rect.x + self.player_rect.width, tile_rect.x + tile_rect.width) - max(self.player_rect.x, tile_rect.x)
                        overlap_y = min(self.player_rect.y + self.player_rect.height, tile_rect.y + tile_rect.height) - max(self.player_rect.y, tile_rect.y)

                        if overlap_x < overlap_y:
                            if self.player_rect.x < tile_rect.x:
                                self.player_rect.x -= overlap_x
                            else:
                                self.player_rect.x += overlap_x
                        else:
                            if self.player_rect.y < tile_rect.y:
                                self.player_rect.y -= overlap_y
                            else:
                                self.player_rect.y += overlap_y

    def on_draw(self):
        self.draw_map()
        self.draw_entities()

    def draw_map(self):
        for y in range(self.map.height):
            for x in range(self.map.width):
                if self.map.is_wall(x, y):
                    rect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                    pygame.draw.rect(self.screen, (0, 255, 0), rect)

    def draw_entities(self):
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.player_rect.x, self.player_rect.y, self.player_rect.width, self.player_rect.height))
        pygame.draw.rect(self.screen, (0, 255, 0),
                         (self.enemy_rect.x, self.enemy_rect.y, self.enemy_rect.width, self.enemy_rect.height))

if __name__ == "__main__":
    config = load_config('config.json')
    game = TopViewGame(config)
    game.start()
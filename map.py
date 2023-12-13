class Map:
    def __init__(self, config):
        self.tile_size = config['tile_size']
        self.tiles = config['map']
        self.width = len(self.tiles[0])
        self.height = len(self.tiles)

    def is_wall(self, x, y):
        return self.tiles[y][x] == 1

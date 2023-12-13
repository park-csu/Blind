import pygame
import sys

class Engine:
    def __init__(self, config):
        pygame.init()
        self.width = config['screen']['width']
        self.height = config['screen']['height']
        self.title = config['screen']['title']
        self.fps = config['screen']['fps']

        # Pygame setup
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()

        # Game state
        self.running = False

        # Event handlers
        self.event_handlers = {}

    def start(self):
        self.running = True
        self.on_start()

        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        self.on_exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.on_event(event)
            self.handle_custom_event(event)

    def handle_custom_event(self, event):
        event_type = event.type
        if event_type in self.event_handlers:
            for handler in self.event_handlers[event_type]:
                handler(event)

    def add_event_handler(self, event_type, handler):
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []
        self.event_handlers[event_type].append(handler)

    def update(self):
        self.on_update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.on_draw()
        pygame.display.flip()

    def on_start(self):
        pass

    def on_exit(self):
        pygame.quit()
        sys.exit()

    def on_event(self, event):
        pass

    def on_update(self):
        pass

    def on_draw(self):
        pass

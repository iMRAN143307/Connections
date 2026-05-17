import sys

import pygame

pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
fps = 60
fpsClock = pygame.time.Clock()
food_positions = [
    (140, 36),
    (340, 36),
    (540, 36),
    (740, 36),
    (940, 36),
]  # food size + space in between should be 200 pixels
all_foods = [
    [None, None, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None],
]
foods_shown = all_foods[0]
holding_item = None
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event_pos
                """this is the left click handler, mouse pos is now a (x,y) tuple"""
                if mouse_pos[1] < 237 and mouse_pos[1] > 35:
                    for box in food_positions:
                        if mouse_pos[0] < box[1] + 201 and mouse_pos[0] > box[0] - 1:
                            holding_item = foods_shown[food_positions.index(box)]

    screen.fill((0, 0, 0))
    pygame.display.flip()
    fpsClock.tick(fps)

import asyncio
import os

import pygame

pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()
song0 = "taconnector1.wav"
song1 = "taconnector2.wav"

playlist = [song0, song1]
pygame.mixer.music.load(song0)
pygame.mixer.music.play()
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
fps = 60
fpsClock = pygame.time.Clock()


async def main():
    def load(filename):
        filename = pygame.image.load(os.path.join(f"{filename}.png")).convert_alpha()
        return filename

    def load_and_scale(filename):
        unscaled = pygame.image.load(os.path.join(f"{filename}.png")).convert()
        return pygame.transform.scale(unscaled, (1280, 720))

    current_index = 0
    background = load_and_scale("background")
    arrow_left = load("arrow_left")
    arrow_right = load("arrow_right")
    tomato = [load("tomato"), load("tomatoicon"), 50, 30, 5, 5, 60, 0]
    dill_pickle = [load("dill_pickle"), load("dill_pickleicon"), 5, 80, 20, 70, 20, 0]
    radicchio = [load("radicchio"), load("radicchioicon"), 5, 10, 90, 5, 15, 1]
    corned_beef = [load("corned_beef"), load("corned_beeficon"), 5, 5, 5, 85, 90, 0]
    pickled_jalapenos = [
        load("pickled_jalapenos"),
        load("pickled_jalapenosicon"),
        10,
        75,
        10,
        55,
        20,
        2,
    ]
    lemon = [load("lemon"), load("lemonicon"), 10, 90, 30, 0, 0, 0]
    chili_flakes = [load("chili_flakes"), load("chili_flakesicon"), 0, 5, 15, 5, 15, 3]
    guacamole = [load("guacamole"), load("guacamoleicon"), 10, 30, 5, 25, 55, 0]
    soy_sauce = [load("soy_sauce"), load("soy_sauceicon"), 5, 15, 35, 90, 65, 0]
    honey = [load("honey"), load("honeyicon"), 90, 5, 0, 0, 5, 0]
    arrabbiata_sauce = [
        load("arrabbiata_sauce"),
        load("arrabbiata_sauceicon"),
        60,
        40,
        10,
        30,
        65,
        2,
        tomato,
        chili_flakes,
    ]
    shredded_beef = [
        load("shredded_beef"),
        load("shredded_beeficon"),
        15,
        70,
        30,
        65,
        85,
        0,
        corned_beef,
        lemon,
    ]
    cowboy_candy = [
        load("cowboy_candy"),
        load("cowboy_candyicon"),
        80,
        60,
        15,
        50,
        30,
        2,
        pickled_jalapenos,
        honey,
    ]
    radicchio_cream = [
        load("radicchio_cream"),
        load("radicchio_creamicon"),
        15,
        15,
        70,
        35,
        55,
        1,
        radicchio,
        guacamole,
    ]
    soy_pickle = [
        load("soy_pickle"),
        load("soy_pickleicon"),
        25,
        65,
        30,
        80,
        80,
        0,
        dill_pickle,
        soy_sauce,
    ]
    taco = load("taco")
    food_positions = [
        (140, 36),
        (340, 36),
        (540, 36),
        (740, 36),
        (940, 36),
    ]
    all_foods = [
        [tomato, dill_pickle, radicchio, corned_beef, pickled_jalapenos],
        [chili_flakes, lemon, guacamole, soy_sauce, honey],
        [arrabbiata_sauce, shredded_beef, cowboy_candy, radicchio_cream, soy_pickle],
    ]
    main_cooking_area = [(440, 300), (840, 700)]
    food_in_cooking_area = []
    cycle_food = int(0)
    foods_shown = all_foods[cycle_food]
    holding_item = False
    running = True

    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pos = mouse_pos[0] - 32, mouse_pos[1] - 32
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if holding_item:
                        if (
                            mouse_pos[0] >= main_cooking_area[0][0]
                            and mouse_pos[0] <= main_cooking_area[1][0]
                        ):
                            if (
                                mouse_pos[1] >= main_cooking_area[0][1]
                                and mouse_pos[1] <= main_cooking_area[1][1]
                            ):
                                food_in_cooking_area.append((holding_item, mouse_pos))
                                holding_item = False
                    if mouse_pos[1] < 237 and mouse_pos[1] > 35:
                        for i, box in enumerate(food_positions):
                            if mouse_pos[0] < box[0] + 201 and mouse_pos[0] >= box[0]:
                                holding_item = foods_shown[i]
                    if mouse_pos[1] < 203 and mouse_pos[1] > 61:
                        if mouse_pos[0] >= 0 and mouse_pos[0] < 141:
                            cycle_food -= 1
                            cycle_food = cycle_food % 3
                            foods_shown = all_foods[cycle_food]
                        elif mouse_pos[0] > 1141 and mouse_pos[0] <= 1280:
                            cycle_food += 1
                            cycle_food = cycle_food % 3
                            foods_shown = all_foods[cycle_food]
            if event.type == SONG_END:
                current_index = (current_index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_index])
                pygame.mixer.music.play()
        screen.blit(background, (0, 0))
        screen.blit(taco, main_cooking_area[0])
        screen.blit(arrow_left, (0, 62))
        screen.blit(arrow_right, (1140, 62))
        for i, food in enumerate(foods_shown):
            screen.blit(food[0], food_positions[i])
        for i, obj in enumerate(food_in_cooking_area):
            screen.blit(obj[0][1], obj[1])
        if holding_item:
            screen.blit(holding_item[1], mouse_pos)
        pygame.display.flip()
        fpsClock.tick(fps)
        await asyncio.sleep(0)
    pygame.mixer.music.stop()
    pygame.quit()


asyncio.run(main())

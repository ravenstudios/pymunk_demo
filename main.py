from constants import *
import pymunk
import pygame

import ball
import solid

surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()
clock = pygame.time.Clock()


space = pymunk.Space()
# space.gravity = (10, 10)
static_body = space.static_body

ball1 = ball.Ball(500, 300, RED, space, static_body)
ball2 = ball.Ball(600, 430, BLUE, space, static_body)

thickness = 20
solids = [
    solid.Solid([0, 0, GAME_WIDTH, thickness], GREEN, space),
    solid.Solid([GAME_WIDTH - thickness, 0, thickness, GAME_HEIGHT], GREEN, space),
    solid.Solid([0, GAME_HEIGHT - thickness, GAME_WIDTH, thickness], GREEN, space),
    solid.Solid([0, 0, thickness, GAME_HEIGHT], GREEN, space),



]





def main():
    running = True

    while running:

        clock.tick(TICK_RATE)
        space.step(1 / TICK_RATE)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    pass
                if event.key == pygame.K_q:
                    running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            ball1.body.apply_impulse_at_local_point((100, 100), (0, 0))


        draw()
        update(events)


    pygame.quit()




def draw():
    surface.fill((75, 75, 75))#background
    ball1.draw(surface)
    ball2.draw(surface)
    for solid in solids:
        solid.draw(surface)
    pygame.display.flip()



def update(events):
    ball1.update()
    ball2.update()
    for solid in solids:
        solid.update()

if __name__ == "__main__":
    main()

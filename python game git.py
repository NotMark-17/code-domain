pip install pygame

import pygame

pygame.init()

# Define the window dimensions
WIDTH, HEIGHT = 800, 600

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

def handle_input(keys, spaceship, projectiles):
    if keys[pygame.K_LEFT]:
        spaceship.move_left()
    if keys[pygame.K_RIGHT]:
        spaceship.move_right()
    if keys[pygame.K_UP]:
        spaceship.move_up()
    if keys[pygame.K_DOWN]:
        spaceship.move_down()
    if keys[pygame.K_SPACE]:
        spaceship.shoot(projectiles)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)  # Limit the frame rate to 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input
    keys = pygame.key.get_pressed()
    handle_input(keys, spaceship, projectiles)

    # Update game objects
    update_game_objects(spaceship, enemies, projectiles)

    # Detect and handle collisions
    handle_collisions(spaceship, enemies, projectiles)

    # Render the game
    render(screen, background, spaceship, enemies, projectiles)

pygame.quit()

def render(screen, background, spaceship, enemies, projectiles):
    screen.blit(background, (0, 0))
    spaceship.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    for projectile in projectiles:
        projectile.draw(screen)

    pygame.display.update()


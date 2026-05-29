import pygame
import random
import math
import sys

# ---------------------------------
# GTA STYLE OPEN WORLD MAP SYSTEM
# ---------------------------------
# Install:
# pip install pygame
# ---------------------------------

pygame.init()

# Window settings
WIDTH = 1400
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Open World GTA Style Map")

clock = pygame.time.Clock()
FPS = 60

# Colors
GREEN = (34, 139, 34)
GRAY = (60, 60, 60)
WHITE = (255, 255, 255)
YELLOW = (255, 220, 0)
BLUE = (50, 120, 255)
RED = (220, 50, 50)
BLACK = (0, 0, 0)
BROWN = (120, 80, 40)
LIGHT_GRAY = (150, 150, 150)

# World size
WORLD_WIDTH = 5000
WORLD_HEIGHT = 5000

# Camera
camera_x = 0
camera_y = 0

# Player settings
player_x = WORLD_WIDTH // 2
player_y = WORLD_HEIGHT // 2
player_speed = 5
player_size = 30

# Minimap
MINIMAP_SIZE = 220

# Font
font = pygame.font.SysFont("Arial", 24)

# Roads
roads = []

for i in range(0, WORLD_WIDTH, 400):
    roads.append(pygame.Rect(i, 0, 120, WORLD_HEIGHT))

for j in range(0, WORLD_HEIGHT, 400):
    roads.append(pygame.Rect(0, j, WORLD_WIDTH, 120))

# Buildings
buildings = []

for _ in range(250):
    x = random.randint(0, WORLD_WIDTH - 200)
    y = random.randint(0, WORLD_HEIGHT - 200)
    w = random.randint(80, 200)
    h = random.randint(80, 200)

    buildings.append(pygame.Rect(x, y, w, h))

# Trees
trees = []

for _ in range(500):
    trees.append((
        random.randint(0, WORLD_WIDTH),
        random.randint(0, WORLD_HEIGHT)
    ))

# Cars
cars = []

for _ in range(40):
    car = {
        "x": random.randint(0, WORLD_WIDTH),
        "y": random.randint(0, WORLD_HEIGHT),
        "speed": random.randint(2, 5),
        "direction": random.choice(["horizontal", "vertical"])
    }

    cars.append(car)



def draw_roads():
    for road in roads:
        rect = pygame.Rect(
            road.x - camera_x,
            road.y - camera_y,
            road.width,
            road.height
        )

        pygame.draw.rect(screen, GRAY, rect)

        # Road lines
        if road.width > road.height:
            for x in range(rect.x, rect.x + rect.width, 50):
                pygame.draw.rect(screen, YELLOW, (x, rect.centery - 3, 30, 6))

        else:
            for y in range(rect.y, rect.y + rect.height, 50):
                pygame.draw.rect(screen, YELLOW, (rect.centerx - 3, y, 6, 30))



def draw_buildings():
    for building in buildings:
        rect = pygame.Rect(
            building.x - camera_x,
            building.y - camera_y,
            building.width,
            building.height
        )

        pygame.draw.rect(screen, LIGHT_GRAY, rect)
        pygame.draw.rect(screen, BLACK, rect, 3)

        # Windows
        for wx in range(rect.x + 10, rect.x + rect.width - 10, 30):
            for wy in range(rect.y + 10, rect.y + rect.height - 10, 30):
                pygame.draw.rect(screen, BLUE, (wx, wy, 12, 12))



def draw_trees():
    for tree_x, tree_y in trees:
        x = tree_x - camera_x
        y = tree_y - camera_y

        pygame.draw.rect(screen, BROWN, (x - 4, y, 8, 20))
        pygame.draw.circle(screen, GREEN, (x, y), 15)



def draw_cars():
    for car in cars:
        x = car["x"] - camera_x
        y = car["y"] - camera_y

        pygame.draw.rect(screen, RED, (x, y, 40, 20))



def update_cars():
    for car in cars:
        if car["direction"] == "horizontal":
            car["x"] += car["speed"]

            if car["x"] > WORLD_WIDTH:
                car["x"] = 0

        else:
            car["y"] += car["speed"]

            if car["y"] > WORLD_HEIGHT:
                car["y"] = 0



def draw_player():
    pygame.draw.circle(
        screen,
        WHITE,
        (WIDTH // 2, HEIGHT // 2),
        player_size
    )

    # Direction indicator
    pygame.draw.circle(
        screen,
        BLACK,
        (WIDTH // 2 + 10, HEIGHT // 2 - 10),
        5
    )



def draw_minimap():
    minimap_x = WIDTH - MINIMAP_SIZE - 20
    minimap_y = 20

    pygame.draw.rect(screen, BLACK, (minimap_x, minimap_y, MINIMAP_SIZE, MINIMAP_SIZE))

    scale_x = MINIMAP_SIZE / WORLD_WIDTH
    scale_y = MINIMAP_SIZE / WORLD_HEIGHT

    # Draw roads
    for road in roads:
        mini_road = pygame.Rect(
            minimap_x + road.x * scale_x,
            minimap_y + road.y * scale_y,
            road.width * scale_x,
            road.height * scale_y
        )

        pygame.draw.rect(screen, GRAY, mini_road)

    # Draw player
    player_mini_x = minimap_x + player_x * scale_x
    player_mini_y = minimap_y + player_y * scale_y

    pygame.draw.circle(
        screen,
        RED,
        (int(player_mini_x), int(player_mini_y)),
        5
    )

    pygame.draw.rect(screen, WHITE, (minimap_x, minimap_y, MINIMAP_SIZE, MINIMAP_SIZE), 3)



def draw_hud():
    text = font.render("GTA STYLE OPEN WORLD MAP", True, WHITE)
    screen.blit(text, (20, 20))

    coords = font.render(f"X: {player_x}  Y: {player_y}", True, WHITE)
    screen.blit(coords, (20, 60))

    controls = font.render("WASD = Move", True, WHITE)
    screen.blit(controls, (20, 100))


# Main game loop
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_y -= player_speed

    if keys[pygame.K_s]:
        player_y += player_speed

    if keys[pygame.K_a]:
        player_x -= player_speed

    if keys[pygame.K_d]:
        player_x += player_speed

    # World boundaries
    player_x = max(0, min(WORLD_WIDTH, player_x))
    player_y = max(0, min(WORLD_HEIGHT, player_y))

    # Camera follows player
    camera_x = player_x - WIDTH // 2
    camera_y = player_y - HEIGHT // 2

    # Draw background
    screen.fill((40, 120, 40))

    # Draw world
    draw_roads()
    draw_buildings()
    draw_trees()

    update_cars()
    draw_cars()

    draw_player()

    draw_minimap()
    draw_hud()

    pygame.display.update()

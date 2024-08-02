import pygame
import random

# Ekran boyutları
WIDTH, HEIGHT = 800, 600

# Renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Oyun değişkenleri
bar = pygame.rect.Rect(0, 0, 10, 0)
initial_speed = 500
max_speed = 1500
speed = initial_speed
arrow_directions = ["up", "down", "left", "right"]
current_direction = random.choice(arrow_directions)
prev_direction = None
score = 0
game_over = False

# Çöp Adam Çizimi
def draw_stickman(surface, position, direction):
    x, y = position
    head_radius = 20
    body_length = 60

    # Kafa
    pygame.draw.circle(surface, BLACK, (x, y), head_radius, 2)
    # Gövde
    pygame.draw.line(surface, BLACK, (x, y + head_radius), (x, y + head_radius + body_length), 2)

    # Kollar
    arm_length = 40
    if direction == "up":
        pygame.draw.line(surface, BLACK, (x, y + head_radius + 20), (x - arm_length, y + head_radius + 20 - arm_length),
                         2)
        pygame.draw.line(surface, BLACK, (x, y + head_radius + 20), (x + arm_length, y + head_radius + 20 - arm_length),
                         2)
    elif direction == "down":
        pygame.draw.line(surface, BLACK, (x, y + head_radius + 20), (x - arm_length, y + head_radius + 20 + arm_length),
                         2)
        pygame.draw.line(surface, BLACK, (x, y + head_radius + 20), (x + arm_length, y + head_radius + 20 + arm_length),
                         2)
    elif direction == "left":
        pygame.draw.line(surface, BLACK, (x, y + head_radius + 20), (x - arm_length, y + head_radius + 20), 2)
    elif direction == "right":
        pygame.draw.line(surface, BLACK, (x, y + head_radius + 20), (x + arm_length, y + head_radius + 20), 2)
    else:
        pygame.draw.line(surface, BLACK, (x, y + head_radius + 20), (x - arm_length, y + head_radius + 20), 2)
        pygame.draw.line(surface, BLACK, (x, y + head_radius + 20), (x + arm_length, y + head_radius + 20), 2)

    # Bacaklar
    leg_length = 50
    pygame.draw.line(surface, BLACK, (x, y + head_radius + body_length),
                     (x - arm_length, y + head_radius + body_length + leg_length), 2)
    pygame.draw.line(surface, BLACK, (x, y + head_radius + body_length),
                     (x + arm_length, y + head_radius + body_length + leg_length), 2)


# Ok Çizimi
def draw_arrow(surface, position, direction, color=BLACK):
    x, y = position
    size = 50

    if direction == "up":
        pygame.draw.polygon(surface, color, [(x, y - size), (x - size / 2, y), (x + size / 2, y)])
    elif direction == "down":
        pygame.draw.polygon(surface, color, [(x, y + size), (x - size / 2, y), (x + size / 2, y)])
    elif direction == "left":
        pygame.draw.polygon(surface, color, [(x - size, y), (x, y - size / 2), (x, y + size / 2)])
    elif direction == "right":
        pygame.draw.polygon(surface, color, [(x + size, y), (x, y - size / 2), (x, y + size / 2)])


# Puan Yazdırma
def draw_score(surface, score):
    font = pygame.font.SysFont(None, 36)
    score_surface = font.render(f"Score: {score}", True, BLACK)
    surface.blit(score_surface, (WIDTH - 150, 20))


# Yeniden Başlatma
def restart_game():
    global bar, speed, current_direction, prev_direction, score, game_over
    bar = pygame.rect.Rect(0, 0, 10, 0)
    speed = initial_speed
    current_direction = random.choice(arrow_directions)
    prev_direction = None
    score = 0
    game_over = False

def handle_key_events(event):
    global current_direction, game_over, score, bar, prev_direction, current_direction, speed
    if event.key == pygame.K_LEFT:
        if current_direction == "left" and not game_over:
            score += 15
            bar.height = 0
            prev_direction = "left"
            current_direction = random.choice(arrow_directions)
            speed += 10
        else:
            game_over = True
            pygame.mixer.stop()
    elif event.key == pygame.K_RIGHT:
        if current_direction == "right" and not game_over:
            score += 15
            bar.height = 0
            prev_direction = "right"
            current_direction = random.choice(arrow_directions)
            speed += 10
        else:
            game_over = True
            pygame.mixer.stop()
    elif event.key == pygame.K_UP:
        if current_direction == "up" and not game_over:
            score += 15
            bar.height = 0
            prev_direction = "up"
            current_direction = random.choice(arrow_directions)
            speed += 10
        else:
            game_over = True
            pygame.mixer.stop()
    elif event.key == pygame.K_DOWN:
        if current_direction == "down" and not game_over:
            score += 15
            bar.height = 0
            prev_direction = "down"
            current_direction = random.choice(arrow_directions)
            speed += 10
        else:
            game_over = True
            pygame.mixer.stop()
    speed = min(speed, max_speed)
    print("speed =",speed)
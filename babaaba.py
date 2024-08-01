import pygame
import random
import sys

# Pygame'i başlat
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yön Tuşu Oyunu")

# Renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# FPS ve zamanlayıcı
FPS = 60
clock = pygame.time.Clock()

# Oyun değişkenleri
level = 1
max_level = 10
initial_speed = 1.0
speed = initial_speed
arrow_directions = ["up", "down", "left", "right"]
current_direction = random.choice(arrow_directions)
prev_direction = None
correct_key_pressed = False
score = 0
arrow_color = BLACK
game_over = False
time_to_change_direction = 2000  # 2 saniye başlangıç
last_direction_change = pygame.time.get_ticks()
key_press_allowed = True  # Her değişim için sadece bir tuş basma hakkı
character_direction = None  # Çöp adamın kollarının durumu

# Yanıp Sönme Kontrolü
blink_time = 250  # Yanıp sönme süresi (milisaniye) - 250 ms
last_blink_time = pygame.time.get_ticks()
arrow_visible = True
arrow_blink_once = False  # Okun sadece bir kez yanıp sönmesini kontrol eder

# Yeniden Başlat Butonu
button_font = pygame.font.SysFont(None, 36)
button_text = button_font.render("Yeniden Başlat", True, BLACK)
button_rect = button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))


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
    global level, speed, current_direction, prev_direction, correct_key_pressed, score, arrow_color, game_over, key_press_allowed, character_direction, time_to_change_direction, last_blink_time, arrow_visible, arrow_blink_once
    level = 1
    speed = initial_speed
    current_direction = random.choice(arrow_directions)
    prev_direction = None
    correct_key_pressed = False
    score = 0
    arrow_color = BLACK
    game_over = False
    key_press_allowed = True
    character_direction = None
    time_to_change_direction = 2000  # Ok değişim süresi başlangıçta 2 saniye
    last_blink_time = pygame.time.get_ticks()
    arrow_visible = True
    arrow_blink_once = False


# Ana oyun döngüsü
running = True
while running:
    current_time = pygame.time.get_ticks()

    # Ekranı temizle
    screen.fill(WHITE)

    # Çöp adam ve puan
    draw_stickman(screen, (WIDTH // 2, HEIGHT // 2), character_direction)

    # Yanıp sönme efekti
    if arrow_visible:
        draw_arrow(screen, (WIDTH // 2, 100), current_direction, arrow_color)
    draw_score(screen, score)

    if game_over:
        screen.blit(button_text, button_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
            if button_rect.collidepoint(event.pos):
                restart_game()

    # Zamanı kontrol ederek yön değiştirme
    if current_time - last_direction_change > time_to_change_direction:
        if key_press_allowed:  # Eğer hala basılmadıysa
            arrow_color = RED
            game_over = True
        else:
            prev_direction = current_direction  # Önceki yönü güncelle
            current_direction = random.choice(arrow_directions)
            last_direction_change = current_time
            arrow_color = BLACK  # Ok rengi normale döner
            key_press_allowed = True  # Yeni tuş basma hakkı verilir
            arrow_blink_once = True  # Ok yanıp sönecek

    # Yanıp sönme efekti
    if arrow_blink_once:
        if current_time - last_blink_time > blink_time:
            arrow_visible = not arrow_visible
            last_blink_time = current_time
            arrow_blink_once = False  # Sadece bir kez yanıp sönecek

    # Tuşların kontrolü
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and key_press_allowed:
            if current_direction == "up":
                score += 1
                speed += 0.1
                time_to_change_direction = max(500, time_to_change_direction - 100)  # Hızı artır
                character_direction = "up"
            else:
                arrow_color = RED
                game_over = True
            key_press_allowed = False
        elif keys[pygame.K_DOWN] and key_press_allowed:
            if current_direction == "down":
                score += 1
                speed += 0.1
                time_to_change_direction = max(500, time_to_change_direction - 100)  # Hızı artır
                character_direction = "down"
            else:
                arrow_color = RED
                game_over = True
            key_press_allowed = False
        elif keys[pygame.K_LEFT] and key_press_allowed:
            if current_direction == "left":
                score += 1
                speed += 0.1
                time_to_change_direction = max(500, time_to_change_direction - 100)  # Hızı artır
                character_direction = "left"
            else:
                arrow_color = RED
                game_over = True
            key_press_allowed = False
            elif keys[pygame.K_RIGHT] and key_press_allowed:
            if current_direction == "right":
                score += 1
                speed += 0.1
                time_to_change_direction = max(500, time_to_change_direction - 100)  # Hızı artır
                character_direction = "right"
            else:
                arrow_color = RED
                game_over = True
            key_press_allowed = False

        # Ekranı güncelle
    pygame.display.flip()
    clock.tick(FPS + int(speed * 10))

pygame.quit()


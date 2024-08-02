import pygame
import sys
import socket
import threading
from copadam import *
import babaaba as chal

# Pygame'i başlat
pygame.init()

# Ekran boyutları
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# UDP bağlantısı için ayarlar
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

MAX_FPS = 60

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

free_mode = False
challenge_mode = False
kashik = False

# Yeniden Başlat Butonu
button_font = pygame.font.Font(None, 36)
button_text = button_font.render("Yeniden Başlat", True, chal.BLACK)
button_rect = button_text.get_rect(center=(width // 2, height // 2 - 75))

def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan

def initMixer():
    BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)

kasik_sound = gangam_song = freemode_song = miske_song = floss_song = challenge_song = None

def load_sounds():
    global kasik_sound,gangam_song,freemode_song,miske_song,floss_song,challenge_song
    kasik_sound = pygame.mixer.Sound('kasik.mp3')
    gangam_song = pygame.mixer.Sound('gangam.mp3')
    freemode_song = pygame.mixer.Sound('freemode.mp3')
    miske_song = pygame.mixer.Sound('Miske.mp3')
    floss_song = pygame.mixer.Sound('floss.mp3')
    challenge_song = pygame.mixer.Sound('challange.mp3')

sound_thread = threading.Thread(target=load_sounds)
sound_thread.start()

initMixer()

def draw_kashik(x, y, open = False, angle_degrees = 0, color = (255, 0, 0)):
    if open:
        circle_pos = draw_rotated_line(screen, color, (0 + x, 0 + y), (10 + x, 10 + y), 2, angle_degrees)
        pygame.draw.circle(screen, color, circle_pos, 3)
        circle_pos = draw_rotated_line(screen, color, (10 + x, 0 + y), (0 + x, 10 + y), 2, angle_degrees)
        pygame.draw.circle(screen, color, circle_pos, 3)
    else:
        circle_pos = draw_rotated_line(screen, color, (5 + x, 0 + y), (5 + x, 12 + y), 2, angle_degrees)
        pygame.draw.circle(screen, color, (circle_pos[0] + 1, circle_pos[1]), 3)

# Çöp adamı tanımlayan sınıf
class StickFigure:
    def __init__(self, x, y, color, control_keys):
        self.x = x
        self.y = y
        self.vel_x = 5
        self.vel_y = 10
        self.is_jumping = False
        self.jump_count = 10
        self.dance_mode = None
        self.dance_step = 0
        self.color = color
        self.control_keys = control_keys

    def draw(self, screen):
        # Baş
        pygame.draw.circle(screen, self.color, (self.x, self.y - 20), 10)
        # Gövde
        pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x, self.y + 30), 2)

        kashik_data = ()
        # Kollar
        if self.dance_mode == 'gangnam': #ok
            if self.dance_step % 40 < 10:
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x - 10, self.y - 40), 2)
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x + 10, self.y - 40), 2)
                pygame.draw.line(screen, self.color, (self.x - 10, self.y - 40), (self.x - 30, self.y - 20), 2)
                pygame.draw.line(screen, self.color, (self.x + 10, self.y - 40), (self.x + 30, self.y - 20), 2)
                kashik_data = (self.x - 30, self.y - 20, self.x + 30, self.y - 20, True)
            elif self.dance_step % 40 < 20:
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x - 20, self.y - 20), 2)
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x + 20, self.y - 20), 2)
                pygame.draw.line(screen, self.color, (self.x - 20, self.y - 20), (self.x - 40, self.y), 2)
                pygame.draw.line(screen, self.color, (self.x + 20, self.y - 20), (self.x + 40, self.y), 2)
                kashik_data = (self.x - 40, self.y, self.x + 40, self.y, False)
            elif self.dance_step % 40 < 30:
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x - 10, self.y - 40), 2)
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x + 20, self.y - 40), 2)
                pygame.draw.line(screen, self.color, (self.x - 10, self.y - 40), (self.x - 30, self.y - 20), 2)
                pygame.draw.line(screen, self.color, (self.x + 20, self.y - 40), (self.x + 40, self.y - 20), 2)
                kashik_data = (self.x - 30, self.y - 20, self.x + 40, self.y - 20, True)
            else:
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x - 20, self.y - 20), 2)
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x + 20, self.y - 20), 2)
                pygame.draw.line(screen, self.color, (self.x - 20, self.y - 20), (self.x - 40, self.y), 2)
                pygame.draw.line(screen, self.color, (self.x + 20, self.y - 20), (self.x + 40, self.y), 2)
                kashik_data = (self.x - 40, self.y, self.x + 40, self.y, False)
        elif self.dance_mode == 'ankara':#ok
            if self.dance_step % 40 < 10:
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x - 20, self.y - 20), 2)
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x + 20, self.y - 20), 2)
                pygame.draw.line(screen, self.color, (self.x - 20, self.y - 20), (self.x - 40, self.y), 2)
                pygame.draw.line(screen, self.color, (self.x + 20, self.y - 20), (self.x + 40, self.y), 2)
                kashik_data = (self.x - 40, self.y, self.x + 40, self.y, True)
            elif self.dance_step % 40 < 20:
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x - 40, self.y - 10), 2)
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x + 20, self.y - 20), 2)
                pygame.draw.line(screen, self.color, (self.x - 40, self.y - 10), (self.x - 60, self.y + 10), 2)
                pygame.draw.line(screen, self.color, (self.x + 20, self.y - 20), (self.x + 40, self.y), 2)
                kashik_data = (self.x - 60, self.y + 10, self.x + 40, self.y, False)
            elif self.dance_step % 40 < 30:
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x - 20, self.y - 40), 2)
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x + 20, self.y + 20), 2)
                pygame.draw.line(screen, self.color, (self.x - 20, self.y - 40), (self.x - 40, self.y - 20), 2) 
                pygame.draw.line(screen, self.color, (self.x + 20, self.y + 20), (self.x + 40, self.y + 40), 2) 
                kashik_data = (self.x - 40, self.y - 20, self.x + 40, self.y + 40, True)
            else:
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x - 20, self.y + 40), 2)
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x + 20, self.y + 40), 2)
                pygame.draw.line(screen, self.color, (self.x - 20, self.y + 40), (self.x - 40, self.y + 60), 2) 
                pygame.draw.line(screen, self.color, (self.x + 20, self.y + 40), (self.x + 40, self.y + 60), 2) 
                kashik_data = (self.x - 40, self.y + 60, self.x + 40, self.y + 60, False)
        elif self.dance_mode == 'floss':#ok
            if self.dance_step % 40 < 10:
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x - 20, self.y + 20), 2) 
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x + 20, self.y + 20), 2) 
                kashik_data = (self.x - 20, self.y + 20, self.x + 20, self.y + 20, True)
            elif self.dance_step % 40 < 20:
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x - 40, self.y + 20), 2) 
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x + 40, self.y + 20), 2) 
                kashik_data = (self.x - 40, self.y + 20, self.x + 40, self.y + 20, False)
            elif self.dance_step % 40 < 30:
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x - 60, self.y + 20), 2) 
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x + 60, self.y + 20), 2) 
                kashik_data = (self.x - 60, self.y + 20, self.x + 60, self.y + 20, True)
            else:
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x - 80, self.y + 20), 2) 
                pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x + 80, self.y + 20), 2)
                kashik_data = (self.x - 80, self.y + 20, self.x + 80, self.y + 20, False)
        else:
            pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x - 20, self.y), 2)
            pygame.draw.line(screen, self.color, (self.x, self.y - 10), (self.x + 20, self.y), 2)
            pygame.draw.line(screen, self.color, (self.x - 20, self.y), (self.x - 40, self.y + 20), 2) 
            pygame.draw.line(screen, self.color, (self.x + 20, self.y), (self.x + 40, self.y + 20), 2)
            kashik_data = (self.x - 40, self.y + 20, self.x + 40, self.y + 20, True)

        if kashik:
            draw_kashik(kashik_data[0] - 4, kashik_data[1] - 6, kashik_data[4], 15)
            draw_kashik(kashik_data[2] - 6, kashik_data[3] - 6, kashik_data[4], -15)

        kashik_data = ()
        # Bacaklar
        pygame.draw.line(screen, self.color, (self.x, self.y + 30), (self.x - 10, self.y + 50), 2)
        pygame.draw.line(screen, self.color, (self.x, self.y + 30), (self.x + 10, self.y + 50), 2)
        if self.dance_mode:
            self.dance_step += 1 * 30 / MAX_FPS

    def handle_keys(self, keys):
        if keys[self.control_keys['left']] and self.x > 0:
            self.x -= self.vel_x
        if keys[self.control_keys['right']] and self.x < width:
            self.x += self.vel_x
        if keys[self.control_keys['up']] and self.y > 0:
            self.y -= self.vel_x
        if keys[self.control_keys['down']] and self.y < height:
            self.y += self.vel_x

# Çöp adam listesi
stick_figures = [ #ok
    StickFigure(50, 50, (0,0,0), {
        'right': pygame.K_RIGHT,
        'left': pygame.K_LEFT,
        'up': pygame.K_UP,
        'down': pygame.K_DOWN,
        'jump': pygame.K_UP,
        'dance1': pygame.K_1,
        'dance2': pygame.K_2,
        'stop_dance': pygame.K_3
    })
]

# Yeni çöp adam oluşturma fonksiyonu
def create_stick_figure(): #ok
    if not stick_figures:
        stick_figures.append(StickFigure(50, 50, (0,0,0), {'right': pygame.K_RIGHT,'left': pygame.K_LEFT, 'up': pygame.K_UP, 'down': pygame.K_DOWN, 'jump': pygame.K_UP,'dance1': pygame.K_1,'dance2': pygame.K_2,'stop_dance': pygame.K_3}))
        return

    positions = [(750, 50), (50, 550), (750, 550)]
    colors = [(0, 255, 255), (0, 255, 0), (0, 0, 255)]
    control_keys = [
        {'right': pygame.K_d, 'left': pygame.K_a, 'jump': pygame.K_w, 'up': pygame.K_w, 'down': pygame.K_s,'dance1': pygame.K_q, 'dance2': pygame.K_e,
         'stop_dance': pygame.K_r},
        {'right': pygame.K_l, 'left': pygame.K_j, 'jump': pygame.K_i, 'up': pygame.K_i, 'down': pygame.K_k,'dance1': pygame.K_o, 'dance2': pygame.K_p,
         'stop_dance': pygame.K_u},
        {'right': pygame.K_h, 'left': pygame.K_f, 'jump': pygame.K_t, 'up': pygame.K_t, 'down': pygame.K_g,'dance1': pygame.K_y, 'dance2': pygame.K_u,
         'stop_dance': pygame.K_i}
    ]

    if len(stick_figures) < 4: #ok
        new_position = positions[len(stick_figures) - 1]
        new_keys = control_keys[len(stick_figures) - 1]
        new_color = colors[len(stick_figures) - 1]
        stick_figures.append(StickFigure(*new_position, new_color, new_keys))

# UDP dinleme ve çöp adam oluşturma fonksiyonu
def udp_listener():
    global free_mode, kashik, challenge_mode

    while True:
        data, addr = sock.recvfrom(1024)
        message = data.decode('utf-8')
        if message == 'YeniKarekter': #ok
            create_stick_figure()
        elif message.startswith('DansModu'): #ok
            _, dance_mode = message.split()
            for stick_figure in stick_figures:
                stick_figure.dance_mode = dance_mode
                stick_figure.dance_step = 0
            
            pygame.mixer.stop()
            if dance_mode == 'gangnam':
                gangam_song.play(-1)
            elif dance_mode == 'ankara':
                miske_song.play(-1)
            elif dance_mode == 'floss':
                floss_song.play(-1)

            if kashik:
                kasik_sound.play(-1)

        elif message.startswith('FreeMode'):
            free_mode = not free_mode
            try:
                pygame.mixer.stop()
                if free_mode:
                    freemode_song.play(-1)
                else:
                    freemode_song.stop()
            except:
                print("error playing sound")
        elif message == 'Reset': #ok
            stick_figures.clear()
            pygame.mixer.stop()
            free_mode = False
            kashik = False
            global left_upper_arm_angle, x, y, left_lower_arm_angle, right_upper_arm_angle,right_lower_arm_angle,left_upper_leg_angle ,left_lower_leg_angle ,right_upper_leg_angle  ,right_lower_leg_angle  ,angle_increment,arm_length,leg_length

            x, y = width // 2, height // 2
            left_upper_arm_angle = 0
            left_lower_arm_angle = 0
            right_upper_arm_angle = 0
            right_lower_arm_angle = 0
            left_upper_leg_angle = -75  # Sol üst bacak açısı
            left_lower_leg_angle = -75  # Sol alt bacak açısı
            right_upper_leg_angle = 75  # Sağ üst bacak açısı
            right_lower_leg_angle = 75  # Sağ alt bacak açısı
            angle_increment = 15
            arm_length = 50
            leg_length = 50
        elif message == 'Kasik':
            kashik = not kashik
            try:
                if kashik:
                    kasik_sound.play(-1)
                else:
                    kasik_sound.stop()
            except:
                print("error playing sound")
        elif message == 'Challenge':
            challenge_mode = not challenge_mode
            pygame.mixer.stop()
            chal.restart_game()
            if challenge_mode and not chal.game_over:
                challenge_song.play(-1)
        elif message == 'Stop':
            pygame.quit()
            sys.exit()

# UDP dinleme işlevini ayrı bir iş parçacığında çalıştırma
threading.Thread(target=udp_listener, daemon=True).start()

# Ana döngü
running = True
while running:
    if clock.get_fps():
        dt = 1 / clock.get_fps()
    else:
        dt = 1 / MAX_FPS

    if not chal.game_over and challenge_mode:
        chal.bar.height += chal.speed * dt
        if chal.bar.height > height:
            chal.game_over = True
            pygame.mixer.stop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and chal.game_over and challenge_mode:
            if button_rect.collidepoint(event.pos):
                chal.restart_game()
                pygame.mixer.stop()
                challenge_song.play(-1)
        elif event.type == pygame.KEYDOWN:
            if free_mode and not challenge_mode:
                if event.key == pygame.K_w:
                    left_upper_arm_angle = min(left_upper_arm_angle + angle_increment, 90)
                elif event.key == pygame.K_s:
                    left_upper_arm_angle = max(left_upper_arm_angle - angle_increment, -90)
                elif event.key == pygame.K_d:
                    left_lower_arm_angle = min(left_lower_arm_angle + angle_increment, 90)
                elif event.key == pygame.K_a:
                    left_lower_arm_angle = max(left_lower_arm_angle - angle_increment, -90)
                elif event.key == pygame.K_k:
                    right_upper_arm_angle = min(right_upper_arm_angle + angle_increment, 90)
                elif event.key == pygame.K_i:
                    right_upper_arm_angle = max(right_upper_arm_angle - angle_increment, -90)
                elif event.key == pygame.K_l:
                    right_lower_arm_angle = min(right_lower_arm_angle + angle_increment, 90)
                elif event.key == pygame.K_j:
                    right_lower_arm_angle = max(right_lower_arm_angle - angle_increment, -90)
                elif event.key == pygame.K_UP:
                    left_upper_leg_angle = min(left_upper_leg_angle + angle_increment, 90)
                elif event.key == pygame.K_DOWN:
                    left_upper_leg_angle = max(left_upper_leg_angle - angle_increment, -90)
                elif event.key == pygame.K_LEFT:
                    left_lower_leg_angle = min(left_lower_leg_angle + angle_increment, 90)
                elif event.key == pygame.K_RIGHT:
                    left_lower_leg_angle = max(left_lower_leg_angle - angle_increment, -90)
                elif event.key == pygame.K_KP2:
                    right_upper_leg_angle = min(right_upper_leg_angle + angle_increment, 90)
                elif event.key == pygame.K_KP8:
                    right_upper_leg_angle = max(right_upper_leg_angle - angle_increment, -90)
                elif event.key == pygame.K_KP4:
                    right_lower_leg_angle = min(right_lower_leg_angle + angle_increment, 90)
                elif event.key == pygame.K_KP6:
                    right_lower_leg_angle = max(right_lower_leg_angle - angle_increment, -90)
            elif challenge_mode:
                chal.handle_key_events(event)
                if event.key == pygame.K_SPACE:
                    if chal.game_over:
                        chal.restart_game()
                        pygame.mixer.stop()
                        challenge_song.play(-1)

    if not free_mode and not challenge_mode:
        keys = pygame.key.get_pressed()
        for stick_figure in stick_figures:
            stick_figure.handle_keys(keys)

    screen.fill((255, 255, 255))

    if challenge_mode:
        chal.draw_stickman(screen, (width // 2, height // 2), chal.prev_direction)
        if chal.game_over:
            screen.blit(button_text, button_rect)
            chal.draw_arrow(screen, (width // 2, 100), chal.current_direction, chal.RED)
        else:
            chal.draw_arrow(screen, (width // 2, 100), chal.current_direction)

        chal.draw_score(screen, chal.score)
        pygame.draw.rect(screen, chal.RED, chal.bar)
    else:
        for stick_figure in stick_figures:
            stick_figure.draw(screen)

        if free_mode:
            draw_stick_figure(screen, x, y, left_upper_arm_angle, left_lower_arm_angle, right_upper_arm_angle, right_lower_arm_angle, left_upper_leg_angle, left_lower_leg_angle, right_upper_leg_angle, right_lower_leg_angle)
    
    pygame.display.flip()
    clock.tick(MAX_FPS)               

sound_thread.join()

pygame.quit()
sys.exit()
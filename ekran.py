import pygame
import sys
import socket
import threading
from copadam import *

# Pygame'i başlat
pygame.init()

# Ekran boyutları
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# UDP bağlantısı için ayarlar
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

free_mode = False
kashik = False

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
    def __init__(self, x, y, control_keys):
        self.x = x
        self.y = y
        self.vel_x = 5
        self.vel_y = 10
        self.is_jumping = False
        self.jump_count = 10
        self.dance_mode = None
        self.dance_step = 0
        self.control_keys = control_keys

    def draw(self, screen):
        # Baş
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y - 20), 10)
        # Gövde
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x, self.y + 30), 2)

        kashik_data = ()
        # Kollar
        if self.dance_mode == 'gangnam': #ok
            if self.dance_step % 40 < 10:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 10, self.y - 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 10, self.y - 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 10, self.y - 40), (self.x - 30, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 10, self.y - 40), (self.x + 30, self.y - 20), 2)
                kashik_data = (self.x - 30, self.y - 20, self.x + 30, self.y - 20, True)
            elif self.dance_step % 40 < 20:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 20, self.y - 20), (self.x - 40, self.y), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y - 20), (self.x + 40, self.y), 2)
                kashik_data = (self.x - 40, self.y, self.x + 40, self.y, False)
            elif self.dance_step % 40 < 30:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 10, self.y - 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y - 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 10, self.y - 40), (self.x - 30, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y - 40), (self.x + 40, self.y - 20), 2)
                kashik_data = (self.x - 30, self.y - 20, self.x + 40, self.y - 20, True)
            else:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 20, self.y - 20), (self.x - 40, self.y), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y - 20), (self.x + 40, self.y), 2)
                kashik_data = (self.x - 40, self.y, self.x + 40, self.y, False)
        elif self.dance_mode == 'ankara':#ok
            if self.dance_step % 40 < 10:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 20, self.y - 20), (self.x - 40, self.y), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y - 20), (self.x + 40, self.y), 2)
                kashik_data = (self.x - 40, self.y, self.x + 40, self.y, True)
            elif self.dance_step % 40 < 20:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 40, self.y - 10), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 40, self.y - 10), (self.x - 60, self.y + 10), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y - 20), (self.x + 40, self.y), 2)
                kashik_data = (self.x - 60, self.y + 10, self.x + 40, self.y, False)
            elif self.dance_step % 40 < 30:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y - 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y + 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 20, self.y - 40), (self.x - 40, self.y - 20), 2) 
                pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y + 20), (self.x + 40, self.y + 40), 2) 
                kashik_data = (self.x - 40, self.y - 20, self.x + 40, self.y + 40, True)
            else:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y + 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y + 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 20, self.y + 40), (self.x - 40, self.y + 60), 2) 
                pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y + 40), (self.x + 40, self.y + 60), 2) 
                kashik_data = (self.x - 40, self.y + 60, self.x + 40, self.y + 60, False)
        elif self.dance_mode == 'floss':#ok
            if self.dance_step % 40 < 10:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y + 20), 2) 
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y + 20), 2) 
                kashik_data = (self.x - 20, self.y + 20, self.x + 20, self.y + 20, True)
            elif self.dance_step % 40 < 20:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 40, self.y + 20), 2) 
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 40, self.y + 20), 2) 
                kashik_data = (self.x - 40, self.y + 20, self.x + 40, self.y + 20, False)
            elif self.dance_step % 40 < 30:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 60, self.y + 20), 2) 
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 60, self.y + 20), 2) 
                kashik_data = (self.x - 60, self.y + 20, self.x + 60, self.y + 20, True)
            else:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 80, self.y + 20), 2) 
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 80, self.y + 20), 2)
                kashik_data = (self.x - 80, self.y + 20, self.x + 80, self.y + 20, False)
        else:
            pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y), 2)
            pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y), 2)
            pygame.draw.line(screen, (0, 0, 0), (self.x - 20, self.y), (self.x - 40, self.y + 20), 2) 
            pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y), (self.x + 40, self.y + 20), 2)
            kashik_data = (self.x - 40, self.y + 20, self.x + 40, self.y + 20, True)

        if kashik:
            draw_kashik(kashik_data[0] - 4, kashik_data[1] - 6, kashik_data[4], 15)
            draw_kashik(kashik_data[2] - 6, kashik_data[3] - 6, kashik_data[4], -15)

        kashik_data = ()
        # Bacaklar
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + 30), (self.x - 10, self.y + 50), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + 30), (self.x + 10, self.y + 50), 2)
        if self.dance_mode:
            self.dance_step += 1

    def handle_keys(self, keys):
        if keys[self.control_keys['left']]:
            self.x -= self.vel_x
        if keys[self.control_keys['right']]:
            self.x += self.vel_x
        if not self.is_jumping:
            if keys[self.control_keys['jump']]:
                self.is_jumping = True
        else:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10

# Çöp adam listesi
stick_figures = [ #ok
    StickFigure(50, 50, {
        'right': pygame.K_RIGHT,
        'left': pygame.K_LEFT,
        'jump': pygame.K_UP,
        'dance1': pygame.K_1,
        'dance2': pygame.K_2,
        'stop_dance': pygame.K_3
    })
]

# Yeni çöp adam oluşturma fonksiyonu
def create_stick_figure(): #ok
    if not stick_figures:
        stick_figures.append(StickFigure(50, 50, {'right': pygame.K_RIGHT,'left': pygame.K_LEFT,'jump': pygame.K_UP,'dance1': pygame.K_1,'dance2': pygame.K_2,'stop_dance': pygame.K_3}))
        return

    positions = [(750, 50), (50, 550), (750, 550)]
    control_keys = [
        {'right': pygame.K_d, 'left': pygame.K_a, 'jump': pygame.K_w, 'dance1': pygame.K_q, 'dance2': pygame.K_e,
         'stop_dance': pygame.K_r},
        {'right': pygame.K_l, 'left': pygame.K_j, 'jump': pygame.K_i, 'dance1': pygame.K_o, 'dance2': pygame.K_p,
         'stop_dance': pygame.K_u},
        {'right': pygame.K_h, 'left': pygame.K_f, 'jump': pygame.K_t, 'dance1': pygame.K_y, 'dance2': pygame.K_u,
         'stop_dance': pygame.K_i}
    ]

    if len(stick_figures) < 4: #ok
        new_position = positions[len(stick_figures) - 1]
        new_keys = control_keys[len(stick_figures) - 1]
        stick_figures.append(StickFigure(*new_position, new_keys))

# UDP dinleme ve çöp adam oluşturma fonksiyonu
def udp_listener():
    global free_mode, kashik

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
        elif message.startswith('FreeMode'):
            free_mode = not free_mode
        elif message == 'Reset': #ok
            stick_figures.clear()
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
        elif message == 'Stop':
            pygame.quit()
            sys.exit()

# UDP dinleme işlevini ayrı bir iş parçacığında çalıştırma
threading.Thread(target=udp_listener, daemon=True).start()

# Ana döngü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if free_mode:
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

    if not free_mode:
        keys = pygame.key.get_pressed()
        for stick_figure in stick_figures:
            stick_figure.handle_keys(keys)

    screen.fill((255, 255, 255))
    for stick_figure in stick_figures:
        stick_figure.draw(screen)

    if free_mode:
        draw_stick_figure(screen, x, y, left_upper_arm_angle, left_lower_arm_angle, right_upper_arm_angle, right_lower_arm_angle, left_upper_leg_angle, left_lower_leg_angle, right_upper_leg_angle, right_lower_leg_angle)
    
    pygame.display.flip()
    clock.tick(30)

import pygame
import math

# Ekran boyutları
width, height = 800, 600

# Renkler
black = (0, 0, 0)
white = (255, 255, 255)

# Çöp adamın başlangıç konumu
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

def draw_stick_figure(screen, x, y, left_upper_arm_angle, left_lower_arm_angle, right_upper_arm_angle, right_lower_arm_angle, left_upper_leg_angle, left_lower_leg_angle, right_upper_leg_angle, right_lower_leg_angle):
    # Vücut
    pygame.draw.line(screen, black, (x, y - 50), (x, y + 50), 2)  # Vücut
    pygame.draw.circle(screen, black, (x, y - 70), 20, 2)  # Kafa

    # Sol Kol
    left_shoulder_x, left_shoulder_y = x, y - 30
    left_elbow_x = left_shoulder_x + arm_length * math.cos(math.radians(left_upper_arm_angle - 180))
    left_elbow_y = left_shoulder_y + arm_length * math.sin(math.radians(left_upper_arm_angle - 180))
    left_hand_x = left_elbow_x + arm_length * math.cos(math.radians(left_lower_arm_angle - 180))
    left_hand_y = left_elbow_y + arm_length * math.sin(math.radians(left_lower_arm_angle - 180))

    pygame.draw.line(screen, black, (left_shoulder_x, left_shoulder_y), (left_elbow_x, left_elbow_y), 2)  # Üst kol
    pygame.draw.line(screen, black, (left_elbow_x, left_elbow_y), (left_hand_x, left_hand_y), 2)  # Alt kol

    # Sağ Kol
    right_shoulder_x, right_shoulder_y = x, y - 30
    right_elbow_x = right_shoulder_x + arm_length * math.cos(math.radians(right_upper_arm_angle))
    right_elbow_y = right_shoulder_y + arm_length * math.sin(math.radians(right_upper_arm_angle))
    right_hand_x = right_elbow_x + arm_length * math.cos(math.radians(right_lower_arm_angle))
    right_hand_y = right_elbow_y + arm_length * math.sin(math.radians(right_lower_arm_angle))

    pygame.draw.line(screen, black, (right_shoulder_x, right_shoulder_y), (right_elbow_x, right_elbow_y), 2)  # Üst kol
    pygame.draw.line(screen, black, (right_elbow_x, right_elbow_y), (right_hand_x, right_hand_y), 2)  # Alt kol

    # Sol Bacak
    left_hip_x, left_hip_y = x, y + 50
    left_knee_x = left_hip_x + leg_length * math.cos(math.radians(left_upper_leg_angle - 180))
    left_knee_y = left_hip_y + leg_length * math.sin(math.radians(left_upper_leg_angle - 180))
    left_foot_x = left_knee_x + leg_length * math.cos(math.radians(left_lower_leg_angle - 180))
    left_foot_y = left_knee_y + leg_length * math.sin(math.radians(left_lower_leg_angle - 180))

    pygame.draw.line(screen, black, (left_hip_x, left_hip_y), (left_knee_x, left_knee_y), 2)  # Üst bacak
    pygame.draw.line(screen, black, (left_knee_x, left_knee_y), (left_foot_x, left_foot_y), 2)  # Alt bacak

    # Sağ Bacak
    right_hip_x, right_hip_y = x, y + 50
    right_knee_x = right_hip_x + leg_length * math.cos(math.radians(right_upper_leg_angle))
    right_knee_y = right_hip_y + leg_length * math.sin(math.radians(right_upper_leg_angle))
    right_foot_x = right_knee_x + leg_length * math.cos(math.radians(right_lower_leg_angle))
    right_foot_y = right_knee_y + leg_length * math.sin(math.radians(right_lower_leg_angle))

    pygame.draw.line(screen, black, (right_hip_x, right_hip_y), (right_knee_x, right_knee_y), 2)  # Üst bacak
    pygame.draw.line(screen, black, (right_knee_x, right_knee_y), (right_foot_x, right_foot_y), 2)  # Alt bacak

def draw_rotated_line(screen, color, start_pos, end_pos, width, angle):
    """Draw a rotated line on the screen."""
    # Unpack start and end positions
    x1, y1 = start_pos
    x2, y2 = end_pos
    
    # Calculate the center of the line segment
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    
    # Convert angle to radians
    angle_rad = math.radians(angle)
    cos_angle = math.cos(angle_rad)
    sin_angle = math.sin(angle_rad)
    
    # Translate points to origin
    x1 -= cx
    y1 -= cy
    x2 -= cx
    y2 -= cy
    
    # Rotate points
    x1_rot = x1 * cos_angle - y1 * sin_angle
    y1_rot = x1 * sin_angle + y1 * cos_angle
    x2_rot = x2 * cos_angle - y2 * sin_angle
    y2_rot = x2 * sin_angle + y2 * cos_angle
    
    # Translate points back
    x1_rot += cx
    y1_rot += cy
    x2_rot += cx
    y2_rot += cy
    
    # Draw the rotated line
    pygame.draw.line(screen, color, (int(x1_rot), int(y1_rot)), (int(x2_rot), int(y2_rot)), width)

    return (int(x2_rot), int(y2_rot))
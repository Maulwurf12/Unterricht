import sys

import pygame
import pygame as pg
import tkinter as tk
from tkinter import simpledialog

pygame.init()
size = width, height = 612, 612
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
snack_1_size_from = 174,118
snack_1_size_to = 224,168
snack_2_size_from = 240,122
snack_2_size_to = 284,170
snack_3_size_from = 301,121
snack_3_size_to = 342,171
snack_4_size_from = 181,201
snack_4_size_to = 221,244
snack_5_size_from = 229,207
snack_5_size_to = 254,247
snack_6_size_from =267,206
snack_6_size_to =284,247
snack_7_size_from =292,207
snack_7_size_to =308,241
snack_8_size_from =317,207
snack_8_size_to =342,243
snack_9_size_from =177,286
snack_9_size_to =202,313
snack_10_size_from = 219,283
snack_10_size_to = 250,314
snack_11_size_from = 258,280
snack_11_size_to = 293,316
snack_12_size_from = 312,283
snack_12_size_to = 340,311
snack_13_size_from = 177,333
snack_13_size_to = 207,388
snack_14_size_from = 224,340
snack_14_size_to = 251,382
snack_15_size_from = 265,327
snack_15_size_to = 300,389
snack_16_size_from = 314,330
snack_16_size_to = 342,382
pay_field_from = 402,166
pay_field_to = 443,247
submit_field_from = 401,313
submit_field_to = 439,354
snacks = {
    1: {"from": snack_1_size_from, "to": snack_1_size_to, "cost": 1.50},
    2: {"from": snack_2_size_from, "to": snack_2_size_to, "cost": 2.00},
    3: {"from": snack_3_size_from, "to": snack_3_size_to, "cost": 1.80},
    4: {"from": snack_4_size_from, "to": snack_4_size_to, "cost": 1.20},
    5: {"from": snack_5_size_from, "to": snack_5_size_to, "cost": 2.50},
    6: {"from": snack_6_size_from, "to": snack_6_size_to, "cost": 2.30},
    7: {"from": snack_7_size_from, "to": snack_7_size_to, "cost": 1.00},
    8: {"from": snack_8_size_from, "to": snack_8_size_to, "cost": 1.75},
    9: {"from": snack_9_size_from, "to": snack_9_size_to, "cost": 2.10},
    10: {"from": snack_10_size_from, "to": snack_10_size_to, "cost": 2.20},
    11: {"from": snack_11_size_from, "to": snack_11_size_to, "cost": 1.40},
    12: {"from": snack_12_size_from, "to": snack_12_size_to, "cost": 2.00},
    13: {"from": snack_13_size_from, "to": snack_13_size_to, "cost": 1.30},
    14: {"from": snack_14_size_from, "to": snack_14_size_to, "cost": 1.90},
    15: {"from": snack_15_size_from, "to": snack_15_size_to, "cost": 2.70},
    16: {"from": snack_16_size_from, "to": snack_16_size_to, "cost": 1.10}
}

def is_inside_bounds(point, top_left, bottom_right):
    return top_left[0] < point[0] < bottom_right[0] and top_left[1] < point[1] < bottom_right[1]

running = True
# Counter-Wert initialisieren
counter = 0

# Pygame Font initialisieren
font = pygame.font.Font(None, 36)  # Standard-Schriftart mit Größe 36

def draw_counter(value):
    # Text rendern (weiß auf schwarzem Hintergrund)
    text = font.render(f"Score: {value}", True, (255, 255, 255))
    # In der oberen linken Ecke zeichnen
    screen.blit(text, (10, 10))
try:
    snackMachine = pygame.image.load('./images/snackMachine.png')
except pygame.error as e:
    print(f"Fehler beim Laden des Bildes: {e}")
    sys.exit()

screen.blit(snackMachine, (0, 0))
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = pygame.mouse.get_pos()
            for snack_id, data in snacks.items():
                if is_inside_bounds(pressed, data["from"], data["to"]):
                    print(f"Snack {snack_id} ausgewählt. Kosten: {data['cost']} €")
                    break
            if is_inside_bounds(pressed, pay_field_from, pay_field_to):
                print("pay")
            elif is_inside_bounds(pressed, submit_field_from, submit_field_to):
                print("submit")
    draw_counter(counter)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()

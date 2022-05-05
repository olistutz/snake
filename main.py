# Programmierprojekt Snake

# Einfügen von bestehenden Libarys
import pygame
import time
import random

pygame.init()

# Farben definieren
weiss = (255, 255, 255)
gelb = (255, 255, 100)
schwarz = (0, 0, 0)
rot = (200, 50, 80)
gruen = (0, 255, 0)
blau = (50, 150, 200)

# Displaygrösse definieren
display_breite = 600
display_hoehe = 400

dis = pygame.display.set_mode((display_breite, display_hoehe))
pygame.display.set_caption('Snake Game')





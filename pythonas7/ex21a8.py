#adcionando musica e instalando pygame pela lampada
import pygame

pygame.init()
pygame.mixer.music.load("ex21a8.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()
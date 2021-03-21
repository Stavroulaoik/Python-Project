import pygame
import sys
import time
import random


FPS = 60

WIDTH = 1000
HEIGHT = 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Game")



class Game:
    def __init__(self):
        self.reset = True
        self.active = False
        self.word = ' '
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time: 0\n Accuracy: 0\n WPM: 0\n'
        self.wpm = 0
        self.end = False
        self.HEAD_C =(255,213,102)
        self.TEXT_C =(240,240,240)
        self.RESULT_C = (255,70,70)



    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.w/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()



def main():
    run = True
    clock = pygame.time.Clock()

    def redraw_window():
        screen.fill((0, 128, 0))
        pygame.display.update()

    while run:
         clock.tick(FPS)
         redraw_window()

         for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    quit()

main()


for event in pygame.event.get():
  if event.type == pygame.QUIT:
    quit()



Game().run()
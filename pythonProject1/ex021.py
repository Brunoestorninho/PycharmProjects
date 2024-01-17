import pygame
pygame.init()   #iniciar pygame
pygame.mixer.music.load('ex021a.mp3')    #carregar a musica
pygame.mixer.music.play()   #tocar a musica
pygame.event.wait()     #esperar terminar para encerrar o programa

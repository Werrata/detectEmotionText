#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 20:00:45 2022

@author: benjamin
"""

import pandas as pd
import pygame
import time
import sys
import queue


#Personal import
import detectEmotionTextRoberta



# Fait afficher un écran pour rentrer du texte. 
# Le texte rentré sera passé au programme PlayMusicAccordingText toutes les 5 secondes sans rien faire
def WriteText():
    pygame.init()
    clock = pygame.time.Clock()
    # it will display on screen
    SIZE_LENGTH = 1200
    SIZE_HEIGHT = 250
    screen = pygame.display.set_mode([SIZE_LENGTH, SIZE_HEIGHT]) 
    # basic font for user typed
    base_font = pygame.font.Font(None, 32)
    pygame.display.set_caption('musai')
    icon = pygame.image.load('/Users/Utilisateur/Desktop/CoursENSEA/2A/Projet_2A/DetectEmotionText/logoMusai.png')
    pygame.display.set_icon(icon)

    # imageMusai = pygame.image.load('/Users/Utilisateur/Desktop/CoursENSEA/2A/Projet_2A/DetectEmotionText/nomLogiciel.png').convert()
    # screen.blit(imageMusai, (0,0))

    # create rectangle
    input_rect = pygame.Rect(20, SIZE_HEIGHT/4, 100, 32)
    waiting_rect = pygame.Rect(400, 200, 1000, 32)
    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color(210,210,210)
    color_passive = pygame.Color(0,0,0)
    jauneMusai = pygame.Color(255,242,40) # La couleur choisie est le même jaune que celui du logo
    color = color_passive
    active = False

    user_text = ""
    emotion1, emotion2 = "", ""
    idiotInt = 0

    file = open("registered_messages.txt",'a')
  
    while True:
        for event in pygame.event.get():
        # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                file.close()
                pygame.quit()
                sys.exit()
  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
  
            if event.type == pygame.KEYDOWN:
            # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    screen.blit(base_font.render("stop pressing keys and listen to the music please", True, jauneMusai),(2*SIZE_LENGTH/5, 2*SIZE_HEIGHT/3))
                    pygame.display.flip()
                    emotion1, emotion2 = detectEmotionTextRoberta.PlayMusicAccordingText(user_text)
                    file.write('message  :  ' + user_text + '\nemotion  :  ' + emotion1 + ', ' + emotion2 + '\n\n')
                    pygame.event.clear()
                    user_text = ""
                else:
                    if input_rect.w < 1160: user_text += event.unicode
                    else: detectEmotionTextRoberta.BipSound()
                

                     
    # it will set background color of screen
        screen.fill((255, 255, 255))
  
        if active:
            color = color_active
        else:
            color = color_passive
        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, (0, 0, 0))
        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

        if idiotInt == 1:
            screen.blit(base_font.render("You idiot", True, (255, 0, 0)),(500, 60))#(700,250) est la position du message
            pygame.display.flip()
      
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width()+10)
      
        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pygame.display.flip()
      
        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)



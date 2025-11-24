import pygame 
from typing import Callable

class Button:
    def __init__(self, x : int, y : int, width : int, height : int, text : str, action : Callable):  
        self.text = text
        
        self.action = action
        self.font = pygame.font.Font(None, 70)
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))  
        self.button_rect = pygame.Rect(x, y, width, height) 
        
        self.text_color = (255,255,255) 
    
    def __eq__(self, value):
        return self.text == value
    
    def __ne__(self, value):
        return self.text != value
        
    def draw(self, surface):
        text_surface = self.font.render(self.text, True, (255, 255, 255)) # White text
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        surface.blit(text_surface, text_rect)
        
    def handle_event(self, event, *args):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                if self.action:
                    self.action(self, *args)
                    self.action = None
                    return True
        return False

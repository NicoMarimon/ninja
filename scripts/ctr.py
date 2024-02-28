import pygame, random
class CRT:
    def __init__(self, surf, screen_height, screen_width):
        self.surf = surf
        self.surf_w = screen_width
        self.surf_h = screen_height
        self.tv = pygame.image.load('data/images/tv.png').convert_alpha()
        self.tv = pygame.transform.scale(self.tv,(self.surf_w,self.surf_h))

    def create_crt_lines(self):
        line_height = 3
        line_amount = int(self.surf_h / line_height)
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv,'black',(0,y_pos),(self.surf_w,y_pos),1)

    def draw(self):
        self.tv.set_alpha(random.randint(75,100))
        self.create_crt_lines()
        self.surf.blit(self.tv,(0,0))
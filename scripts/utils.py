import os
import pygame

# Default path
BASE_IMG_PATH = 'data/images/'

def load_image(path): # Esta función carga una imagen
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0,0,0)) # Crear fondo transparente
    return img

def load_images(path): # Esta función carga una lista de imágenes
    images = []
    for image_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + image_name))

    return images

class Animation:
    def __init__(self, images, img_dur = 5, loop =True):
        self.images = images
        self.loop = loop
        self.img_duration = img_dur
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)
    
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True
    
    def img(self):
        return self.images[int(self.frame / self.img_duration)]
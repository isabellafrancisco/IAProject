import pygame

class estado_inicial(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('estados/estado_inicial.png')
        self.image = pygame.transform.scale(self.image, [120, 150])
                              # x, y, w(larg), h(alt)
        self.rect = pygame.Rect(10, 10, 10, 10)

class estado1(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('estados/2m2c_1m1c.png')
        self.image = pygame.transform.scale(self.image, [120, 150])
                              # x, y, w(larg), h(alt)
        self.rect = pygame.Rect(120, 30, 120, 30)

class estado2(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('estados/3m2c_0m1c.png')
        self.image = pygame.transform.scale(self.image, [120, 150])
                              # x, y, w(larg), h(alt)
        self.rect = pygame.Rect(230, 50, 230, 50)

class estado3(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('estados/3m0c_0m3c.png')
        self.image = pygame.transform.scale(self.image, [120, 150])
                              # x, y, w(larg), h(alt)
        self.rect = pygame.Rect(340, 70, 340, 70)

class estado4(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('estados/3m1c_om2c.png')
        self.image = pygame.transform.scale(self.image, [120, 150])
                              # x, y, w(larg), h(alt)
        self.rect = pygame.Rect(450, 90, 450, 90)

class estado5(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        #if(estado == )
        self.image = pygame.image.load('estados/1m1c_2m2c.png')
        self.image = pygame.transform.scale(self.image, [120, 150])
                              # x, y, w(larg), h(alt)
        self.rect = pygame.Rect(560, 110, 560, 110)

class estado6(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        #if(estado == )
        self.image = pygame.image.load('estados/2m2c_1m1c.png')
        self.image = pygame.transform.scale(self.image, [120, 150])
                              # x, y, w(larg), h(alt)
        self.rect = pygame.Rect(670, 130, 670, 130)

class estado7(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        #if(estado == )
        self.image = pygame.image.load('estados/0m2c_3m1c.png')
        self.image = pygame.transform.scale(self.image, [120, 150])
                              # x, y, w(larg), h(alt)
        self.rect = pygame.Rect(780, 150, 780, 150)

class estado8(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        #if(estado == )
        self.image = pygame.image.load('estados/0m3c_3m0c.png')
        self.image = pygame.transform.scale(self.image, [120, 150])
                              # x, y, w(larg), h(alt)
        self.rect = pygame.Rect(890, 170, 890, 170)

class estado9(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        #if(estado == )
        self.image = pygame.image.load('estados/0m1c_3m2c.png')
        self.image = pygame.transform.scale(self.image, [120, 150])
                              # x, y, w(larg), h(alt)
        self.rect = pygame.Rect(1000, 190, 1000, 190)

class estado10(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        #if(estado == )
        self.image = pygame.image.load('estados/1m1c_2m2c.png')
        self.image = pygame.transform.scale(self.image, [120, 150])
                              # x, y, w(larg), h(alt)
        self.rect = pygame.Rect(1110, 210, 1110, 210)

class estado_final(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        #if(estado == )
        self.image = pygame.image.load('estados/estado_final.png')
        self.image = pygame.transform.scale(self.image, [120, 150])
                              # x, y, w(larg), h(alt)
        self.rect = pygame.Rect(1220, 230, 1220, 230)
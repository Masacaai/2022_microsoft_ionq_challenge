from helper import *
from quantum import *
from variables import *

class inputbox:
    def __init__(self, x, y, w, h,text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (255,0,0)
        self.text = text
        self.txt_surface = type.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = not self.active
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = type.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

class mob(object):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color

    def init_virus(self):
        self.firststate = cirk1.initialize(qiskit.quantum_info.random_statevector(2).data, 0)
        self.secondstate = cirk1.initialize(qiskit.quantum_info.random_statevector(2).data, 1)

    def move(self):
        self.pos = (self.pos[0] + 1, self.pos[1])

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, 30)

class gate(object):
    def __init__(self, color, pos, type):
        self.pos = pos
        self.color = color
        self.type = type
        self.rect = pygame.Rect(self.pos[0], self.pos[1], dis, dis)
        self.drag = False
        self.offset_x = 0
        self.offset_y = 0
        self.mouse_x = 0
        self.mouse_y = 0

    def move(self, event):

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.drag:
                #print("Before rect(x,y): ", self.rect.x, self.rect.y)
                #print("Before mouse coords: ", event.pos[0], event.pos[1])
                # Error: Due to the weird 1.5 row scaling, the tile sometimes snaps to the wrong container
                #if (self.rect.x % 40) > 20:
                #    self.rect.x = event.pos[0] - 40 - (event.pos[0] % 40)
                #    self.rect.y = event.pos[1] - 40 - (event.pos[1] % 40)
                #else:
                    self.rect.x = self.mouse_x - (self.mouse_x % 80)
                    self.rect.y = self.mouse_y - (self.mouse_y % 80)
                    self.drag = False
                #print("After rect(x,y): ", self.rect.x, self.rect.y)
                #print("After mouse coords: ", self.mouse_x, self.mouse_y)
        elif event.type == pygame.MOUSEMOTION:
            if self.drag:
                self.mouse_x, self.mouse_y = event.pos
                self.rect.x = self.mouse_x + self.offset_x
                self.rect.y = self.mouse_y + self.offset_y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        words(self.type, 50, black, self.rect.x + 40, self.rect.y + 40, surface)


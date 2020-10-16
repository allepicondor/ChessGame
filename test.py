import copy
import pygame

KNIGHT_BLACK = pygame.image.load('PiecesImg/Black/Knight.png')
class Dog:
    def __init__(self):
        self.happy = True
        self.Sad = False
        self.x = 70
    def draw(self,win):
        pos = [300,300]
        win.blit(pygame.transform.scale(KNIGHT_BLACK,(20,20)), (pos[0]-1,pos[1]-2))

class Person:
    def __init__(self):
        self.pets = []
        self.dd = 6767
        self.passcode = 546564
        self.x = 430
    def buyPets(self):
        self.pets.append(Dog())
        self.pets[0].x = 30
def CopyClass(person):
    new_person = Person()
    new_person.pets = person.pets
    new_person.dd = person.dd
    new_person.passcode = person.passcode
    new_person.x = person.x
    return new_person
Tom = Person()
Tom.buyPets()
Tom.x = 60

New_tom = copy.deepcopy(Tom)

New_tom.x = 30
New_tom.pets[0].x = 604530
print(Tom.x,Tom.pets[0].x,Tom.passcode,Tom.dd)
print(New_tom.x,New_tom.pets[0].x,New_tom.passcode,New_tom.dd)
win = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
New_tom.pets[0].draw(win)
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    pygame.display.update()



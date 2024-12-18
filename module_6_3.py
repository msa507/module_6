import random

class Animal:

    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        _coords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        coords = [dx, dy, dz]
        if self.speed > 0:
             _coords = map(lambda x: x * self.speed, coords)
        if dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            Animal.x = dx * self.speed
            Animal.y = dy * self.speed
            Animal.z = dz * self.speed
        print(list(_coords))
        return _coords

    def get_coords(self):
         pass

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print('Sorry, Im peaceful :)')
        else:
            print('Be careful, Im attacking you 0_0')

    def speak(self):
        sound = self.sound
        print(sound)


class Bird(Animal):
    beak = True
    random_eggs = random.randint(0, 4)

    def lay_eggs(self, random_eggs):
        print (f'Here are(is) {random_eggs} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        pass

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal ):
    sound = "Click-click-click"



db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()
db.move(1, 2, -3)


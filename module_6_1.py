class Animal:
    alive = True
    fed = False
    name = []
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food == Plant.edible:
            fed = True
            print(f'{self.name} съел {food.name}')
        else:
            alive = False
            print(f'{self.name} не стал есть {food.name}')


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

class Flower(Plant):

    def __init__(self, flower_name):
        self.name = flower_name
        print(f' O {flower_name} ')


class Fruit(Plant):

    def __init__(self, fruit_name):
        self.name = fruit_name
        print(f' O {fruit_name} ')


a1 = Predator('Волк с Уолл-Стрит')
# a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
# p2 = Fruit('Заводной апельсин')

# print(a1.name)
# print(p1.name, p2.name)

# print(a1.alive)
# print(a2.fed)
a1.eat(p1)

# a2.eat(p2)
# print(a1.alive)
# print(a2.fed)

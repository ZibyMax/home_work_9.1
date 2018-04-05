# Общий класс - животные
class Animals():
    voice = None
    limb = None
    skin = None
    nose = None

    # и все они умеют кричать
    def cry(self):
        print(self.voise)


# Классы домашней скотины и птицы наследуют от предка общие свойства с уникальными значениями
class Livestock(Animals):
    # уникальное свойство - есть рога
    horns = True
    limb = 'hooves'
    skin = 'wool'
    nose = 'normal nose)'


class Fowl(Animals):
    horns = True
    limb = 'paws and wings'
    skin = 'plumage'
    nose = 'beak'

    # уникальный метод - могут летать
    def fly(self):
        print('I FLY!')


class Cow(Livestock):
    voise = 'мууу мууу'


class Goat(Livestock):
    voise = 'меее меее'


class Sheep(Livestock):
    voise = 'беее беее'


# у свиньи переопределяем переменные родительского класса
class Pig(Livestock):
    skin = 'pigskin'
    nose = 'piglet'
    horns = None
    voise = 'хрю хрю'


class Duck(Fowl):
    voise = 'кря кря'


class Goose(Fowl):
    voise = 'га га га'


# у курицы переопределяем метод родительского класса
class Chicken(Fowl):
    voise = 'кудах кудах)'

    def fly(self):
        print('I forgot to fly(')


# перекличка на скотном дворе
animals = [Cow(), Goat(), Sheep(), Pig(), Duck(), Goose(), Chicken()]
for animal in animals:
    animal.cry()

# есть ли у коровы рога
burenka = Cow()
if burenka.horns:
    print('У коровы рога есть')
else:
    print('Нет рогов')

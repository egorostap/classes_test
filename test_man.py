# модель человека по принципам ооп
from random import randint

class Animal:
    def __init__(self):
        self.fulness = 50
        self.happiness = 30
        self.health = 100
        self.food = 0

    def activity(self):
        if self.health <= 100:
            self.fulness -= 10
            self.happiness += 10
            self.health += 20

    def eat(self):
        self.fulness += 30
        self.food -= 30
        self.happiness += 30
        self.health += 10


    def take_food(self):
        self.food += 30
        self.eat()



class Man(Animal):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.money = 0
        self.home = None

    def __str__(self):
        return f'Я - {self.name}, моя сытость: {self.fulness}, количество денег: {self.money}, уровень счастья: {self.happiness}, уровень здоровья: {self.health}'

    def take_food(self):
        if self.food < 30 and self.home.food >= 30:
            self.food += 30
            self.home.food -= 30
            print('взял еду из холодильника')
            self.take_food()
        elif self.home.food < 30:
            print('пойду в магазин за едой')
            self.shopping()
            self.take_food()
        else:
            self.eat()
            print('я поел, спасибо!')


    def work(self):
        self.fulness -= 20
        self.money += 50
        self.home.money += 50
        self.happiness -= 20
        self.health -= 10
        print(f'я сходил на работу и заработал 50 денег')

    def play_dota(self):
        self.fulness -= 10
        self.happiness += 50
        self.money -= 10
        self.health -= 5
        print('я поиграл в доту, и стал счастливее на 50 единиц')

    def watch_sunset(self):
        self.fulness -= 5
        self.happiness += 10
        self.health += 5
        print('я смотрел на закат и стал счастливее на 10 единиц')

    def shopping(self):
        if self.money < 60 and self.home.money >= 60:
            self.home.money -= 60
            self.money += 60
        elif self.home.money < 60:
            self.work()
        else:
            self.home.food += 60
            self.money -= 60

    def go_home(self, home):
        self.home = home
        print(f'Я заехал в {self.home}')

    def act(self):
        self.happiness -= 10
        dice = randint(1, 6)

        if self.fulness <= 0:
            self.health = 0
            return 'the end'
        elif self.fulness <= 20:
            self.take_food()
        elif self.health < 50:
            self.activity()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.watch_sunset()
        else:
            self.play_dota()

class Home:
    def __init__(self):
        self.money = 1000
        self.happiness = 100
        self.food = 300

    def __str__(self):
        return f'в доме еды осталось: {self.food}, денег осталось в доме: {self.money}'


sweet_home = Home()
one_man = Man(name='one_man')
one_man.go_home(home=sweet_home)

day = 1
while day < 5000 and one_man.act() != 'the end':
    day += 1
    print(f'__________день {day}___________')
    one_man.act()
    print(one_man)
    print(sweet_home)

if day == 5000 or one_man.act() == 'the end':
    print('the end')

class  Arrows(object):
    def __init__(self,name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f'{self.name} наношу урон {self.damage}'


class Heroes(object):

    def __init__(self, name, hp):
        self.name = name
        self.max_hp =  hp
        self.hp = hp
        self.Arrows = Arrows('Стреляю с лука  !', 40)


    def action(self):
        return print(f'{self.name} Меня призвали сражаться ')

    def a_arrowas(self, arrows: Arrows):
        self.arrows = arrows

    def attack(self, other: 'Heroes'):
        print(f'{self.name} Я {self.Arrows.name} Враг атакует! {other.name} ')
        other.hp -= self.Arrows.damage

    def action(self):
        return print(f'{self.name} Меня призвали сражаться ')

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f'{self.name}, - {self.hp}/{self.max_hp} HP'

class Orck(Heroes):
    def __init__(self, name, hp, shot):
        super().__init__(name, hp)
        self.max_hp = hp
        self.arrows = Arrows('Бью с топора', 20)
        self.shot = shot

    def attack(self, other: 'Heroes'):
        print(f'{self.name}  Враг атакует! {other.name} Я {self.Arrows.name} ')
        other.hp -= self.Arrows.damage * self.shot

# Archer = Arrows('Arrows', 2)
Drowka = Heroes('Drowka', 290)
Bloodseker = Orck('Bloodseker', 180, 2)

Drowka.action()
Bloodseker.action()

while any([Bloodseker.is_alive(),Drowka.is_alive()]):
    Bloodseker.attack(Drowka)
    print(Drowka)
    Drowka.attack(Bloodseker)
    print(Bloodseker)

class Hero:
    is_adult = 0
    is_adult = 100

    @classmethod
    def urivni(cls, max):
        return cls.is_adult <= max <= cls.is_adult

    def __init__(self, name, lvl, HP, talent):
        self.name = name
        self.lvl = lvl
        self.HP = HP
        self.talent = talent

    def introduce(self):
        return print(f'Привет, меня зовут {self.name}, мой LVL {self.lvl}, мое HP {self.HP} ')


Hunter = Hero('Diablo', 45, 1800, 'archery' )
Druid = Hero('Hiler', 50, 2800, 'buff')
Paladin = Hero('Drinor', 80, 5200, 'Protect')

Hunter.introduce()
Druid.introduce()
Paladin.introduce()

print(Hero.urivni(100))
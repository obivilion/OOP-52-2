from main import Hero


class Jester(Hero):
    from main import Hero

    def unique_attack(self):
        return print("Ouuu")

    def unique_scream(self):
        return print('Ass')


    def action(self):
        if 1 == self.get_random_int():
            print(self.attack)
        elif 2 == self.get_random_int():
            print(self.protection)
        else:
            return self.rest()
        print(self.rest)


Loi = Jester("name", 12, 200, 2)
Loi.action()
Loi.unique_attack()
Loi.unique_scream()

class Enemy(object):

    def __init__(self, name = "Enemy", hit_points = 0, lives = 1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_hitpoints = self.hit_points - damage
        if remaining_hitpoints >= 0:
            self.hit_points = remaining_hitpoints
            print("now i have {} hit points".format(self.hit_points))
        else:
            self.lives -= 1

    def __str__(self):
        print("Name: {0.name}, Lives: {0.lives}, Hitpoints: {0.hit_points}".format(self))

class Vampyre(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)

class Vampyre_King(Vampyre):
    def __init__(self, name):
        super().__init__(name)
        self.hit_points = 140
    
    def take_damage(self, damage):
        return super().take_damage(damage//4)

Pepe = Vampyre_King("Pepe")

Pepe.take_damage(14)
Pepe.__str__()
class Participants:
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health = 100

    def health_up(self, add):
        if self.health < 100:
            self.health += add
        if self.health > 100:
            self.health = 100

    def health_down(self, got_damage):
        self.health -= got_damage
        if self.health <= 0:
            self.health = 0
            return 'Dead. Game Over'

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health


class Movement:
    def __init__(self):
        super().__init__()
        self.position = 0
        self.move = 2

    def get_position(self):
        return self.position

    def moved(self):
        self.position += self.move

    def set_position(self, dist):
        self.position = dist


class Archer:
    def __init__(self):
        super().__init__()
        self.attack = 5
        self.attack_dist = 4

    def get_attack(self):
        return self.attack

    def get_attack_dist(self):
        return self.attack_dist


class Medic:
    def __init__(self):
        super().__init__()
        self.attack = 1
        self.heal = 3

    def get_heal(self):
        return self.heal


class Infantryman:
    def __init__(self):
        super().__init__()
        self.attack = 5
        self.attack_dist = 1

    def get_attack(self):
        return self.attack

    def get_attack_dist(self):
        return self.attack_dist


class ArcherMain(Participants, Archer, Movement):
    pass


class MedicMain(Participants, Medic, Movement):
    pass


class InfantrymanMain(Participants, Infantryman, Movement):
    pass
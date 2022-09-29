class Monster:
    def __init__(self, name, health, melee, speed, defence, gold, loot):
        self.name = name
        self.health = health
        self.melee = melee
        self.speed = speed
        self.defence = defence
        self.gold = gold
        self.loot = loot

    # getters - for getting a variable
    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_melee(self):
        return self.melee

    def get_speed(self):
        return self.speed

    def get_defence(self):
        return self.defence

    def get_gold(self):
        return self.gold

    def get_loot(self):
        return self.loot



    # setters - for changing a variable
    def set_health(self, new_health):
        self.health = new_health

    def set_melee(self, new_melee):
        self.melee = new_melee

    def set_defence(self, new_defence):
        self.defence = new_defence

    def set_gold(self, new_gold):
        self.gold = new_gold

    def set_negative_loot(self, new_loot):
        self.loot.remove(new_loot)
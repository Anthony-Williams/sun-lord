class Hero:
    def __init__(self, max_health, health, max_melee, melee, ranged, stealth, defence, max_magic, magic,
                 gold, hero_class, name, equipment):
        self.max_health = max_health
        self.health = health
        self.max_melee = max_melee
        self.melee = melee
        self.ranged = ranged
        self.stealth = stealth
        self.defence = defence
        self.max_magic = max_magic
        self.magic = magic
        self.gold = gold
        self.hero_class = hero_class
        self.name = name
        self.equipment = equipment

    # getters - for getting a variable
    def get_max_health(self):
        return self.max_health

    def get_health(self):
        return self.health

    def get_max_melee(self):
        return self.max_melee

    def get_melee(self):
        return self.melee

    def get_ranged(self):
        return self.ranged

    def get_stealth(self):
        return self.stealth

    def get_defence(self):
        return self.defence

    def get_max_magic(self):
        return self.max_magic

    def get_magic(self):
        return self.magic

    def get_gold(self):
        return self.gold

    def get_hero_class(self):
        return self.hero_class

    def get_name(self):
        return self.name

    def get_equipment(self):
        return self.equipment

    # setters - for changing a variable
    def set_health(self, new_health):
        if new_health > self.max_health:
            self.health = self.max_health
        else:
            self.health = new_health

    def set_max_melee(self, new_max_melee):
        self.max_melee = new_max_melee

    def set_melee(self, new_melee):
        if new_melee > self.max_melee:
            self.melee = self.max_melee
        else:
            self.melee = new_melee

    def set_ranged(self, new_ranged):
        self.ranged = new_ranged

    def set_stealth(self, new_stealth):
        self.stealth = new_stealth

    def set_defence(self, new_defence):
        self.defence = new_defence

    def set_magic(self, new_magic):
        if new_magic > self.max_magic:
            self.magic = self.max_magic
        else:
            self.magic = new_magic

    def set_gold(self, new_gold):
        self.gold = new_gold

    def set_positive_equipment(self, new_equipment):
        self.equipment.append(new_equipment)

    def set_negative_equipment(self, new_equipment):
        self.equipment.remove(new_equipment)
import random


class World:
    def __init__(self, weather, time_unit, magic_time_marker, tower_upper_floor_campfire, purple_moss):
        self.weather = weather
        self.time_unit = time_unit
        self.magic_time_marker = magic_time_marker
        self.tower_upper_floor_campfire = tower_upper_floor_campfire
        self.purple_moss = purple_moss


    def get_weather(self):
        return self.weather


    def get_time_unit(self):
        return self.time_unit


    def get_magic_time_marker(self):
        return self.magic_time_marker


    def get_tower_upper_floor_campfire(self):
        return self.tower_upper_floor_campfire


    def get_purple_moss(self):
        return self.purple_moss


    # setters
    def set_weather(self, new_weather):
        self.weather = new_weather


    def set_new_weather(self):
        weather_options = ['rain', 'rain', 'heavy rain', 'rain and fog', 'fog']
        self.weather = random.choice(weather_options)


    def set_time_unit(self, new_time_unit):
        self.time_unit = new_time_unit


    def set_magic_time_marker(self, new_magic_time_marker):
        self.magic_time_marker = new_magic_time_marker


    def set_tower_upper_floor_campfire(self, new_tower_upper_floor_campfire):
        self.tower_upper_floor_campfire = new_tower_upper_floor_campfire


    def set_purple_moss(self, new_purple_moss):
        self.purple_moss = new_purple_moss
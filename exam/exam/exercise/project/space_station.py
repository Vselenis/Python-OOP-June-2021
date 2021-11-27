from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type, name):
        if astronaut_type == "Biologist":
            new_astronaut = Biologist(name)
            if not self.astronaut_repository.find_by_name(name):
                self.astronaut_repository.add(new_astronaut)
                return f"Successfully added {astronaut_type}: {name}."
            else:
                return f"{name} is already added."
        elif astronaut_type == "Geodesist":
            new_astronaut = Geodesist(name)
            if not self.astronaut_repository.find_by_name(name):
                self.astronaut_repository.add(new_astronaut)
                return f"Successfully added {astronaut_type}: {name}."
            else:
                return f"{name} is already added."
        elif astronaut_type == "Meteorologist":
            new_astronaut = Meteorologist(name)
            if not self.astronaut_repository.find_by_name(name):
                self.astronaut_repository.add(new_astronaut)
                return f"Successfully added {astronaut_type}: {name}."
            else:
                return f"{name} is already added."
        else:
            raise Exception("Astronaut type is not valid!")


    def add_planet(self, name, *items):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        else:
            self.planet_repository.add(Planet(name))
            Planet(name).items = items
            return f"Successfully added Planet: {name}."


    def retire_astronaut(self, name):
        try:
            filter_astronaut = [n for n in self.astronaut_repository.astronauts if n.name == name][0]
            self.astronaut_repository.astronauts.remove(filter_astronaut)
            return f"Astronaut {name} was retired!"
        except:
            raise Exception(f"Astronaut {name} doesn't exists!")

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen()

    def send_on_mission(self, planet_name):
        try:
            if self.planet_repository.find_by_name(planet_name):
                the_best_astro = sorted([b for b in self.astronaut_repository.astronauts.oxygen])[:5]
        except:
            raise Exception("Invalid planet name!")





    def report(self):
        pass

# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self, city_population: int, room_num: int):
        self.city_population = city_population
        self.room_num = room_num

    def get_person_room(self) -> int:
        return self.room_num

    def get_city_population(self) -> int:
        return self.city_population


# TODO после выполнения задания попробуйте
if __name__ == '__main__':
    human = Person(11002, 42)
    print(human.get_person_room())
    print(human.get_city_population())

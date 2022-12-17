# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, speed: int = 1, condition=None, field=(0, 0)):
        self.speed = speed
        self.condition = condition
        self.field = field

    def _set_condition(self):
        if self.condition == 'fly':
            self.speed *= 1.2
        elif self.condition == 'crawl':
            self.speed *= 0.5
        else:
            raise ValueError('Эк тебя раскорячило')

    def move_(self, x_coord, y_coord, direction):
        if direction == 'UP':
            new_y = y_coord + self.speed
            new_x = x_coord
            return self._set_field(new_x, new_y)
        elif direction == 'DOWN':
            new_y = y_coord - self.speed
            new_x = x_coord
            return self._set_field(new_x, new_y)
        elif direction == 'LEFT':
            new_y = y_coord
            new_x = x_coord - self.speed
            return self._set_field(new_x, new_y)
        elif direction == 'RIGTH':
            new_y = y_coord
            new_x = x_coord + self.speed
            return self._set_field(new_x, new_y)

    def _set_field(self, x_coord, y_coord):
        self.field = (x_coord, y_coord)
        return self.field


unit = Unit(condition='fly')
unit.move_(1, 2, 'UP')
print(unit.field)


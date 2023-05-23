#1
class CashRegister:
    def __init__(self):
        self.money = 0

    def top_up(self, amount):
        self.money += amount

    def count_1000(self):
        return self.money // 1000

    def take_away(self, amount):
        if self.money >= amount:
            self.money -= amount
        else:
            raise ValueError("Недостаточно денег в кассе")

#2

class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("Невозможно уменьшить количество клеточек до значения ≤ 0")

    def count_moves(self, x2, y2):
        x_diff = abs(self.x - x2)
        y_diff = abs(self.y - y2)
        return (x_diff + y_diff) // self.s + (1 if (x_diff + y_diff) % self.s != 0 else 0)

from random import randint


class Die():
    """表示一个骰子的类"""

    def __init__(self, number_sides=6):
        """骰子默认是6面"""
        self.number_sides = number_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机数"""
        return randint(1, self.number_sides)

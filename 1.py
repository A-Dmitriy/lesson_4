from sys import argv

name, time, rate, bonus = argv

def simple_calc():
    try:
        time = int(time)
        rate = int(rate)
        bonus = int(bonus)
        res = time * rate + bonus
        print(f'заработная плата сотрудника  {res}")
    except ValueError:
        print("Введите 3 числа")

simple_calc()
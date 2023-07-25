def dict_generator(names: list[str], wage_rate: list[int], bonus: list[str]) -> dict[str, float]:
    if len(names) == len(wage_rate) == len(bonus):
        result = {k : v1+(v1*float(v2[:-1])/100) for (k, v1, v2) in zip(names, wage_rate, bonus)}
        return result


names = ["Иван", "Сергей", "Пётр", "Василий"]
wage_rate = [1000, 800, 900, 950]
bonus = ["15.6%", "10.25%", "22.63%", "17.8%"]

print(dict_generator(names, wage_rate, bonus))

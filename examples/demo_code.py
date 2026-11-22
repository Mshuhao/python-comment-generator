def calculate_total(price_list):
    total = 0
    for p in price_list:
        total += p
    return total

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name}, {self.age}岁"


class House:
    def __init__(self):
        self.numberOfFloors = 0
    def setNewNumberOfFloors(self,floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)


h1 = House()
print(h1.numberOfFloors)
h1.setNewNumberOfFloors(5)

'''
class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f"Количество этажей изменено на: {self.numberOfFloors}")


# Пример использования:
my_house = House()  # Создаем объект дома с начальной этажностью 0
print(f"Начальное количество этажей: {my_house.numberOfFloors}")

my_house.setNewNumberOfFloors(5)  # Изменяем этажность на 5
my_house.setNewNumberOfFloors(10)  # Изменяем этажность на 10
'''
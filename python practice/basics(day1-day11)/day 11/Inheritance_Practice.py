class vehicle:
    def __init__(self, brand, model, year, type):
        self.model = model
        self.brand = brand
        self.year = year
        self.type = type

    def start(self):
        print(
            f"{self.brand} {self.model} of {self.type} belongs to year {self.year} is starting")


class car(vehicle):
    def start(self):
        print(
            f"{self.brand} {self.model} of {self.type} belongs to year {self.year} car starting...")


class bike(vehicle):
    def start(self):
        print(
            f"{self.brand} {self.model} of {self.type} belongs to year {self.year} bike starting...")


car1 = car("toyoto", "FORTUNER", "2020", "bs6")
car1.start()

class vehicle:
    def __init__(self, brand, model, year, type):
        self.brand = brand
        self.model = model
        self.year = year
        self.type = type


class car(vehicle):
    def __init__(self, brand, model, year, type, fuel_type):
        super().__init__(brand, model, year, type)
        self.fuel_type = fuel_type

    def show_info(self):
        print(f"{self.brand} {self.model} of type {self.type} in the year {self.year} uses fuel of type {self.fuel_type} ")


car1 = car("toyoto", "fortuner", "2020", "BS6", "petrol")
car1.show_info()

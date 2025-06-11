class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"the {self.brand} {self.model} is starting....")


car1 = car("ambasidor", "c2")
car2 = car("toyota", "fortuner")
car1.start()
car2.start()

class Car:
    def __init__(self, brand, model):      # __init__() is the constructor
        self.brand = brand                 # 'self' is like 'this' of js
        self.model = model
    
    def fetch_full_name(self):
        return f'{self.brand} {self.model}'

my_car = Car('Lambo', 'Aventador')
print('your car brand is : ', my_car.brand)
print('your car full name is : ', my_car.fetch_full_name())


# Inheritance 
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar('Tesla', "model-s", '84kwh')

print('Your electric car model is :',my_tesla.model)
print('Your electric car full name is :',my_tesla.fetch_full_name())  # see we have acess to the super classe's methods
from car import Car

my_new_car =Car('BMW', '7 series', 2017)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#9.4.3从一个模块中导入多个类
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

me_tesla = ElectricCar('tesla', 'roadster', 2016)
print(me_tesla.get_descriptive_name())

#9.4.4 导入整个模块
import car

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

me_tesla = ElectricCar('tesla', 'roadster', 2016)
print(me_tesla.get_descriptive_name())

#9.4.5 导入模块中的所有类
from car import *

#9.4.6在一个模块中导入另一个模块
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

me_tesla = ElectricCar('tesla', 'roadster', 2016)
print(me_tesla.get_descriptive_name())

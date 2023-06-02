# from car import Car
# from car import *                                    #导入模块中所有的类
# from car import Car as EC                            #使用别名

# import car                                             #导入整个模板
import car as Es

my_new_car = Es.Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

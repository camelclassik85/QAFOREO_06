'''4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
     периметр квадрата, площадь квадрата и диагональ квадрата.'''
# def square(a):
#     return (4*a, a**2, a * (2**0.5))
# print(square(4))

'''4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно 
     в формате аргумент: значение. Например:
	name: John
	last_name: Smith
	age: 35 
	position: web developer'''
# def name_fun(**kwargs):
#     for a, b in kwargs.items():
#         print(f'{a}: {b}')
# name_fun(name = "Joh", last_name = "Smith", age = 35)

'''4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только 
     положительные числа'''
# my_list = [20, -3, 15, 2, -1, -21]
# new_list = list(filter(lambda x: x >= 0, my_list))
# print(new_list)

'''4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке '''
# from functools import reduce
# my_list = [20, -3, 15, 2, -1, -21]
# res = reduce(lambda x, y: x * y, my_list)
# print(res)

'''4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра '''
# import time
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         print(f'spent time {time.perf_counter() - start}')
#         return result
#
#     return wrapper
#
#
# @timer
# def complex_calculation():
#     time.sleep(0.5)
#     return "end function"
#
#
# print(complex_calculation())

'''4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления. 
     Примените эти функции в качестве методов в другом файле. '''
# import my_calc

# print(my_calc.multi(2, 3))
# print(my_calc.sum_args(2, 3, 4, 5, 5, 6))
# print(my_calc.multi(5, 6))
# print(my_calc.division(99, 0))

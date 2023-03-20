#  3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(*my_list[2])

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# list_dig = [x for x in list_1 if type(x) == int]
# list_str = [x for x in list_1 if type(x) == str]
# for i in list_str:
#     if "a" in i:
#         print(i)
# print(sum(list_dig))

# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
# print(tuple(['cat', 'dog', 'horse', 'cow']))

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family_1 = tuple(input().split(','))
# family_2 = tuple(input().split(','))
# if len(family_1) > len(family_2):
#     print(f'семья с большим составом{family_1}')
# elif len(family_2) > len(family_1):
#     print(f'семья с большим составом{family_2}')
# else:
#     print('Equal')

#
# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
#my_dict = {
#     'title': 'newnew',
#     'director': "dfdfdf",
#     'year': "1985",
#     'budget': "1200000000",
#     'main_actor': "Me young_do",
#     'slogan': "be or not to be"
#}
# print(*my_dict.keys())
# print(*my_dict.values())
#for kv in my_dict.items():
#    print(kv)

#
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# sum1 = 0
# for i in range(1, len(my_dictionary) + 1):
#     sum1 += my_dictionary['num' + str(i)]
# print(sum1)
# print(sum(my_dictionary.values()))

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# list_1 = [1, 2, 3, 4, 5, 3, 2, 1]
# list_1 = list(set(list_1))
# print(list_1)
# # print(*set(list_1))

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set1.symmetric_difference(set2))
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print(set1.issuperset(set2))
# print(set2.issuperset(set1))









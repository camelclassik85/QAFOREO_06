'''5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
    - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
    нужно использовать методы get и set'''
class MyClass:

    Color = 'orange'

    def __init__(self, name='Alex', surname='Smith', age='0', weight='0'):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight
        print('Create object of MyClass')

    def print_info(self):
        print(f'Name of MyClass {self.name} {self.surname} with weight {self.weight} and age {self.age}')

    # def get_name(self):
    #     return self.__name if self.__name else None
    #
    # def set_name(self, name):
    #     self.__name = name
    #     self.Color = 'green'


class Worker(MyClass):
    def __init__(self, name, surname, age, weight, prof='baker'):
        super().__init__(name, surname, age, weight)
        self.prof = prof
        print(self.prof)

    def is_working(self):
        print(f'{self.name} {self.surname} is working by {self.prof}')

class Officer(MyClass):
    def __init__(self, name, surname, age, weight):
        super().__init__(name, surname, age, weight)

    def print_info(self):
        print(
            f'Name of Officer {self.name} {self.surname} with weight {self.weight} and age {self.age}'
        )

class Gibrid(Officer, Worker):
    def print_gibrid(self):
        print(f'Gibrid created')


# person = MyClass(name='Konor', surname="McGregor", weight='77', age='35')
# print(person.__dict__)
# print(person.name)
# person.print_info()
# print(person.Color)
# print(MyClass.Color)
# person.set_name('Boris')
# print(person.Color)
worker1 = Worker(name='Boris', surname='Krylov', age='43', weight='98', prof='builder')
worker2 = Worker('Peter', 'Vix', '34', '87',"US NAvy")
print(worker1.__dict__)
print(worker2.__dict__)
worker1.print_info()
worker2.is_working()
officer1 = Officer('Gala', 'Petro', '35', '33')
print(officer1.__dict__)
officer1.print_info()
gibrid1 = Gibrid('Troll', 'Grace', '21', '45')
print(gibrid1.__dict__)
gibrid1.print_info()

'''
5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий
'''
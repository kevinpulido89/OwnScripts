# source> https://www.youtube.com/watch?v=JeznW_7DlB0
# Python Object Oriented Programming (OOP) - For Beginners

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 -100

    def get_grade(self):
        return self.grade

class Course(object):
    """docstring for Course."""

    def __init__(self, name, max_students):
        super(Course, self).__init__()
        self.name = name
        self.max_students = max_students
        self.students = list()

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        value = 0
        for st in self.students:
            value += st.get_grade()
        return value/len(self.students)

s1 = Student('Tim', 19, 95)
s2 = Student('Bill', 20, 75)
s3 = Student('Kevin', 31, 98)

Math = Course('Math', 2)
Math.add_student(s1)
Math.add_student(s2)

'''
print(Math.students[0].name)
print(Math.get_average_grade())
'''

## Inheritance

class Pet(object):
    """Docstring for Pet.

    Parameters:
        str1 (str):The string which is to be reversed.

    Returns:
        reverse(str1):The string which gets reversed.

    """
    def __init__(self, name, age):
        super(Pet, self).__init__()
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    '''
    [ES] Gato
    [FR] Chat
    '''
    def __init__(self, name, age, color):
        super(Cat, self).__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I'm {self.color}")

class Dog(Pet):
    '''
    [ES] Gato
    [FR] Chat
    '''
    def speak(self):
        print("Woof")

class Fish(Pet):
    '''
    [ES] Pez
    [FR] Poisson
    '''
    pass

p = Pet('Kevin',31)
c = Cat('Santi',13, 'Blue')
d = Dog('Canela',9)
f = Fish('Bubbles', 2)

'''
p.show()
c.show()
d.speak()
f.speak()
print(c.__doc__)
print(isinstance(d,Cat))
print(issubclass(Cat,Dog))
'''

# classmethods

class Person(object):
    """docstring for Person."""
    number_of_people = 0

    def __init__(self, name, age):
        super(Person, self).__init__()
        self.name = name
        self.age = age
        Person.add_person()

    @classmethod
    def how_many_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    @classmethod
    def from_string(cls, string_):
        name, age = string_.split('-')
        return cls(name, int(age))

    @staticmethod
    def Birthday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return 'Cae fin de semana'
        return 'Cae entre semana'

p1 = Person('Tim', 20)
p2 = Person('Kevin',31)

new_person = 'Sofi-14'
p3 = Person.from_string(new_person)
# print(Person.how_many_people())

'''
import datetime
my_birthday = datetime.date(2006, 3, 10)
print(p3.Birthday(my_birthday))
'''

# https://www.youtube.com/watch?v=3ohzBxoFHAY
# Python OOP Tutorial 5: Special (Magic/Dunder) Methods

# https://www.youtube.com/watch?v=jCzT9XFZ5bw&t=6s
# Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters

class Employee(object):
    """docstring for Employee."""

    raise_amt = 1.05

    def __init__(self, first, last, age, pay):
        super(Employee, self).__init__()
        self.first = first
        self.last = last
        self.age = age
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self,fllnm):
        self.first, self.last = fllnm.split(' ')

    @fullname.deleter
    def fullname(self):
        print('[!] Deleted name.')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f'Employee: {self.first}, {self.last}, pay: {self.pay}'

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        '''
        Devuelve el valor sumado de propio salario + el otro salario
        '''
        return self.pay + other.pay

    def __len__(self):
        '''
        Devuelve la longitud del fullname
        '''
        return len(self.fullname())

    def __wtf__(self,other):
        '''
        Devuelve el valor restado de las edades
        '''
        return self.age - other.age

emp_1 = Employee('Kevin', 'Pulido', 31, 50000)
emp_2 = Employee('Nico', 'Mejía',3, 45000)

'''
print(emp_1) # --> <__main__.Employee object at 0x000001F6330FF388>
print(str(emp_1))  # emp_1.__str__ --> Kevin Pulido - Kevin.Pulido@gmail.com
print(repr(emp_1)) # emp_1.__repr__ --> Employee: Kevin, Pulido, pay: 50000
print(emp_1+emp_2) # --> 95000
print(len(emp_1)) # --> 12
print(emp_1.__wtf__(emp_2)) # --> 28

emp_1.fullname = 'Andres Rodriguez'
print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)

del(emp_1.fullname)
print(emp_1.fullname)
'''

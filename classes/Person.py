import logging
class Person:
    __name: str
    __age: int
    __gender: str
    __salary: int

    def __init__(self):


    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_gender(self, gender):
        self.__gender = gender

    def get_salary(self, salary):
        self.__salary = salary

    def __calculate_salary(self):
        if self.__gender == 'Male':
            self.__salary = self.__salary * 10

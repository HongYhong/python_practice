class Person(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        if 0<=age<=200:
            self.__age = age
        else:
            raise ValueError('bad age')
hong = Person('hongfox',23)
print(hong.get_age())
print(hong.get_name())
hong.set_age(500)
print(hong.get_age())

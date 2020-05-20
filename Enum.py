from enum import Enum,unique

class Seasons(Enum):
    spring = 1
    summer = 2
    fall = 3
    winter = 4

@unique
class Gender(Enum):
    Male = 1
    Female = 2
class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

bart = Student('Bart', Gender.Male)
print(type(Student))
print(bart.gender)


Months = Enum('Months',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in Seasons.__members__.items():
    print(name,member.value)
for name2,member2 in Months.__members__.items():
    print(name2,member2.value)

print(Seasons['spring'])
print(Seasons.summer)
print(Seasons(3))
print(Seasons.spring.value)
print(Seasons.summer.name)

for season in Seasons:
    print(season)
import json
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

s = Student('hong',23,98)
string = json.dumps(s,default=lambda obj: obj.__dict__)
print(string)
t = json.loads(string)
print(t)
t = json.loads(string,object_hook=dict2student)
print(t)

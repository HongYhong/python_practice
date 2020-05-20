class Student(object):
    pass
def fn(self,name):
    print('hello %s'%name)
A = type('A',(object,),{'name':'hong'})
Hello = type('abc',(object,),dict(hello = fn))
print(A.name)
print(Student)
print(Hello)

h = Hello()
h.hello('hong')
print(h)

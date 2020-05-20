class Person(object):
    pass
def set_name(self,name):
    self.name = name
Person.set_name = set_name
hong = Person()
print(getattr(hong,'name',404))
hong.set_name('hongfox')
print(getattr(hong,'name',404))
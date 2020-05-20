class testobject(object):
    def __init__(self):
        self.x = 12
    def power(self):
        return self.x * self.x


obj = testobject()


fn = getattr(obj,'power')

print(fn())

print(hasattr(obj,'x'))

print(getattr(obj,'x'))

print(hasattr(obj,'y'))

setattr(obj,'y',13)

print(hasattr(obj,'y'))

print(getattr(obj,'y'))






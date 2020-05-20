d = {'__class__' : 'Student'}

className = d.pop('__class__', None)
cls = globals()[className]
print(cls)
print(className)
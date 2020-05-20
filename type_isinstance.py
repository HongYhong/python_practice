import types
def fn():
    pass
print(type(fn) == types.FunctionType)

class plant(object):
    pass
class flowers(plant):
    pass
class tree(plant):
    pass

print(type(tree()))

a = plant()
b = flowers()
c = tree()
print(isinstance(b,flowers))
print(isinstance(c,tree))
print(isinstance(a,plant))

print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))


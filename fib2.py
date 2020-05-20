class Fib(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            end = n.stop
            if start == None:
                start = 0
            a ,b = 0 ,1
            L = []
            for x in range(end):
                if x > start:
                    L.append(a)
                a,b = b,a+b
            return L

f = Fib()
print(f[0:5])

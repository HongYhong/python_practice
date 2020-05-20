class Student(object):
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
           raise ValueError("not an integer.")
        elif value<0 or value > 100:
            raise ValueError("out of range!")
        else:
            self.__score = value

hong = Student()
hong.score = 100
print(hong.score)
hong.score = 8888
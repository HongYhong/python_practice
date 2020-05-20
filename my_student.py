#my_student.py
class Student2(object):
    def __init__(self,name,score):
        self.name =name
        self.score = score
    def get_grade(self):
        if self.score > 100 or self.score < 0:
            raise ValueError('error:invalid score %s'%self.score)
        elif self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


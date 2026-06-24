class student :
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def printing(self):
        print(self.marks,self.name,self.roll)
s1=student("krish",23,45)
s1.printing()

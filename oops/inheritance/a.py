class student :
    name="krish"
    roll=45
    marks=4.34
    def printingss(self):
        print(self.marks,self.name,self.roll)
student.printingss(student)
#student.printing()will not work . as no argment is given 
s1=student()
s1.printingss() #this will work as argumnet automatciely by object is given 
s1.printingss(s1)#this will not work as thier are two argumnet bnoth are s1 and s1 . ,first is by pyhton automotaiclyy . seond is by us 


class student :
    name = "krish"
    roll= 13
    marks=100
    def printing(selfd):
        print(f"the name of student is {selfd.name} roll number : {selfd.roll} marks : {selfd.marks}")
student.printing(student)
krish=student()
krish.printing()
#we cant write student.printing()
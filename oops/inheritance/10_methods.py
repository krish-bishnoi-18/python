class student:
    name="krish"
    def show(self):
        print(f"name of person is {self.name}")
s1=student()
s1.name="krish2"
student.show(student)
student.show(s1)
s1.show()
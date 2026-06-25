class student :
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        print("these are thing inside the init funtion that why they are printing ")
    def printing(self):
        print(self.name,self.roll,"these are due to another printing printg funtions")
s1=student("krish",45)
s1.printing()

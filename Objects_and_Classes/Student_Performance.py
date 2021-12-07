class Student:
    def __init__(self,name = None,phy = 0,chem = 0,bio = 0):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
    #Method
    def totalObtained(self):
      return (self.phy+self.chem+self.bio)
    def percentage(self):
      return self.totalObtained()*100/300
#Tests 
student_1 = Student('Mark',80,90,40)
print(f"Name: {student_1.name}")   
print(f"Total marks of a student: {student_1.totalObtained()}")
print(f"Percentage: {student_1.percentage()}")

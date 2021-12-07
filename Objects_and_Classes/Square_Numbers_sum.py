class Point:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
    #Method
    def sqSum(self):
        return (self.x**2 + self.y**2 + self.z**2)
numbers = []
for i in range(3):
  aux = int(input(f"Number {i+1} :"))
  numbers.append(aux)  
Suma = Point(numbers[0],numbers[1],numbers[2])
print(f"Square Numbers and Return Their Sum: {Suma.sqSum()}")

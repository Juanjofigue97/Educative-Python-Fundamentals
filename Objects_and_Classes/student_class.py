class Student:
    def __init__(self,name,rollNumber):
        self.__name = name
        self.__rollNumber = rollNumber
    def setName(self,x):
        self.__name = x

    def getName(self):
        return self.__name

    def setRollNumber(self,y):
        self.__rollNumber = y

    def getRollNumber(self):
        return self.__rollNumber

# Test

Juan = Student('Juan',12)
Juan.setName('Marce')

#New name
Juan.getName()

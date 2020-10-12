class Employee:
    "Simple Python Class"

    empCount = 0 # Class variable shared among all objects

    def __init__(self,firstName,lastName,salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary # __salary means data hiding from outside world
        self.fullName = firstName + " " + lastName
        Employee.empCount+=1
        print("Initialised New User...",self.fullName)

    def displayInfo(self):
        print("Name : ",self.fullName)
        print("Salary : ",self.salary)

    def displayCount(self):
        print("Total Employees so far : ",Employee.empCount)


# this was the employee class definition
emp1=Employee("Shiladitya","Ganguly",2200000)
emp2=Employee("John","Wayne",1000000)

# emp1.bonus=100

emp1.displayInfo()
emp2.displayInfo()

emp1.displayCount()
# print(emp1.bonus)

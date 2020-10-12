class Employee:
    empcount = 0
    bonus = 300000

    def __init__(self, fname, lname, salary):
        self.firstName = fname
        self.lastName = lname
        self.salary = salary
        Employee.empcount += 1
        print("{} is initialised".format(fname))

    def displayInfo(self):
        print("----------------------")
        self.applyBonus()
        print("Name:", self.firstName, self.lastName)
        print("Salary:",self.salary)

    def applyBonus(self):
        self.salary += Employee.bonus


class Developer(Employee):
    # pass
    def __init__(self,fname,lname,salary,skills):
        # self.firstName=fname
        # self.lastName=lname
        # self.salary=salary
        super(Developer, self).__init__(fname,lname,salary)
        self.skills=skills

    def displayInfo(self):
        print("<---Developer--->")
        super(Developer, self).displayInfo()
        print("Skills:",self.skills)

class Tester(Employee):
    def __init__(self,fname,lname,salary,test_tools):
        super(Tester, self).__init__(fname,lname,salary)
        self.test_tools=test_tools

    def displayInfo(self):
        print("<---Tester--->")
        super(Tester, self).displayInfo()
        print("Tools:",self.test_tools)

        
emp1 = Developer("Shiladitya","Ganguly",1400000,"Java")
emp1.displayInfo()
emp2 = Tester("Lady","Gaga",1200000,"Selenium")
emp2.displayInfo()


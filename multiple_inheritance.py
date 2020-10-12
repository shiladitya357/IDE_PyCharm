class A:
    def display(self):
        print("This is A")

class B:
    def display(self):
        print("This is B")
# Depending on the order of classes the methods will be resolved
class C(B,A):
    def display(self):
        super(C, self).display()
        print("This is called from C")


cObj = C()
cObj.display()
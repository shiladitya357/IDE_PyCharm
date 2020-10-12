class MathUtils:
    " Utility class for mathematical operations"
    def_var = 10
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def subtract(a,b):
        return a-b

    @classmethod
    def add1(cls,a,b):
        return a+b

mu1=MathUtils()
print(mu1.add1(10,20))

print(MathUtils.add(10,20))
print(MathUtils.subtract(50,43))

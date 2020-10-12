def getInverse():
    try:
        num=int(input("Enter any number: "))
        inverse = 1/num
    except ValueError:
        print("Enter numbers only")
    except ZeroDivisionError:
        print("Division by zero error")
    except Exception as err:
        print("Unknown Error",err)
    else:
        print("The inverse is",inverse)


getInverse()
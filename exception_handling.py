def writeToFile(data):
    try:
        fp=open("Oracle.txt","r")
        fp.write(data)
    except FileNotFoundError as err:
        print("Error! File Does Not Exist, {}".format(err))
    except Exception: # generic Exception
        print("Unknown Error!")
    else:
        fp.close()
        print("Data written...")

writeToFile("Welcome to Oracle")
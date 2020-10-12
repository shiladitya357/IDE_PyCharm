def writeToFile(data):
    "Writes to 'Oracle1.txt'"
    fp = open("Oracle1.txt","a")
    fp.write(data)
    fp.write("---------\n")
    fp.close()

# writeToFile("Hello Oracle Employee\n")

def readFromFile():
    fp = open("Oracle1.txt","r")
    # data = fp.read()
    # print("First 10 : ",data)
    # fp.seek(0,0)
    # data = fp.read()
    # print("Next ",data)
    # data = fp.readlines()
    data = fp.read()
    print(data)
    fp.close()

readFromFile()

# os can be used for different modifications on file
# os.path documentation can be used
import os
# os.mkdir("demoDir")

print("Current dir : ",os.getcwd())

# os.chdir("D:/Program Files/Games")
entries = os.listdir(os.getcwd())
print(entries)

listOfFiles=[]
listOfDir=[]

for entry in entries:
    if os.path.isfile(entry):
        listOfFiles.append(entry)
    elif os.path.isdir(entry):
        listOfDir.append(entry)

print("Files are : ",listOfFiles)
print("Dirs are : ",listOfDir)
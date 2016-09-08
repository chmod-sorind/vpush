import datetime

now = datetime.datetime.now()
nowT = now.strftime("%H:%M:%S")


with open("time.txt", "a+") as testFile:
    testFile.write("Execution Time " + nowT +  "\n")
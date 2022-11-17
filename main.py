import os

while True:
    fileCheck = open("check.txt", "r")

    for line in fileCheck:
        if line == 'run':
            cmd = 'python test.py'
            os.system(cmd)
            fileCheck.close()
            tempFile = open("check.txt","w")
            tempFile.write("")
            



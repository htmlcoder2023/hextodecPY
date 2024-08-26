import os
import sys
lineArr = []
file = sys.argv[1]
if len(sys.argv) != 2:
    raise Exception("Expected 2 arguments, got " + str(len(sys.argv)) + "!")
if os.path.isfile(file):
    print("")
else:
    raise Exception("File not found!")
fileinput = open(file, "r")
while True:
    line = fileinput.readline()
    if not line:
        break
    line = int(line, 16)
    lineArr.append(line)
file = open(file, "w")
linesWritten = 0
for lines in range(len(lineArr)):
    if linesWritten == 0:
        file.write(str(lineArr[lines]))
        linesWritten += 1
    else:
        file.write("\n" + str(lineArr[lines]))
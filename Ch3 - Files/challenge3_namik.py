import os


byteCount = 0
fileNames = ""

fileList = os.listdir()
for f in fileList:
    if os.path.isfile(f):
        byteCount += os.path.getsize(f)
        fileNames += f + "\n"
myStr = "Total bytecount:"
myStr += str(byteCount) + "\n"
myStr += "Files list:\n"
myStr += "--------------\n"
myStr += fileNames

os.mkdir("results")
newfile = open("results/results.txt", "w+")
if newfile.writable():
    newfile.write(myStr)

newfile.close()

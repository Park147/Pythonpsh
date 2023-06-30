inFp = None 
inList = ""    

inFp = open("C:/Tempython/test.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")

inList = inFp.readlines()
print(type(inList))
print(inList)

inFp.close()

inFp = None 
inList, inStr = [],""    

inFp = open("C:/Tempython/test.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")

inList = inFp.readlines()
for inStr in inList :
    print(type(inList))
    print(type(inStr))
    print(inStr, end="")

inFp.close()
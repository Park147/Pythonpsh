#해당 파일 읽을 때 기본 인코딩, ANSI, 만약, utf-8 변경 할려면
#encoding="utf-8"로 변경해야함.
#

inFp = open("C:/CookAnalysis/CSV/singer1.csv", "r")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()
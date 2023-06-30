inFp, outFp = None, None 
inStr = ""
#rb binary로 read , wb
inFp = open("C:/Windows/write.exe", "rb")
outFp = open("C:/Temp/write.exe", "wb")

while True :
    inStr = inFp.read(1)
    if not inStr : # 잘 쓰이는 문법 존재유무 뒤가 true면 false고 뒤가 false면 true가 되어 break 반복문 밖으로!
        break
    outFp.write(inStr)

inFp.close()
outFp.close()
print("--- 이진 파일이 정상적으로 복사되었음 ---")

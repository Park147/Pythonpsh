print("안녕하세요?")
print("100")
print("%d" % 100)
print("100 + 100")
print("%d" % (100 + 100))

print("%d %d" % (100, 200))
print("%d" % (100))

print("%d / %d = %d" % (100, 200, 0.5))
print("%d / %d = %5.1f" % (100, 200, 0.5))
print("%d / %d = %1.1f" % (100, 200, 0.5))
print("%d / %d = %5.11f" % (100, 200, 0.5))

# - 서식에 따른 출력

# 정수형 데이터 출력
print("%d" % 123)
print("%5d" % 123)
print("%05d" % 123)

print("%d%5d%05d" % (123, 123, 123))
print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))
print("{2:d} {1:d} {0:d}".format(100, 200, 300))


# 실수형 데이터의 서식 지정
print("%f" % 123.45)
print("%7.1f" % 123.45)
print("%7.31f" % 123.45)
print("%7.3f" % 123.45)

# 문자형 데이터의 서식 지정
print("%s" % "Python")
print("%10s" % "Python")
print("%10s" % "ㅁㅂPythonㅍㅊㅊ")

print("한 행입니다. 또 한 행입니다.")
print("한 행입니다. \n또 한 행입니다.")

# 이스케이프 문자
print("\n줄바꿈\n연습 ")
print("\t탭키\t연습")
print('글자가 "강조"되는 효과1')
print("글자가 '강조'되는 효과2")
print("\\\\\\ 백슬래시 세 개 출력")
print(r"\n \t \" \\를 그대로 출력")

# 변수의 선언
boolVar = False
intVar = 100
floatVar = 123.45
strVar = "안녕?"

boolVar, intVar, floatVar, strVar = False, 100, 123.45, "안녕?"

# 변수의 사용
type(boolVar), type(intVar), type(floatVar), type(strVar)

var2 = 200
var1 = var2

var1 = 100 + 100
var1 = var2 + 100

var1 = var2 = var3 = var4 = 100

val1 = var1 + 200

noVar = noVar + 200

myVar = 100
type(myVar)
myVar = 100.0
type(myVar)

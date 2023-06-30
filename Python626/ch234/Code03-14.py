i=0
hap = 0

for i in range(1,11,1) :
    hap = hap + i

print("1에서 10까지의 합계 : %d" % hap)

i,hap = 0,0
for i in range(0, 101, 7) :
    hap = hap + i
print("0에서 100 사이의 7의 배수 합계 : %d" % hap)

# 전역변수 사용됨.
i,k = 0,0

# 따로 메인 함수가 없음. 코드가 짧아서, 단순, 순차적으로 실
# 코드가
for i in range(2,10,1):
    print (" ## %d단 ## " % i)
    for k in range(1,10,1) : # 바깥 for 문에서 순서1
        print("%d X %d = %2d" %(i, k, i * k))
    print("") # 바깥 for 문에서 순서2

hap, i = 0,0

for i in range(1,101) :
    if i % 3 == 0 :
        continue
    hap += i

print("1~100의 합계(3의 배수 제외) : %d" % hap)
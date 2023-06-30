aa = [0,0,0,0]
hap = 0

#setter
aa[0] = int(input("1번째 숫자 : "))
aa[1] = int(input("2번째 숫자 : "))
aa[2] = int(input("3번째 숫자 : "))
aa[3] = int(input("4번째 숫자 : "))

#getter
hap = aa[0] + aa[1] + aa[2] + aa[3]

print("합계 ==> %d" % hap)

#Code04-04.py
myList = [30, 10, 20]
print("현재 리스트 : %s" % myList)

myList.append(40)
print("append(40) 후의 리스트 : %s" % myList)

print("pop()으로 추출한 값 : %s" % myList.pop())
print("pop() 후의 리스트 : %s" % myList)

#sort 는 내림차순으로 정렬
myList.sort()
print("sort() 후의 리스트 : %s" % myList)
#sort의 반대
myList.reverse()
print("reverse() 후의 리스트 : %s" % myList)

print("20값의 위치 : %d" % myList.index(20))

myList.insert(2, 222)
print("insert(2, 222) 후의 리스트 : %s" % myList)

myList.remove(222)
print("remove(222) 후의 리스트 : %s" % myList)

#+와 비슷 
myList.extend( [77, 88, 77] )
print("extend([77, 88, 77]) 후의 리스트 : %s" % myList)

print("77값의 개수 : %d" % myList.count(77))

#Code 4-5
list1 = []
list2 = []
value=1
for i in range(0, 3) :
    for k in range(0, 4) :
        list1.append(value)
        value += 1
    list2.append(list1)
    list1 = []

for i in range(0, 3) :
    for k in range(0, 4) :
        print("%3d" % list2[i][k], end = " ")
    print("")

#Self Study 4-2
list1 = []
list2 = []
value=0
for i in range(0, 4) :
    for k in range(0, 5) :
        list1.append(value)
        value += 3
    list2.append(list1)
    list1 = []

for i in range(0, 4) :
    for k in range(0, 5) :
        print("%3d" % list2[i][k], end = " ")
    print("")



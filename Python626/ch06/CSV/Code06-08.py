import csv

with open("C:/CookAnalysis/CSV/singerA.csv", "r") as inFpA :
    with open("C:/CookAnalysis/CSV/singerB.csv", "r") as inFpB:
        with open("C:/CookAnalysis/CSV/singerSum.csv", "w", newline='') as outFp:
            # 참조 변수
            csvReaderA = csv.reader(inFpA)
            csvReaderB = csv.reader(inFpB)
            csvWriter = csv.writer(outFp)
            #singerA.csv 나 singerB.csv 양식이 같으므로 쉽게 합침
            header_list = next(csvReaderA)
            header_list = next(csvReaderB)
            # 만약, 헤더가 다르다면, 양식이 다르면, 출력할 헤더를 정해서
            # 해당 인덱스로 필터링하기. -> SELF STUDY 6-2
            csvWriter.writerow(header_list)
            #데이터 출력!
            for row_list in csvReaderA:
                csvWriter.writerow(row_list)
            for row_list in csvReaderB:
                csvWriter.writerow(row_list)

print('Save. OK~')
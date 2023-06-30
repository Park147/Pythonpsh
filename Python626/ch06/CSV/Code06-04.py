with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp :
    with open("C:/CookAnalysis/CSV/new_singer1.csv", "w") as outFp:
        #header : 아이디 이름 인원 주소 국번 전화 번호 평균 키 데뷔 일자
        header = inFp.readline()
        header = header.strip()
        header_list = header.split(',')
        header_str = ','.join(map(str, header_list))
        #, 하는 이유 csv파일 형식으로 읽으려고
        outFp.write(header_str + '\n')
        #헤더를 제외한 2번째 행부터 데이터
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(',')
            # -1, 해당 리스트의 마지막 요소. "데뷔 일자"
            row_list[-1] = row_list[-1].replace('.', '/')
            height_str = "{0:.2f}".format(int(row_list[-2]))
            row_list[-2] = height_str
            row_str = ','.join(map(str, row_list))
            outFp.write(row_str + '\n')

print('Save. OK~')
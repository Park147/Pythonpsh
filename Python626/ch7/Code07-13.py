from tkinter import *
import xlsxwriter
window = Tk()
photo = PhotoImage(file = 'C:/CookAnalysis/GIF/pic7.gif')
h = photo.height()
w = photo.width()

photoR=[ [0 for _ in range(h)] for _ in range(w)]
photoG=[ [0 for _ in range(h)] for _ in range(w)]
photoB=[ [0 for _ in range(h)] for _ in range(w)]

for i in range(w) :
    for k in range(h) :
        r, g, b = photo.get(i,k)
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b

workbook = xlsxwriter.Workbook('C:/CookAnalysis/Excel/picture06_art_0629.xlsx')
worksheet = workbook.add_worksheet('photoRGB')

#옵션, 각 셀의 크기를 작게 조정.
worksheet.set_column(0, w - 1, 1.0)  # 약 0.34
for i in range(h):
    worksheet.set_row(i, 9.5)  # 약 0.35

#10진수 -> 16진수로 변환하는 작업, 해당 HEX 결과의 값이 0xFF형식인데,
#만약, 2자리X. 1자리라면, 앞에 0을 붙여서 출력함!
for i in range(w) :
    for k in range(h) :
        hexR = hex(photoR[i][k]) #0xFF(255), 0x10(16) 만약 0xF(15)라면 -> 0x0F 이렇ㄱㅔ 함. 두자리 유지 위하여
        hexG = hex(photoG[i][k]) #0xFF
        hexB = hex(photoB[i][k]) #0xFF
        hexStr = '#'
        if len(hexR[2:]) < 2:
            hexStr += '0' + hexR[2:]
        else:
            hexStr += hexR[2:]
        if len(hexG[2:]) < 2:
            hexStr += '0' + hexG[2:]
        else:
            hexStr += hexG[2:]
        if len(hexB[2:]) < 2:
            hexStr += '0' + hexB[2:]
        else:
            hexStr += hexB[2:]
            
#셀 서식 -> 배경, -> hexStr #FFFFFF
        cell_format = workbook.add_format()
        cell_format.set_bg_color(hexStr)
        worksheet.write(k, i, '', cell_format)

workbook.close()
print('Save. OK~')
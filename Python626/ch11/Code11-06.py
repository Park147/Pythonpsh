import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

inFilename = 'C:/CookAnalysis/Excel/singer.xlsx'
outFilename = 'C:/CookAnalysis/Excel/singer_over630.xlsx'

df_seniro = pd.read_excel(inFilename, 'senior', index_col=None)
df_junior = pd.read_excel(inFilename, 'junior', index_col=None)

df_singer = pd.concat( [df_seniro, df_junior] )
print(df_singer)
df_singer_over6 = df_singer[df_singer['인원'] >= 6]

df_singer_over6 = df_singer_over6.sort_values(by=['인원'], axis=0, ascending=False)
df_singer_over6 = df_singer_over6.loc[:, ['아이디', '이름', '인원', '유튜브 조회수']]
print('정렬 적용 후')
print(df_singer_over6)

x_data = df_singer_over6['아이디']
y_data = df_singer_over6['인원']
print('시리즈 적용 후')
print(df_singer_over6)
colorAry = [ np.random.choice(['red', 'green', 'blue', 'brown', 'gold', 'lime', 'aqua', 'magenta', 'purple']) for _ in range(len(x_data))]
plt.bar(x_data, y_data, color=colorAry)
plt.show()

writer = pd.ExcelWriter(outFilename)
df_singer_over6.to_excel(writer, sheet_name='singer', index=False)
writer.close() # writer.save() 하면 오류남. writer._save()하면 응 난 안되.
print('Save. OK~')
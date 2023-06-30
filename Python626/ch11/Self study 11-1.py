import pandas as pd
import numpy as np

data = { '이름' : ['여자친구','소녀시대','레드벨벳','에이핑크','마마무'],
         '인원' : [6,8,4,6,4],
         '데뷔 일자' : ['2015.01.15','2007.08.02','2014.08.01','2011.02.10','2014.06.19']}
data_index = ['WMN', 'GRL', 'RED', 'APN', 'MMU']
# df1 = pd.DataFrame(data1)
# df1
# df2 = pd.DataFrame(data1, index=['WMN','GRL','RED','APN','MMU'])
# df2
df = pd.DataFrame(data, index =data_index)
print(df)

df = df.drop(['이름'], axis=1)
df = df.drop( ['GRL', 'RED', 'APN'])
df.loc['ABC'] = [1, '2023.03.03']
print(df)
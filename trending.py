
import pandas as pd
data0 = pd.read_csv('/home/schellamuthu/Sowmiya/upgrad/saavn/output/00.csv',header=None,usecols=[0,1,2], names=['songid', 'date', 'count'])
data1 = pd.read_csv('/home/schellamuthu/Sowmiya/upgrad/saavn/output/01.csv',header=None,usecols=[0,1,2], names=['songid', 'date', 'count'])
data2 = pd.read_csv('/home/schellamuthu/Sowmiya/upgrad/saavn/output/02.csv',header=None,usecols=[0,1,2], names=['songid', 'date', 'count'])
data3 = pd.read_csv('/home/schellamuthu/Sowmiya/upgrad/saavn/output/03.csv',header=None,usecols=[0,1,2], names=['songid', 'date', 'count'])

data=pd.concat([data0, data1, data2, data3])

gp_data = data.groupby('songid').size().reset_index(name='count')

gp_data = gp_data.sort(['count'], ascending=[False])

less_days = gp_data[gp_data['count'] > 30]

filtered_data1= data[data['songid'].isin(less_days['songid'])]


filtered_data1['date'] = pd.to_datetime(filtered_data1['date'])

expected = pd.read_csv('/home/schellamuthu/Sowmiya/upgrad/saavn/output/expected_data.csv')


# dec 25
dec25 = pd.to_datetime('2017-12-25')
trending_dec25_grouped = filtered_data1[filtered_data1['date'] < dec25]
trending_dec25_grouped= trending_dec25_grouped.groupby('songid')['count'].sum().reset_index(name='total')
trending_dec25_grouped = trending_dec25_grouped.sort(['total'], ascending=[False]).head(100)
print(len(trending_dec25_grouped.index))

# dec 26
dec26 = pd.to_datetime('2017-12-26')
trending_dec26_grouped = filtered_data1[filtered_data1['date'] < dec26]
trending_dec26_grouped= trending_dec26_grouped.groupby('songid')['count'].sum().reset_index(name='total')
trending_dec26_grouped = trending_dec26_grouped.sort(['total'], ascending=[False]).head(100)
print(len(trending_dec26_grouped.index))

# dec 27
dec27 = pd.to_datetime('2017-12-27')
trending_dec27_grouped = filtered_data1[filtered_data1['date'] < dec27]
trending_dec27_grouped= trending_dec27_grouped.groupby('songid')['count'].sum().reset_index(name='total')
trending_dec27_grouped = trending_dec27_grouped.sort(['total'], ascending=[False]).head(100)
print(len(trending_dec27_grouped.index))

# dec 28
dec28 = pd.to_datetime('2017-12-28')
trending_dec28_grouped = filtered_data1[filtered_data1['date'] < dec28]
trending_dec28_grouped= trending_dec28_grouped.groupby('songid')['count'].sum().reset_index(name='total')
trending_dec28_grouped = trending_dec28_grouped.sort(['total'], ascending=[False]).head(100)
print(len(trending_dec28_grouped.index))

# dec 29
dec29 = pd.to_datetime('2017-12-29')
trending_dec29_grouped = filtered_data1[filtered_data1['date'] < dec29]
trending_dec29_grouped= trending_dec29_grouped.groupby('songid')['count'].sum().reset_index(name='total')
trending_dec29_grouped = trending_dec29_grouped.sort(['total'], ascending=[False]).head(100)
print(len(trending_dec29_grouped.index))

# dec 30
dec30 = pd.to_datetime('2017-12-30')
trending_dec30_grouped = filtered_data1[filtered_data1['date'] < dec30]
trending_dec30_grouped= trending_dec30_grouped.groupby('songid')['count'].sum().reset_index(name='total')
trending_dec30_grouped = trending_dec30_grouped.sort(['total'], ascending=[False]).head(100)
print(len(trending_dec30_grouped.index))

# dec 31
dec31 = pd.to_datetime('2017-12-31')
trending_dec31_grouped = filtered_data1[filtered_data1['date'] < dec31]
trending_dec31_grouped= trending_dec31_grouped.groupby('songid')['count'].sum().reset_index(name='total')
trending_dec31_grouped = trending_dec31_grouped.sort(['total'], ascending=[False]).head(100)
print(len(trending_dec31_grouped.index))


expected['date'] = pd.to_datetime(expected['date'])
trending25 = expected[expected['date'] == dec25]
matched25 = trending_dec25_grouped[trending_dec25_grouped['songid'].isin(trending25['pid'])]
print('dec 25')
print(len(matched25.index))

trending26 = expected[expected['date'] == dec26]
matched26 = trending_dec26_grouped[trending_dec26_grouped['songid'].isin(trending26['pid'])]
print('dec 26')
print(len(matched26.index))

trending27 = expected[expected['date'] == dec27]
matched27 = trending_dec27_grouped[trending_dec27_grouped['songid'].isin(trending27['pid'])]
print('dec 27')
print(len(matched27.index))

trending28 = expected[expected['date'] == dec28]
matched28 = trending_dec28_grouped[trending_dec28_grouped['songid'].isin(trending28['pid'])]
print('dec 28')
print(len(matched28.index))

trending29 = expected[expected['date'] == dec29]
matched29 = trending_dec29_grouped[trending_dec29_grouped['songid'].isin(trending29['pid'])]
print('dec 29')
print(len(matched29.index))

trending30 = expected[expected['date'] == dec30]
matched30 = trending_dec30_grouped[trending_dec30_grouped['songid'].isin(trending30['pid'])]
print('dec 30')
print(len(matched30.index))

trending31 = expected[expected['date'] == dec31]
matched31 = trending_dec31_grouped[trending_dec31_grouped['songid'].isin(trending31['pid'])]
print('dec 31')
print(len(matched31.index))


trending_dec25_grouped['songid'].to_csv('/home/schellamuthu/Sowmiya/upgrad/saavn/trending/25.txt', header=False, index=False)
trending_dec26_grouped['songid'].to_csv('/home/schellamuthu/Sowmiya/upgrad/saavn/trending/26.txt', header=False, index=False)
trending_dec27_grouped['songid'].to_csv('/home/schellamuthu/Sowmiya/upgrad/saavn/trending/27.txt', header=False, index=False)
trending_dec28_grouped['songid'].to_csv('/home/schellamuthu/Sowmiya/upgrad/saavn/trending/28.txt', header=False, index=False)
trending_dec29_grouped['songid'].to_csv('/home/schellamuthu/Sowmiya/upgrad/saavn/trending/29.txt', header=False, index=False)
trending_dec30_grouped['songid'].to_csv('/home/schellamuthu/Sowmiya/upgrad/saavn/trending/30.txt', header=False, index=False)
trending_dec31_grouped['songid'].to_csv('/home/schellamuthu/Sowmiya/upgrad/saavn/trending/31.txt', header=False, index=False)
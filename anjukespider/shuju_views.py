import pandas as pd
from matplotlib.pylab import plt

pf = pd.read_csv('item.csv',encoding='utf-8',names=["area","age","floor","location","district","price","mode"])

pf = pf.drop_duplicates() # 除去相同行，返回新数据,不是在旧有的上面修改
# 数据清洗，删除空值的行
pf.dropna(subset=["price"])
pf.dropna(subset=["area"])

pf['total_price'] = pf['price'] * pf['area']/10000

# 郑州的房价平均值
print(pf.mean())

# 最贵的房子
print(pf["total_price"].max())
print(pf["total_price"].max())

# 最便宜的房子

print(pf["total_price"].min())


# 把房子价格从低到高进行输出，sort_values
print(pf['total_price'].sort_values(inplace=False))


pf_mean = pf.groupby('district')['price'].mean()
pf_count = pf.groupby('district')['price'].count()

plt.figure(figsize=(10,6))

plt.rc('font',family='SimHei',size=13)

plt.title(u'各区域平均房价')
plt.xlabel(u'郑州区域')
plt.ylabel(u'平均单位房价(万/米)')
plt.bar(pf_mean.index,pf_mean.values,color='g')
plt.show()

plt.figure(figsize=(10,10))
plt.rc('font',family='SimHei',size=13)
explode = [0]*len(pf_count)
explode[9] = 0.1
plt.pie(pf_count,radius=2,autopct='%1.f%%',shadow=True,labels=pf_count.index,explode=explode)
plt.axis('equal')
plt.title(u'各区域平均房子分布量')
plt.show()


pf_mean = pf.groupby('district')['total_price'].mean()
pf_count = pf.groupby('district')['total_price'].count()

plt.figure(figsize=(10,6))

plt.rc('font',family='SimHei',size=13)

plt.title(u'各区域平均总房价')
plt.xlabel(u'郑州区域')
plt.ylabel(u'平均房价(万)')
plt.bar(pf_mean.index,pf_mean.values,color='g')
plt.show()

#
# pf_means = pf.groupby('district')['mode'].mean()
# pf_counts = pf.groupby('district')['mode'].count()
#
# plt.figure(figsize=(10,6))
#
# plt.rc('font',family='SimHei',size=13)
#
# plt.title(u'各区域平均总房价')
# plt.xlabel(u'郑州区域')
# plt.ylabel(u'房子户型')
# plt.bar(pf_means.index,pf_means.values,color='g')
# plt.show()
#
# plt.figure(figsize=(10,10))
# plt.rc('font',family='SimHei',size=13)
# explode = [0]*len(pf_count)
# explode[9] = 0.1
# plt.pie(pf_counts,radius=2,autopct='%1.f%%',shadow=True,labels=pf_count.index,explode=explode)
# plt.axis('equal')
# plt.title(u'各区域平均房子户型分布量')
# plt.show()


import matplotlib.pyplot as plt
import csv
f=open('data분석 with python/seoul_temp.csv')
data=csv.reader(f)
next(data)
mx_temp=[]
for r in data:
    if r[-1] != '':
        mx_temp.append(float(r[-1]))
print(len(mx_temp))

plt.plot(mx_temp)

plt.show()
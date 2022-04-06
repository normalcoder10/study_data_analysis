import csv
f=open('data분석 with python/seoul_temp.csv')
data=csv.reader(f)
for r in data:
    print(r)
import csv
import matplotlib.pyplot as plt
f = open('card.csv')
data = csv.reader(f)
next(data)
data = list(data)
s_mon = [0, 0, 0]
for row in data:
    if row[-1] == '전표매입':
        mon, payment = int(row[0].split('-')[1]), int(row[-3])
        idx = mon - 10
        s_mon[idx] += payment

plt.rc('font', family='AppleGothic')
plt.title('10월 ~ 12월 지출 현황')
plt.bar(['10월', '11월', '12월'], s_mon, color = 'royalblue')
plt.show()
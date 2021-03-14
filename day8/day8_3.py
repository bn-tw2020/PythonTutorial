import csv
import matplotlib.pyplot as plt
f = open('card.csv')
data = csv.reader(f)
next(data)
data = list(data)

deli = [0, 0, 0]
taxi = [0, 0, 0]
for row in data:
    if row[-1] == '전표매입' and row[5] == '(주)우아한형제들':
        mon, payment = int(row[0].split('-')[1]), int(row[-3])
        idx = mon - 10
        deli[idx] += payment
    if row[-1] == '전표매입' and '택시' in row[5]:
        mon, payment = int(row[0].split('-')[1]), int(row[-3])
        idx = mon - 10
        taxi[idx] += payment


plt.rc('font', family = 'AppleGothic')
plt.title('10월 ~ 12월 배달 지출 현황')
plt.plot(['10월', '11월', '12월'], deli, color = 'red', label = '배달음식 지출액');
plt.plot(['10월', '11월', '12월'], taxi, color = 'indigo', label = '택시비 지출액');
plt.legend()
plt.show()
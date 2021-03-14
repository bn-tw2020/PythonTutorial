import csv
import operator
import matplotlib.pyplot as plt
f = open('card.csv')
data = csv.reader(f)
next(data)
data = list(data)

spending = {}
for row in data:
    if row[-1] == '전표매입':
        store, payment = row[-4], int(row[-3])
        if store not in spending.keys():
            spending[store] = payment
        else:
            spending[store] += payment

# print(spending)

top10 = sorted(spending.items(), key=operator.itemgetter(1), reverse = True)[:10]
top10_store, top10_amout = [], []
for t in top10:
    top10_store.append(t[0])
    top10_amout.append(t[1])

plt.rc('font', family = 'AppleGothic')
plt.title('10월 ~ 12월 지출 TOP 10')
plt.barh(top10_store, top10_amout, color='b')
plt.show()
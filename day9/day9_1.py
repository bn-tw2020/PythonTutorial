import csv
import matplotlib.pyplot as plt
f = open('LOCAL_PEOPLE_DONG_201912.csv')
data = csv.reader(f)
next(data)
data = list(data)

f2 = open('dong_code.csv')
code_data = csv.reader(f2)
next(code_data)
next(code_data)
code_data = list(code_data)


for row in data:
    for i in range(1, 32):
        if i <= 2:
            row[i] = int(row[i])
        else:
            row[i] = float(row[i])

for row in code_data:
    row[1] = int(row[1])


# # 행정동명과 행정동코드 연결하기
# # 알고리즘
# # 1. 사용자에게서 행정동명을 입력받아 변수(dong_name)에 저장하기
# # 2. 행정동코드 데이터(code_data)를 돌며 반복하기
# # 3. 행정동코드 데이터의 마지막 열인 행정동명(열 인덱스[-1])이 입력된 행정동명(dong_name)과 같다면
# # 4. 해당하는 행정동코드를 변수(dong_code)에 저장하기

dong_name = input('핫 플레이스가 위치한 행정동을 입력하세요 -->')
for row in code_data:
    if row[-1] == dong_name:
        dong_code = row[1]
print(dong_name, '-', dong_code, '을(를) 분석합니다.')

# population = [] # 시간대별 평균 인구저장할 변수
# for i in range(24):
#     population.append(0)
population = [0 for _ in range(24)]
for row in data:
    if row[2] == dong_code:
        time, p = row[1], row[3]
        population[time] += p
population = [p/31 for p in population]

plt.rc('font', family = 'AppleGothic')
plt.title(dong_name + ' 시간대별 평균 인구')
plt.plot(range(24), population, color='indigo') 
plt.xticks(range(24), range(24)) # x축 눈금
plt.xlabel('시간대') #x축 이름
plt.ylabel('평균인구수') #y축 이름
plt.show()

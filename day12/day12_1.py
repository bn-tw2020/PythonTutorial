from tkinter import *

root = Tk() # 창 생성
root.title('my first tkinter') # 창 제목
root.geometry('400x200+0+300') # 창 크기 조절
root.resizable(False, False) # 창의 크기를 변경할 수 없게


# 레이블로는 텍스트와 이미지를 표현
# label2 = Label(root, text='Hello', font=('AppleGothic', 20), fg='blue', bg='gray', width=20, height=5, anchor='se')
# label2.pack()

# 이미지 레이블만들기
# letsgetit = PhotoImage(file='letsgetit.png') # 이미지 객체만들기
# img_label = Label(root, image=letsgetit) # 레이블 객체 생성
# img_label.pack()

# 위젯 배치하기
# 사용법 : place(x=x좌표, y=y좌표)
# 절대 위치
# label1 = Label(root, text='절대위치 x = 200, y = 100')
# label1.place(x=200, y=100)

# 상대 위치
# label1 = Label(root, text='안녕하세요!', relief='groove') # groove는 테두리 설정
# label1.pack()
# label2 = Label(root, text='Hello!', relief='groove')
# label2.pack()
# label3 = Label(root, text='니 하오!', relief='groove')
# label3.pack()
# label4 = Label(root, text='봉쥬르!', relief='groove')
# label4.pack(side='bottom') # left, right, bootom, top


# 그리드
label1 = Label(root, text='안녕하세요!', relief='groove') # groove는 테두리 설정
label1.grid(row=0, column=0)
label2 = Label(root, text='Hello!', relief='groove')
label2.grid(row=0, column=1)
label3 = Label(root, text='니 하오!', relief='groove')
label3.grid(row=1, column=0)
label4 = Label(root, text='봉쥬르!', relief='groove')
label4.grid(row=1, column=1)

root.mainloop() # 창 띄우기


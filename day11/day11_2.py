# 클래스와 객체로 프로그램 작성하기

class Product:
    def __init__(self, n, p, s):
        self.name, self.price, self.stock = n, p, s

    def sold(self, count):
        self.stock -= count
        print(self.name, count, '개 팔림!')
        print('남은 재고 : ', self.stock)

class Member:
    def __init__(self, n, d):
        self.name, self.join_date = n, d
        self.purchase_list = []
        self.purchase_amount = 0

    def information(self):
        print('회원이름 : ', self.name)
        print('가입날짜 : ', self.join_date)
        print('구매내역 : ', self.purchase_list)
        print('누적 구매금액 : ', self.purchase_amount)

    def buy(self, product, count):
        print(self.name, '고객님이', product.name, count, '개 구매!')
        self.purchase_list.append(product.name)
        self.purchase_amount += (product.price * count)

# 물건 등록
socks = Product('socks', 1000, 10)
books = Product('books', 17500, 15)

# 회원 가입
Anna = Member('Anna', '20200420')
Grace = Member('Grace', '20200130')

Anna.buy(socks, 1)
socks.sold(1)

Anna.information()
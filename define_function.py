# 사용자 함수정의
# 함수정의
def calc_fun(a,b) :
    x = a
    y = b
    def plus() :
        p = x + y
        return p
    def minus() :
        m = x - y
        return m
    return plus,minus

p,m = calc_fun(10,20)
print('plus=',p())
print('minus=',m())

class calc_class :
    x = y = 0 # 변수초기화

    def __init__(self,a,b) :
        self.x = a
        self.y = b
    def plus(self) :
        p = self.x + self.y
        return p
    def minus(self) :
        m = self.x - self.y
        return m
obj = calc_class(10,20)
print('plus =',obj.plus())
print('minus =',obj.minus()) # 절대값 사용도 됨

#클래스의 구성요소

class Car :
    cc = 0
    door = 0
    carType = None # 자료형을 캐릭터형으로

    def __init__(self,cc,door,carType) :
        self.cc = cc
        self.door = door
        self.carType = carType


    def display(self) : # 메서드를 디스플레이로 사용
        print("자동차 %d cc이고 , 문짝은 %d,타입은 %s"%(self.cc,self.door,self.carType))

car1 = Car(2000,4,"승용차") # object 생성
car2 = Car(3000,5,"SUV")

car1.display()
car2.display()

#생성자

class multiply :
    x = y = 0

    def __init__(self,x,y): #생성자
        self.x = x
        self.y = y

    def mul(self):
        m = self.x * self.y
        return m

obj = multiply(10,20)
print('곱셈 =',obj.mul())

# 생성자 없는 클래스  다시해봐야함 에러 .Traceback (most recent call last):
#   File "<input>", line 16, in <module>
# TypeError: data() missing 1 required positional argument: 'y'

class multiply2 :
    x = y = 0

    def __init__(self):
        pass
    def data(self,x,y):
        self.x = x
        self.y = y

    def mul(self):
        m = self.x * self.y
        return m

obj = multiply2
obj.data(10, 20)
print('곱셈 = ',obj.mul())

#self

class multiply3 :

    def data(self, x, y) :
        self.x = x
        self.y = y
    def mul(self):
        result = self.x * self.y
        self.display(result)
    def display(self,result):
        print("곱셈 = %d"%(result))

obj = multiply3
obj.data(10,20)
obj.mul()

#클래스 멤버의 예 .

class DatePro :
    content = "날짜 처리 클래스"

    def __init__(self,year,month,day) :
        self.year = year
        self.month = month
        self.day = day
    def display(self):
        print("%d-%d-%d"%(self.year,self.month,self.day))

     @classmethod #클래스 함수로 호출이 되는 클래스 매서드
    def date_string(cls, dateStr):
        year = dateStr[:4]
        month = dateStr[4:6]
        day = dateStr[6:]

        print(f"{year}년,{month}월,{day}일")

date = DatePro(1995, 10, 25)
print(date.content)
print(date.year)
date.display()

DatePro.date_string('19951025')

# 캡슐화 __변수명 = 은닉화 ?

class Account :
    __balance = 0
    __accName = None
    __accNo = None

    def __init__(self,bal,name,no):
        self.__balance = bal
        self.__accName = name
        self.__accNo = no

    def getBalance(self): #계좌의 정보를 얻는다.
        return self.__balance,self.__accName,self.__accNo
    def deposit(self,money):
        if money < 0 :
            print('금액 확인')
            return
        self.__balance+= money

    def withdraw(self,money):
        if self.__balance < money :
            print('잔액 부족')
            return
        self.__balance -= money

#오브젝트 생성
acc = Account(1000,'홍길동','125-152-4125-41')
#계좌 정보 확인
bal = acc.getBalance()
print('계좌정보 : ',bal)

acc.deposit(500) #입금하기 #입금하려는 돈이  0보다 작으면 입금을 확인하라는 메세지가 출력됨.
bal = acc.getBalance()
print('계좌정보 : ',bal)

acc.withdraw(500) # 출금하기 # 출금하려는금액이 잔액보다 클경우 잔액부족이 PRINT
bal = acc.getBalance() #계좌 정보 확인하기
print('출금 :',bal)

# 부모클래스

class Super :
    name = None
    age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print('name : %s, age : %d'%(self.name,self.age))

sup = Super('부모',55)
sup.display()
# 자식 클래스

class Sub(Super) :

    def __init__(self,name,age,gender) : #method override (재정의)
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print('name : %s, age : %d, gender : %s'%(self.name,self.age,self.gender))

sub = Sub('자식',25,'여자')
sub.display()

# Super 클래스

class Parent :
    def __init__(self,name,job):
        self.name = name
        self.job = job

    def display(self):
        print('name : {}, job : {}'.format(self.name,self.job))

p = Parent('홍길동','회사원')
p.display()

#Super 클래스의 자식클래스
class Children(Parent) :
    gender = None
    def __init__(self,name,job,gender) :
        super().__init__(name,job)
        self.gender = gender
    def display(self):
        print('name : {}, job : {}, gender : {}'.format(self.name,self.job,self.gender))

chil = Children('이순신','해군 장군','남자')
chil.display()


#매서드의 재정의 부모클래스를 상속받아 자식클래스 두개의 매서드를 다르게 함수를 만든다.

# 1.부모클래스 정의하기

class Employee :
    name = None
    pay = 0

    def __init__(self,name) :
        self.name = name

    def pay_calc(self) :
        pass

# 2. 자식클래스 : 정규직

class Permanent(Employee) :
    def __init__(self,name) :
        super().__init__(name)
    def pay_calc(self,base,bonus) :
        self.pay = base + bonus
        print('총 수령액 : ',format(self.pay,'3,d'),'원')

# 3. 자식클래스 : 임시직

class Temporary(Employee) :
            def __init__(self,name) :
                super().__init__(name)
            def pay_calc(self,tpay,time) :
                self.pay = tpay * time
                print('총수령액 : ',format(self.pay,'3,d'),'원')

p= Permanent("이순신")
p.pay_calc(300000,20000)
t = Temporary("홍길동")
t.pay_calc(15000,80)

# 다형성
class Flight :
    def fly(self) :
        print('날다 , fly 원형 매서드')
class Airplane(Flight) :
    def fly(self) :
        print('비행기가 날다.')
class Bird(Flight) :
    def fly(self):
        print('새가 날다.')
class PaperAirplane(Flight) :
    def fly(self) :
        print('종이 비행기가 날다.')

#객체를 생성 부모객체 = 자식 객체(자식1,자식2)
flight = Flight()
air = Airplane()
bird = Bird()
paper = PaperAirplane()

# 다형성 확인해보기
flight.fly()
flight = air
flight.fly()
flight = bird
flight.fly()
paper.fly()

# 빌트인 모듈 사용하기
#리스트 열거형 객체 사용
lst = [1,3,5]
for i, c in enumerate(lst) :
    print('색인 : ',i,end = ' ')
    print('내용 : ',c)

dic = {'name' : '홍길동','job' : '회사원','addr':'서울시'}
for i, k in enumerate(dic) :
    print('순서 :',i,end = ' ')
    print('키 : ',k,end=' ') # 키값 출력
    print('값 : ',dic[k]) # 밸류 출력

# import 모듈 내장클래스 예
import datetime
from datetime import date,time

today = date(2021,10,23)
print(today)

print(today.year)
print(today.month)
print(today.day)

w =  today.weekday()
print('요일 정보 : ',w)

currTime = time(11,7,30)
print(currTime)

print(currTime.hour)
print(currTime.minute)
print(currTime.second)

isoTime = currTime.isoformat()
print(isoTime)

# scattering 모듈

#(1) 평균과 제곱근 모듈  import
from statistics import mean
from math import sqrt

#평균 함수
def Avg(data) :
    avg = mean(data)
    return avg

def var_sd(data) :
    avg = Avg(data)
    diff = [(d-avg)**2 for d in data]
    var = sum(diff) / (len(data)-1)
    sd = sqrt(var)
    return  var , sd

import testPackage2.scattering as s
# 테스트 파일인 패키지 폴더를 만든후 그안에 추가해주어야 한다.

data = [1,3,1.5,2,1,3.2]

print('평균 : ',s.Avg(data))

var,sd = s.var_sd(data)
print('분산 :', var)
print('표준편차 : ',sd)

#############################################################

# 프로그램 시작점 만들기

from statistics import mean
from math import sqrt

def Avg(data) :
    avg = mean(data)
    return avg

def var_sd(data) :
    avg = Avg(data)
    diff = [(d - avg)**2 for d in data]
    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)
    return var,sd

if __name__ == "__main__" :
    data = [1,3,5,7]
    print('평균 = ', Avg(data))
    var, sd = var_sd(data)
    print('분산  = ',var)
    print('표준편차 = ',sd)

# 프로그램 시작점 없음

from statistics import mean
from math import sqrt


def Avg(data):
    avg = mean(data)
    return avg


def var_sd(data):
    avg = Avg(data)
    diff = [(d - avg) ** 2 for d in data]
    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)
    return var, sd


data = [1, 3, 5, 7]
print('평균 = ', Avg(data))
var, sd = var_sd(data)
print('분산  = ', var)
print('표준편차 = ', sd)



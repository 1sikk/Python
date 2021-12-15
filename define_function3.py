# 사용자 정의 함수
# 모듈이있을땐 검증된 모듈을 사용하는 것이 안전하다.
import random

def userFuc1() :
    print('인수가 없는 함수')
    print('userFunc1')

userFuc1()

#인수가있는 사용자 정의 함수
def userFunc2(x,y) :
    print('userFunc2')
    z = x + y
    print('z =',z)

userFunc2(10,20)

# return이 있는 함수
def userFunc3(x,y) :
    print('userFunc3')
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y

    return tot, sub, mul, div

x= int(input('x입력 : '))
y= int(input('y입력 : '))

t,s,m,d = userFunc3(x,y)
print('tot =',t)
print('sub =',s)
print('mul =',m)
print('div =',d)

# 산포도 구하기

from statistics import mean, variance # 모듈 불러오기
from math import sqrt

dataset = [2,4,5,6,1,8]

def Avg(data) : #산술 평균 구하는 사용자 정의 함수
    avg = mean(data)
    return avg
print('산술평균 =',Avg(dataset))

def var_sd(data) :
    avg = Avg(data)
    diff = [(d-avg)**2 for d in data]
    var = sum(diff) / len(data)-1
    sd = sqrt(var)
    return var , sd
v,s = var_sd(dataset)
print('분산 =',v)
print('표준편차 =',s)

# 피타고라스 정의 [빗변의 제곱 = 밑변의제곱 + 높이의 제곱]

def pytha(s,t) :
    a = s**2 - t**2
    b = 2 * s * t
    c = s**2 + t **2
    print("3변의 길이 :",a,b,c)

pytha(2,1)

# 몬테 카를로 시뮬레이션
#단계 1 : 동전 앞면과 뒷면의 난수 확률분포 함수 정의
import random
def coin(n) :
    result = []
    for i in range(n) :
        r = random.randint(0,1)
        if (r == 1) :
            result.append(1)
        else :
            result.append(0)
    return result
print(coin(10))

# 단계  2  : 몬테카를로 시뮬레이션 함수 정의

def montaCoin(n) :
    cnt = 0
    for i in range(n) :
        cnt += coin(1)[0]

    result =cnt/n
    return result
print(montaCoin(10))
print(montaCoin(30))
print(montaCoin(100))
print(montaCoin(1000))
print(montaCoin(10000))

for i in range(6) :
    l=random.randint(0,9)
print(l)

# 가변인수 함수
# 1) 튜플형 가변 함수
def Func1(name,*names) :
    print(name)
    print(names)

Func1("홍길동","이순신","유관순")

import statistics

def statis(func,*data) :
    if func == 'avg':
        return mean(data)
    elif func == 'var':
        return variance(data)
    elif func == 'std':
        return stdev(data)
    else :
        return 'TypeError'
print('avg=', statis('avg',1,2,3,4,5))
print('var=', statis('var',1,2,3,4,5))
print('std =', statis('std',1,2,3,4,5))

# 딕트형 가변인수
def emp_func(name,age,**other) :
    print(name)
    print(age)
    print(other)

emp_func('홍길동',35,addr='서울시',height = 175,weight=65) # 이름과 나이 프린트후 딕트로 키 :벨류 값으로 묶임

# 람다함수와 일반 함수 비교하기
def Adder(x,y) :
    add = x + y
    return add
print('add =',Adder(10,20))
#람다 함수
print('add=',(lambda x,y:x+y)(10,20))
# 스코프
x= 50 # 전역변수
def local_fuc(x):
    x +=50 # 지역변수의 종료 시점 local_fuc 은 100의 값을 갖는다.
local_fuc(x)
print('x=',x)

def global_fuc() :
    global x # 전역변수 x를 사용 바깥쪽에서 선언된 전역변수 x를 사용하겠다는 의미.
    x += 50
global_fuc()
print('x=',x)

#중첩 함수
# 일급함수
def a() :
    print('a 함수')
    def b() :
        print('b 함수')
    return b
b = a()
b()

# 함수 클로저
data = list(range (1,101))
def outer_func(data) :
    dataset = data
    def tot():
        tot_val = sum(dataset)
        return  tot_val
    def avg(tot_val) :
        avg_val = tot_val / len(dataset)
        return avg_val
    return tot,avg

tot, avg = outer_func(data)
tot_val =tot()
print('tot =',tot_val)
avg_val = avg()
print('avg =',avg_val)

# 산포도를 구하는 중첩함수
from statistics import mean
from math import sqrt

data = [4,5,3.5,2.5,6.3,5.5]

def scattering_func(data) :
    dataset = data
    def avg_func():
        avg_val = mean(dataset)
        return avg_val
    def var_func(avg) :
        diff = [(data - avg)**2 for data in dataset]
        #print(sum(diff))
        var_val=sum(diff)/(len(dataset)-1)
        return var_val

    def std_func(var) :
        std_var = sqrt(var)
        return std_var
    return avg_func, var_func, std_func

avg,var,std = scattering_func(data) #### 전체함수를 호출

print('평균 :',avg())
print('분산 :',var(avg()))
print('표준편차:',std(var(avg())))

# 중첩함수 정의
def main_func(num):
    num_val = num
    def getter():
        return num_val
    def setter(value) :
        nonlocal num_val
        num_val = value

    return getter, setter

getter,setter = main_func(100)

print('num =',getter())

setter(200) # num 값을 수정한다.
print('num = ',getter())

# 함수 장식자 wraper function
def wrap(func):
    def decorated():
        print('방가워요!')
        func() # 사이에 들어갈 함수
        func()
        print('잘가요!')
    return decorated()
@wrap
def hello() :
    print('hi~',"홍길동")

# 숫자 카운트 하기

def Counter(n):
    if n == 0 :
        return 0
    else :
        Counter(n-1)
        print(n,end='')

print('n=0 :', Counter(0))
Counter(5)

# 누적합

def Adder(n) :
    if n == 1 :
        return 1
    else :
        result = n + Adder(n-1)

        print(n,end ='')
        return result

    print('n=1', Adder(1))
    print('\nn-5:',Adder(5))
    




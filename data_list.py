
# 순서 자료 구조

str_var = str(object='string')
print(str_var)
print(type(str_var))
print(str_var[0])

str_var2 = 'string'
print(str_var2)
print(type(str_var2))

#리스트 객체는 인덱스를 이용하여 자료를 참조 할수 있음/

lst = [1,2,3,4,5]
print(lst)
print(type(lst))
for i in lst :
    print(lst[:i])

x = list (range(1,11))
print(x)
print(x[:5])
print(x[-5:])
print(x[::2])

#단일 list
a=['a','b','c']
# 중첩 list
b= [10,20,a,5,True,'문자열']
print(b[0])
print(b[2])
print(b[2][0]) # 중첩리스트 안의 리스트의 인덱스를 볼수있다.

#추가 삭제 수정 삽입

num = ['one','two','three','four']
print(num)
print(len(num))
num.append('five') # five 추가 맨 오른쪽에 붙음.
print(num)
num.remove('five') # five 삭제
print(num)
num.insert(0,'zero') # 삽입은 위치 지정후 넣어줄수 있음.
print(num)

#  리스트 결합
x= [1,2,3,4]
y = [1.5,2.5]
z =  x + y
print(z)
#x를 확장하기
x.extend(y)
print(x)
# 추가
x.append(y)
print(x)
# 리스트 두배확장
lst = [1,2,3,4]
result = lst*2
print(result)

# 리스트 정렬해주기
print(result)
result.sort() #오름차순 1 1 2 2 3 3 4 4
print(result)
result.sort(reverse=True) # 내림 차순 44 33 22 11 # reverse = 역순
print(result)

#리스트 요소 검사

import random
r = []
for i in range(5) :
    r.append(random.randint(1,5))
print(r)
if 4 in r :
    print('있음')
else:
print('없음')

# 변수 = [값1(True) If 조건 else 값2(False) for 변수 in 열거형객체 ]

x= [2,4,1,5,7]

lst = [i**2 for i in x]
print(lst)

# 1~ 10까지 2의배수
num= list(range(1,11))
lst2 = [i*2 for i in num if i % 2 == 0]
print(lst2)

#튜플형
t = (1,)

t2= (1,2,3,4,5,3)
print(t2)
print(type(t2))
# 괄호가 있든 없든 데이터들이 콤마로 이어지면 튜플로 인식.
t3 = 1,2,3,4
print(t3)
print(type(t3))

print(t2[0],t2[1:4],t2[-1])

# 튜플은 수정이안되므로 ERROR
t2[0] = 5

#요소 반복, 검사는 가능하다.
for i in t2:
    print(i,end=' ') #엔드 옵션이 있으면 붙여쓴다.

if 6 in t2:
    print("6 있음")
else :
    print("6 없음")

t4 = 1,9,4,3

t5 = t4[1],t4[2]

print(t5)
# 튜플 관련 함수

lst = list(range(1,6))
t3 = tuple(lst)

print(t3.count(3))
print(t3.index(4))

# list = [] tuple = () set = {}
#set 객체 . 비순서 자료구조
s = {1,3,5,3,1}
print(len(s))
print(s)
# 순서는 상관하지않기때문에 오름차순으로 표기를해준다.

for d in s:
    print(d, end= '')

# 집합 함수
s2 = {3,6}
print(s.union(s2)) # s 와 s2의 합집합
print((s.difference(s2))) # s 와 s2의 차집합
print(s.intersection(s2))# s와 s2의 교집합.

s3 = {1,3,5}
s3.add(7)
print(s3)

gender = ['남','여','남','여']

sgender = set(gender)
lgender = list(sgender)
print(lgender)
# set 형으로 변환하게되면 중복된 원소는 사라지고 중복되지 않은 원소만 남음.

#딕트형

dic = dict(key1 = 100,key2 = 200 , key3 = 300)
print(dic)

person = {'name':'홍길동','age':35,'address':'서울시'}
print(person)
#  Key : value #
#딕트 구조 파악

dic = dict(key1 = 100 , key2 = 200, key3 = 300)
print(dic)

person = {'name':'홍길동' ,'age':35,'address':'서울시'}
print(person)
print(person['name']) # 비순서형 구조 , [key]값을 입력하면 value를 보여줌.
print(type(dic))
print(type(person))
a = list(person) # list화 하면 key값만 보여줌
print(a)
person['age'] = 45 value값 변경
print(person)
del person['address'] # key값을 없애면 value값도 같이 없어진다.
print(person)
person['pay'] = 350 # 변수에 키,벨류값 추가
print(person)
#요소 검사
print('age' in person)

for key in person.keys() : # 키확인
    print(key)
for value in person.values() : # 벨류확인
    print(value)
for i in person.items() : # 키 , 벨류 확인
    print(i)
print(person)

# 빈도수 구하기
charset = ['abc','code','band','band','abc']
wc = {}

for key in charset :
wc[key] = wc.get(key,0) + 1
print(wc)

name = ['홍길동','이순신','강감찬']
print('name address =', id(name))

name2 = name
print('name2 address =',id(name2))

name2[0] = '김길동'
print(name)
print(name2) # 두개의 주소값이 같다 같이 변함

import copy
name3 = copy.deepcopy(name) # 똑같은 내용이지만 별도의 공간에 생성됨
print(name)

print('name adress =', id(name))
print('name adress= ', id(name3))
name[1] = '이순신 장군'
print(name)
print(name3)


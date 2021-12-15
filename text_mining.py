# 문장과 단어 추출

string = '''나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다.'''

sents = []
words = []
for sen in string.split(sep='\n') : ### 구분 줄바꿈으로 스플릿
    sents.append(sen)

for word in sen.split() :
    words.append(word)

print('문장 :', sents)
print('문장수 :', len(sents))
print('단어 : ', words)
print('단어의수 : ',len(words))

# 텍스트마이닝
import re
from re import findall

st1  = '1234 abc홍길동 ABC_555_6 이다도시'

print(findall('1234',st1)) #['1234']
print(findall('[0-9]', st1)) # ['1', '2', '3', '4', '5', '5', '5', '6']
print(findall('[0-9]{3}',st1)) # ['123','555']
print(findall('[0-9]{3,}',st1)) #['1234', '555']
print(findall('\\d{3}',st1)) #['123', '555']

print(findall('[가-힣]{3,}',st1)) # ['홍길동', '이다도시']
print(findall('[a-z]{3}',st1))  # ['abc']
print(findall('[a-z|A-Z]{3}',st1)) #['abc', 'ABC']

st2 = 'testlabcABC 123mbc 45test'

#접두/접미어

print(findall('^test',st2)) #접두어
print(findall('st$',st2)) #접미어

#종료문자찾기

print(findall('.bc',st2))  #bc로 끝나는걸 찾음

#시작문자 찾기

print(findall('t.',st2)) # .을더붙이면 이후에 추가로 더찾을수있음

st3 = 'test^홍길동 abc 대한*민국 123$tbc'
words = findall('\\w{3,}',st3) # 3단위 이상 텍스트 끊어냄 #\\w 한글+숫자+영문 모두포함.
print(words)

print(findall('[^^*$]+',st3)) # 특수문자 제외

#문자열검사 match
from re import match

jumin = '123456-3234567'
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
print(result)

if result :
    print('주민번호 일치')
else :
    print('잘못된 주민번호')

jumin = '123456-5234567'
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
print(result)
if result :
    print('주민번호 일치')
else :
    print('잘못된 주민번호')

#문자열 치환

from re import sub

st3 = 'test^홍길동 abc 대한*민국 123$tbc'

#특수문자 제거

text1 = sub('[\^*$]+', '', st3) #역슬래시 쓴이유는 일반 특수문자로 인식하기위함.
print(text1)
test2 = sub('[0-9]', '', text1)
print(test2)

#텍스트 처리

from  re import split,match,compile

multi_line = """http://www.naver.com
http://www.daum.net
www.hongkildong.com"""

web_site = split("\n",multi_line) #split("pattern",string)
print(web_site)

pat = compile("http://")

sel_site = [site for site in web_site if match(pat,site)] # pat를 파라미터로 사용
print(sel_site)

# 자연어 전처리

from re import findall,sub

texts = ['우리나라   대한민국,우리나라%$만세','비아그&라 500GRAM 정력 최고!','나는 대한민국 사람','보험료 15000원에 평생 보장 마감 임박','나는 홍길동']

texts_re1 = [t.lower() for t in texts] #소문자로 변경
print('tests_re1 : ',texts_re1)

texts_re2 = [sub('[0-9]', '', text) for text in texts_re1] #숫자제거
print(texts_re2)

texts_re3 = [sub('[,.?!:;]', '', text) for text in texts_re2] #문장부호 제거
print(texts_re3)

spec_str = '[@#$%^&*()]'
text_re4 = [sub(spec_str, '', text) for text in texts_re3]
print(text_re4)

text_re5 = [''.join(findall('[^a-z]', text)) for text in text_re4] #영문자 제거
print(text_re5)

text_re6 = [' '.join(text.split()) for text in text_re5]
print(text_re6)

# 전처리 함수를 만들기.

from re import findall,sub

texts = ['우리나라   대한민국,우리나라%$만세','비아그&라 500GRAM 정력 최고!','나는 대한민국 사람','보험료 15000원에 평생 보장 마감 임박','나는 홍길동']

def  clean_text(text) :

    text_re = text.lower
    text_re2 = sub('[0-9]','',text_re)
    text_re3 = sub('[,.?!;:]', "", text_re2)
    text_re4 = sub('[@#$%^&*]', '',text_re3)
    text_re5 = sub('[a-z]', '', text_re4)
    text_re6 = ' '.join(text_re5.split())
    return text_re6

texts_result = [clean_text(text) for text in texts]
print(texts_result)


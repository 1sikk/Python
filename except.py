# 예외 발생코드

print('프로그램 시작 !!!')
x = [10,30,25.2,'num',14,51]

for i in x :
    print(i)
    y = i**2
    print('y = ',y)

print('프로그램 종료') # 중간에 에러가 발생되면 이후에 처리가 되지 않음\

print('프로그램 시작!!!')

#예외 처리 코드를 사용!
#에러가 발생하면 예외로 인식하고 스킵후 다음 for문 출력
print('프로그램 시작 !!!')

for i in x :
    try :
        y = i**2
        print('i=',i, 'y=',y)
    except :
        print('숫자 아님',i)

print('프로그램 종료')

#유형별 예외 처리
print('\n유형별 에러 처리')
try:
    div = 1000/2.53
    print('div = %5.2f'%(div))
    div = 1000/0
    f = open('c:\\test.txt')
    num = int(input('숫자입력 : '))
    print('num =', num)

except ZeroDivisionError as e :
    print('오류정보 :', e)
except FileNotFoundError as e :
    print('오류정보 :',e)
except Exception as e :
    print('오류정보 :',e)

finally:
    print('finally 영역 - 항상 실행되는 영역')

#텍스트파일 입출력

import os
print('\n현재경로 :', os.getcwd())

try :
    ftest1 = open('Dataset/data/ftest.txt',mode= 'r')
    print(ftest1.read())
    ftest2 = open('Dataset/data/ftest2.txt',mode = 'w')
    ftest2.write('my first text~~~~~~')
    ftest3 = open('Dataset/data/ftest2.txt',mode= 'e')
    ftest3.write('\nmy second text ~~~')
except Exception as e:
    print('Error 발생 : ', e)
finally:
    ftest1.close()
    ftest2.close()
    ftest3.close()


# 파일 읽기 관련함수
try :
    ftest = open('Dataset/data/ftest.txt',mode='r')
    full_text = ftest.read()
    print(full_text)
    print(type(full_text))

    ftest = open('Dataset/data/ftest.txt', mode='r')
    lines = ftest.readlines()
    print(lines)
    print(type(lines))
    print('문단수 : ',len(lines))

    docs = []
    for line in lines :
        print(line.strip())
        docs.append(line.strip())

    print(docs)

    ftest = open('Dataset/data/ftest.txt', mode='r')
    line = ftest.readline()
    print(line)
    print(type(line))

except Exception as e :
    print('Error 발생:', e)

finally:
    ftest.close()


# os 모듈 파일

import os

os.getcwd()

os.chdir('Dataset')
os.getcwd()

#작업 디렉터리목록 리스트화
os.listdir('.')

#test 디렉터리 생성
os.mkdir('test')
os.listdir('.')

os.makedirs('test2/test3')
os.listdir('.')

os.chdir('test2')
os.listdir('.')
#디렉터리 이동
os.chdir('../')
os.getcwd()

#경로 표현함수

import os.path

os.getcwd()
#경로 변경
os.chdir('Dataset')
os.getcwd()
#경로의 존재 유무
os.path.exists('c:/Users/Nam/PycharmProjects/pythonProject2')
#파일의 유무 확인
os.path.isfile


#glob 모듈
import glob
glob.glob('test*.py')

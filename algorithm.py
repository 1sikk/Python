#알고리즘 최댓값/ 최솟값
import random
dataset = []
for i in range(10) :
    r = random.randint(1,100)
    dataset.append(r)
print(dataset)

vmax = vmin = dataset[0]

for i in dataset: # 첫번째 인덱스부터 순차적확인 알고리즘.
    if vmax < i :
        vmax = i
    if vmin > i :
        vmax = i

# vmax vmin dataset
# =================
# [0]   [0]   [0]
# [1]   [1]   [1] 작은지 큰지 비교
print('max =',vmax,'min =',vmin)

dataset = [3,5,1,2,4]
n = len(dataset)
for i in range(0,n-1) :
    for j in range(i+1,n) :
        if dataset[i] > dataset[j] :
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp
    print(dataset) # 바뀌는 과정
print(dataset) # 결과

dataset = [3,5,1,2,4]
n =  len(dataset)
for i in range(0,n-1):
    for j in range(i+1 , n) :
        if dataset[i] < dataset[j] :
            tmp = dataset
            dataset [i] = dataset[j]
            dataset[j] = tmp
    print(dataset)
print(dataset)

# 이진 검색 알고리즘

dataset = [5,10,18,22,35,55,75,103]
value = int(input('검색할 값 입력 : '))
low  = 0  # 시작점
high = len(dataset) # 끝지점
loc = 0 # mid
state = False # 찾는값이 없을때

while(low<=high) :
    mid = (low + high) // 2

    if dataset[mid] > value :
        high = mid - 1
    elif dataset[mid] < value :
        low = mid + 1
    else :
        loc = mid
        state = True
        break
if state :
    print('찾은위치 : %d 번째'%(loc+1))
else:
    print('찾는 값은 없습니다.')


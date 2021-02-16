## 2.2 파이썬 기본

### 2.2.2 파이썬 제어문

> 프로그램 내부 코드는 동작 행위와 상태로 구분되어 있다고 했습니다. 앞서 배운 자료형은 데이터의 상태를 나타내기 위해 사용합니다.
>
> 데이터의 상태를 참조하면서 코드의 흐름을 제어해야 우리가 원하는 프로그램을 개발할 수 있습니다.

</br>

#### if 조건문

- 주어진 조건을 판단했을 때 논리적으로 `참(True)`인 경우에만 조건문을 수행
- 주의 할 점은 if 조건문에 포함 된 코드들은 들여쓰기를 해야 한다는 점이다
  - 파이썬은 들여쓰기(`tap`)를 통해 코드를 묶기 때문
- 조건문 다음에는 반드시 콜론`:`을 사용 함

```python
>>> dist = 300
>>> if dist >= 0 and dist <= 50:
...     print('1000won')
... elif dist > 50 and dist <= 100:
...     print('2000won')
... else:
...     print('Over 3000won')
...
Over 3000won
```

> 조건식이 여러 개인 경우 제일 처음 if문이 False라면 순차적으로 그 다음 elif를 조사하고, 모두 False라면 마지막으로 else 구문이 진행 됩니다.

<br/>

- 조건문에 사용하는 연산자

<br/>

| 연산자  | 설명                                 |
| ------- | ------------------------------------ |
| A == B  | A와 B가 동일하면 결과는 True         |
| A != B  | A와 B가 동일하지 않으면 결과는 True  |
| A and B | A와 B가 모두 True면 결과는 True      |
| A or B  | A와 B 중 하나라도 True면 결과는 True |
| A       | A가 True면 결과는 True               |
| not A   | A가 True가 아니면 결과는 True        |
| A > B   | A가 B보다 크면 결과는True            |
| A >= B  | A가 B보다 크거나 같으면 결과는 True  |
| A < B   | A가 B보다 작으면 결과는 True         |
| A <= B  | A가 B보다 작거나 같으면 결과는 True  |

<br/>

#### while 반복문

- 주어진 조건이 거짓(False)이 될 때까지 반복해서 코드 수행
  - 해당 조건이 참(True)인 동안 반복문에 포함된 코드를 반복해서 수행(Loop)

- 반복 할 코드를 들여쓰기로 구분해야 함
- 조건이 False가 되지 않으면 무한 반복(무한 루프)에 빠지게 됨
  - 무한루프를 처리하느라 자원을 많이 사용해서 시스템이 느려질 수 있음
  - 인터프리터를 이용한 실습 중 무한루프에 빠지면 `Ctrl + C`를 눌러 탈출

<br/>

##### while 반복문 사용

```python
>>> i = 1
>>> while i <= 10:
...     print('i=%d' % i)
...     i = i + 1
...
i=1
i=2
i=3
i=4
i=5
i=6
i=7
i=8
i=9
i=10
```

- 문자열 포매팅을 이용 해 변수의 자료형에 맞는내용을 표현할 수 있다.

| 문자열 포매팅 | 설명        |
| ------------- | ----------- |
| %d            | 10진수 출력 |
| %x            | 16진수 출력 |
| %o            | 8진수 출력  |
| %f            | 실수 출력   |
| %s            | 문자열 출력 |

<br/>

##### 무한 루프 사용

```python
>>> while True:	# 무한루프
...     print('input number : ')
...     menu = int(input())
...     if menu == 0 : break	# 무한루프 중단
...     elif menu == 1 : print('number one')
...     elif menu == 99: continue	# 검사 없이 다음 루프 반복
...     elif menu == 2 : print('number two')
...     else : print('another number')
...
input number :
1
number one
input number :
2
number two
input number :
3
another number
input number :
99
input number :
0
>>>
```

<br/>

#### for 반복문

- 리스트, 튜플, 문자열에서 요소를 하나씩 꺼내 사용할 때는 for 반복문 사용

<br/>

##### for 반복문 사용

```python
>>> numbers = [1,2,3,4,5]
>>> for n in numbers:
...     print(n)
...
1
2
3
4
5
```

- 주어진 리스트, 튜플, 문자열 등의 요소를 대상으로 처음부터 끝까지 반복함

<br/>

##### range()함수 이용

```python
>>> numbers = [1,2,3,4,5]
>>> for n in range(1,3):
...     print(n)
...
1
2

# 또는 아래처럼 값 지정시 사용 가능

>>> number = range(1,6)
>>> for n in numbers:
...     print(n)
...
1
2
3
4
5
```

- 인자로 사용하는 값을 생략시 0부터 끝가지
- 인자 값은 (여기 부터, 여기미만까지)
  - 다시 말해서 (1,6)은 인덱스 1번 요소부터 5번까지

<br/>

##### 여러 개의 변수에 자동 대입

```python
>>> cord = [ (0,0), (10,15), (20,25) ]
>>> for x,y in cord:
...     print(x,y)
...
0 0
10 15
```

- 튜플이 아니더라도 여러 개의 요소를 가지는 자료형이면 자동으로 변수에 대입 됨
  - 요소 수와 대입 될 변수의 개수는 같아야 함

<br/>

##### 딕셔너리의 key() 함수를 이용해 for문으로 출력하기

```python
>>> user = {'name':'kei', 'age':35, 'nationality': 'Korea'}
>>> user.keys()
dict_keys(['name', 'age', 'nationality'])

# 위 key()함수 기능을 사용해 for 반복문으로 출력하기

>>> user = {'name':'kei', 'age':35, 'nationality': 'Korea'}
>>> for k in user.keys():
...     print(k)
...
name
age
nationality

```

<br/>

##### 딕셔너리의 items() 함수를 이용해 for문으로 출력하기

```python
>>> user = {'name':'kei', 'age':35, 'nationality': 'Korea'}
>>> user.items()
dict_items([('name', 'kei'), ('age', 35), ('nationality', 'Korea')])

# 위 items()함수 기능을 사용해 for 반복문으로 출력하기

>>> user = {'name':'kei', 'age':35, 'nationality': 'Korea'}
>>> for k,b in user.items():
...     print(k,v)
...
name Korea
age Korea
nationality Korea
```

<br/>

### 2.2.3 함수

> 함수란 하나의 기능을 수행하는 코드들의 집합입니다. 반복적으로 수행하는 코드들을 기능 단위로 묶어서 재사용할 수 있도록 구성한 겁니다.
>
> 잘 짜인 함수는 단 하나의 목적을 가지며, 함수명으로 그 함수의 역할을 유추할 수 있어야 합니다.
>
> 코드는 기본적으로 입력값과 결괏값을 가집니다. 입력값과 결괏값이 없는 함수도 존재합니다.

<br/>

#### 사용자 정의 함수

- 사용자가 만들어 사용
  - 따지고 보면 시스템 내장 함수, 외장 함수 모두 사용자 정의 함수라서 기본적으로 동일한 형태
- 들여쓰기를 이용해 함수에 포함 된 코드들을 묶음
- def 예약어를 사용해 함수를 정의

<br/>

##### 결괏값 반환 함수

```python
>>> def add(a,b):	# 함수 선언
...     return a+b	# 수행 결과
...
>>> add(10,20)
30
```

- 경우에 따라 인자와 결괏값 생략 가능

<br/>

##### 결괏값 반환하지 않은 함수

```python
>>> def print_user(name, age, score):
...     print("name : %s" % name)
...     print("age : %d" % age)
...     print("score : %d" % score)
...
>>> score = 65
>>> print_user('kei', 35, score)
name : kei
age : 35
score : 65
```

- 본문에서는 딕셔너리를 사용하지만 인터프리터에서 키 값을 못찾길래 그냥 입력하는 예제로 임의 변경

<br/>

#### 내장 함수

- 시스템에 내장되어 바로 사용
- 이미 탑재되어 있기에 별도로 모듈 import, 함수 정의 등을 하지 않고 사용 가능

<br/>

##### format()

- % 형식자를 이용한 문자열 포매팅과 format()함수를 이용해 문자열 포매팅 가능
- 기본적으로 동일한 기능을 하며, 변수 타입과 상관 없이 중괄호{}와 순서에 맞는 인덱스만 사용하면 됨

```python
>>> print('integer : {} / float : {} / string : {}'.format(10, 3.14, "hello"))
integer : 10 / float : 3.14 / string : hello
#
>>> print('integer : {0} / float : {1} / string : {2}'.format(10, 3.14, "hello"))
integer : 10 / float : 3.14 / string : hello
#
>>> print('float : {1} / integer : {0} /string : {2}'.format(10, 3.14, "hello"))
float : 3.14 / integer : 10 /string : hello
```

<br/>

##### enumerate()

- 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력하여 사용
  - 인덱스를 포함한 요솟값을 반환
- for 반복문을 이용해 자료형을 탐색할 때 요솟값만 사용이 가능하기에 enumerate()함수를 사용하면 인덱스 활용이 편함

```python
>>> numbers = [10,11,12,13,14]
>>> for idx, value in enumerate(numbers):
...     print('index:{} / value:{}'.format(idx, value))
...
index:0 / value:10
index:1 / value:11
index:2 / value:12
index:3 / value:13
index:4 / value:14
```

<br/>

##### str()

- 입력으로 들어온 데이터를 문자열 객체로 반환

```python
>>> str(10)
'10'
>>> type(str(10))
<class 'str'>
>>> str("hello".upper())	# 대문자로 변환
'HELLO'
>>> str("HELLO".lower())	# 소문자로 변환
'hello'
>>> str([1,2,3])
'[1, 2, 3]'
```

<br/>

##### join()

- 리스트에 포함되어 있는 요소들을 지정한 구분자로 구분해 연결 된 문자열로 반환
- 구분자를 ' '사이에 명시
  - 명시하지 않고 ''.join(리스트)로 사용하면 모두 붙음
  - 리스트 내 요소들을 문자열로 합칠 때 사용
- 원본이 변경되는 것이 아님

```python
>>> names = ['Kei', 'Tonny', 'Grace', 'Jenny', 'Jaeyoo']
>>> ','.join(names)
'Kei,Tonny,Grace,Jenny,Jaeyoo'
>>> '/'.join(names)
'Kei/Tonny/Grace/Jenny/Jaeyoo'
>>> ''.join(names)
'KeiTonnyGraceJennyJaeyoo'
>>> names
['Kei', 'Tonny', 'Grace', 'Jenny', 'Jaeyoo']
```

<br/>

##### split()

- 리스트에 포함되어 있는 요소들을 지정한 구분자로 분리해 분리 된 문자열로 반환
- 구분자를 괄호 안에 명시
  - 명시하지 않고 리스트.split()로 사용하면 공백 기준으로 분리
  - 리스트 내 요소들을 구분자 기준으로 나눌 때 사용
- 원본이 변경되는 것이 아님

```python
>>> names = ['Kei', 'Tonny', 'Grace', 'Jenny', 'Jaeyoo']
>>> ','.join(names)
'Kei,Tonny,Grace,Jenny,Jaeyoo'
>>> names_str = ','.join(names)
>>> names_split = names_str.split(',')
>>> names_split
['Kei', 'Tonny', 'Grace', 'Jenny', 'Jaeyoo']
#======================================
>>> names = ['Kei', 'Tonny', 'Grace', 'Jenny', 'Jaeyoo']
>>> ' '.join(names)
'Kei Tonny Grace Jenny Jaeyoo'
>>> names_str = ' '.join(names)
>>> names_split = names_str.split()	
	# 구분자 명시 안할 경우 공백 기준으로 구분
>>> names_split
['Kei', 'Tonny', 'Grace', 'Jenny', 'Jaeyoo']
```

<br/>

##### id()

- 객체를 입력받아 객체의 고유 주솟값 (레퍼런스)를 반환
- 해당 객체의 할당 주소 위치 확인 용
- 컴퓨터나 운영체제에 따라 달라질 수 있음

```python
>>> a = 10
>>> id(a)
140716176902080
>>> b = a
>>> id(b)
140716176902080
```

<br/>

##### find()

- 특정 문자열을 찾기 위해 사용
- 찾으려는 문자열의 시작 위치를 반환
  - 없다면 -1을 반환

```python
>>> str = "I want to be a great programmer."
>>> str.find("be")
10
>>> str.find("I")
0
>>> str.find("i")
-1
```

<br/>

##### filter()

- 개별 요소를 반복적으로 셀 수 있는 객체(iterable Object)를 입력 받음
  - 각 요소를 함수로 수행한 후 결과가 True인 것만 묶어서 반환
  - 수행 조건에 True인 값만 돌려주는 필터
- filter 객체 형태로 반환하기 때문에 다른 형태로 사용하려면 생성자를 사용해야 함

```python
>>> def is_even(number):
...		return number % 2 == 0 # 짝수면 True 반환
>>> nubmers = range(1, 21)
>>> print(list(filter(is_even, nubmers)))	# list 형태로 반환 
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

<br/>

##### lambda 키워드

- 함수를 생성할 때 사용하는 키워드
  - def 보다 간결하게 함수를 정의할 수 있다
  - 함수가 복잡하다면 def로 정의하여 사용하는 것이 좋음
- 익명 함수기 때문에 한 번 사용하고 나면 heap 메모리에서 삭제되어 메모리 관리에 효율적

```python
>>> def times(x):
...     return x * 2
...
>>> times(2)
4
>>> times(4)
8
#==========위와 아래는 같은 기능을 하는 함수==========
>>> f = lambda x: x*2
>>> f(2)
4
>>> f(4)
8
```

<br/>

##### filter()함수에 lambda 키워드 사용하기

- 함수를 생성할 때 사용하는 키워드
  - def 보다 간결하게 함수를 정의할 수 있다
  - 함수가 복잡하다면 def로 정의하여 사용하는 것이 좋음
- 익명 함수기 때문에 한 번 사용하고 나면 heap 메모리에서 삭제되어 메모리 관리에 효율적

```python
>>> def is_even(number):
...		return number % 2 == 0 # 짝수면 True 반환
>>> nubmers = range(1, 21)
>>> print(list(filter(is_even, nubmers)))	# list 형태로 반환 
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#==========위와 아래는 같은 기능을 하는 함수==========
>>> numbers = range(1,21)
>>> print(list(filter(lambda n: n%2==0, numbers)))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

<br/>

##### map() 함수와 lambds 사용

- 개별 요소를 반복적으로 셀 수 있는 객체를 입력 받음
  - 각 요소를 함수로 수행 후 결과를 묶어 반환
- 수행 즉시 연산하지 않고 지연 연산(lazy evaluation)을 수행 함
  - 계산이 필요할 때만 메모리를 사용하기 때문에 메모리 절약 효과가 있음

```python
 def square(number):
...     return number ** 2
...
>>> numbers = range(1,5)
>>> print(list(map(square, numbers)))
[1, 4, 9, 16]
#==========위와 아래는 같은 기능을 하는 함수==========
>>> numbers = range(1,5)
>>> print(list(map(lambda x : x**2, numbers)))
[1, 4, 9, 16]
```



<br/>

#### 외장 함수

- 다른 개발자들이 라이브러리 형태로 모듈화 시켜 놓아 임포트(import)하여 사용
- 클래스와 모듈 형태로 묶여 있음
- import 키워드를 사용하여 모듈 불러와 사용

<br/>

##### sys

- 파이썬 인터프리터와 관련된 정보와 기능 제공
- 명령행에서 인수를 전달 받기 위해 많이 사용
  - 프롬프트 상에서 파이썬 실행 시 인자를 추가 할 수 있음
  - 인자 개수는 제한 없음
  - 메모리 허용하는 한 필요한 만큼 사용 할 수 있음
  - 저장한 값은 sys.argv 리스트에 저장하여 사용

<br/>

##### 에디터

```
import sys

print(sys.argv) # 시스템 인자로 들어온 리스트 내용 출력
msg = sys.argv[1] # 'hello'
cnt = int(sys.argv[2]) # 10

for i in range(cnt):    # cnt 범위 만큼 반복
    print(i, msg)
```

<br/>

##### 명령 프롬프트

```shell
[기본 경로]>cd [for_test.py 파일이 있는 폴더 경로]
[폴더 경로]>python for_test.py 'hello' 10    // 엔터키로 실행
['for_test.py', "'hello'", '10']
0 'hello'
1 'hello'
2 'hello'
3 'hello'
4 'hello'
5 'hello'
6 'hello'
7 'hello'
8 'hello'
9 'hello'
```

<br/>

- python 명령 다음부터 시작해 공백 기준으로 나눈 결과가 sys.argv 리스트에 들어감
- 수행 후 종료시킬 땐 에디터 쪽 코드에 sys.exit()을 수행문에 추가



<br/>

##### pickle

- pickle 모듈은 파이썬 객체를 파일로 저장하고 메모리로 읽어 올 수 있도록 도와줌
  - 프로그램을 종료하면 메모리가 초기화 되며 객체가 사라지기 때문
  - 재 실행시에도 유지되어야하는 객체가 있다면  pickle 모듈을 사용하여 저장하고 읽어오면 가능
  - 주로 프로그램 내부에서 사용되는 환경설정이나 결괏값을 유지시키기 위해 사용

- pickle 모듈의 dump() 함수를 이용해 리스트와 딕셔너리 객체를 파일로 저장하는 예제

```python
#==========피클 모듈로 저장하기================
>>> impot pickle
>>> f = open('setting.txt', 'wb')	# Writebinary 모드로 파일 열기
>>> setting = [ {'title', 'python program'}, {'author' : 'kei'}]	
>>> pickle.dump(setting, f)	# 객체 setting의 내용 파일에 저장
>>> f.close()
#=========================================
>>> impot pickle
>>> f = open('setting.txt', 'rb')	# Readbinary 모드로 파일 열기
>>> setting = pickle.load(f)	# 객체 setting에 파일에서 불러온 내용 저장
>>> f.close()
>>> print(setting)
[ {'title', 'python program'}, {'author' : 'kei'}]
```

<br/>

##### time

- time 모듈은 시스템이 제공하는 시관과 관련된 유용한 함수들을 포함
- 시간을 다루는 방식은 지역이나 시스템에 따라 다르기 때문에 결과가 다를 수 있음
- time() 함수를 이용해 현재 시간을 구할 수 있음
  - UTC(Universal Time Coordinated = 협정 세계 표준시) 시간대를 사용해 실수 형태로 반환

```python
>>> import time
>>> time.time()
1613469465.7202463
>>> time.time()
1613469471.247848
```

<br/>

```python
>>> time.localtime(time.time())
time.struct_time(tm_year=2021, tm_mon=2, tm_mday=16, tm_hour=18, tm_min=58, tm_sec=52, tm_wday=1, tm_yday=47, tm_isdst=0)
```

- time 모듈의 localtime() 함수는 반환 된 실수 형태의 초 데이터를 UTC 기준의 struct_time 객체로 변환 해줌
  - 인자가 없는 경우 현재 시간을 기준으로 반환

<br/>

```python
>>> lt = time.localtime(time.time())
>>> time.strftime('%Y/%m/%d %H :%M :%S', lt)
'2021/02/16 19 :00 :56'
```

- time 모듈의 strftime()함수에 인자로 포매팅을하면 원하는 형태로 출력 가능
  - time.strftime('시간 포매팅', time.localtime(time.time()))

<br/>

##### 시간 관련 포매팅 문자

| 포매팅 | 실행               | 예      |
| ------ | ------------------ | ------- |
| %Y     | 연도               | 2020    |
| %m     | 월                 | 01 ~ 12 |
| %d     | 날짜               | 01 ~ 31 |
| %B     | 월                 | January |
| %b     | 월(축약)           | Jan     |
| %A     | 요일               | Monday  |
| %a     | 요일(축약)         | Mon     |
| %H     | 24시간제 출력 형태 | 00 ~ 23 |
| %l     | 12시간제 출력 형태 | 01 ~ 12 |
| %p     | AM 또는 PM         | AM, PM  |
| %M     | 분                 | 00 ~ 59 |
| %S     | 초                 | 00 ~ 59 |

<br/>

##### ramdom

- ramdom 모듈은 난숫값을 생성하는 기능과 다양한 랜덤 관련 함수 제공
- ramdom() 함수를 사용하면 0에서 1사이의 실숫값을 랜덤으로 반환
  - 랜덤이기 때문에 실행때마다 다른 값이 나옴

```python
>>> import random
>>> random.random()
0.7884650238190282
>>> random.random()
0.5644800229772583
```

<br/>

```python
>>> import random
>>> random.uniform(1,2)	 #1이상 2미만
1.8571718237597166
```

<br/>

- uniform() 함수를 사용하면 임의 생성 실수의 범위를 정할 수 있음




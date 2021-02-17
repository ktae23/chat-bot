## 2.2 파이썬 기본

### 2.2.4 클래스

> 객체지향 언어에서는 객체를 생성하기 위해 언어 차원에서 클래스를 지원합니다. 프로그램을 개발 할 때 유사한 기능을 묶어 객체 단위로 해석하면 프로그램 복잡도를 크게 낮출 수 있는 장점이 있습니다.
>
> 파이썬도 객체지향 언어이므로 클래스 문법을 제공하고 있습니다.

<br/>

- 파이썬에서 사용하는 모든 자료형은 객체
  - 객체는 메모리에 적재되어야 사용할 수 있으며 하나의 객체는 어떤 문제를 해결하기 위해 동일한 목적을 갖는 상태와 동작 행위를 가짐
- 객체가 어떤 클래스를 나타내는 경우 인스턴스라고 부름
  - 언어에 따라 객체와 인스턴스를 혼용해서 사용하는 경우도 있으며 넒은 의미에서 객체는 인스턴스를 포함
- 파이썬에서는 모든 데이터를 객체(Object)로 보고 있음
  - 모든 객체는 어떤 기능을 하는 클래스의 인스턴스
  - 즉 파이썬에서 생성하는 모든 객체는 인스턴스

<br/>

```python
class Chatbot :	# 클래스 정의/ 첫 글자는 대문자가 관례
    def sayHello(self):
        print("say Hello")

    def sayMyName(self):
        print("My name is kbot :D")

chatbot = Chatbot()	# Chatbot의 인스턴스 생성
chatbot.sayHello()	# chatbot을 참조하여 메서드 호출
chatbot.sayMyName()	# chatbot을 참조하여 메서드 호출
```

- 클래스 명 첫 글자는 대문자 사용이 관례
- 클래스의 메서드를 정의 할 때는 첫 번째 인자로 반드시 self 키워드를 사용
  - [self를 사용하는 이유](https://wikidocs.net/1742)

#### 생성자 및 소멸자

> 파이썬에서는 인스턴스가 생성될 때 자동으로 호출하는 생성자(Constructor)라는 메서드를 제공합니다.
>
> 생성자 메서드명은 사용자가 임의로 변경 할 수 없으며, 생성자 메서드로 `__init__`을 사용합니다.
>
> 생성자는 인스턴스가 생성되는 시점에 실행되기 때문에 해당 객체를 동작시키기 위한 사전 작업을 하게 됩니다.

<br/>

```python
class 클래스명 :
    def __init__(self, 인자, ...):
        ...
```

<br/>

> 파이썬은 인스턴스가 소멸될 때 자동으로 호출되는 소멸자(Destructor)라는 메서드도 제공합니다.
>
> 소멸자 메서드명은 임의로 변경 할 수 없으며, 소멸자 메서드로 `__del__`을 사용합니다.
>
> 인자를 사용 할 수 없으며 인스턴스 객체가 소멸되는 시점에 호출되기 때문에 주로 객체가 사용하고 남은 메모리를 청소하는 작업을 합니다.

<br/>

```python
class 클래스명 :
    def __del__(self):
        ...
```

<br/>

```python
class SimpleObj:
    def __init__(self):
        print('call__init__()')
        
    def __del__(self):
        print('call__del__()')
        
obj = SimpleObj()
print('obj instacne is alive...')
del obj
```

<br/>

#### 메서드와 인스턴스 변수

> 클래스는 메서드와 인스턴스 변수로 구성되어 있습니다. 메서드를 통해 객체의 행동을 정의하고 인스턴스 변수를 이용해 객체의 상태를 표현할 수 있습니다.
>
> 앞서 배운 함수와 변수의 개념과 동일하기 때문에 클래스 내부에서 사용되는 함수는 메서드, 클래스 안에서 전역적으로 사용되는 변수는 인스턴스 변수라고 생각해도 큰 무리가 없습니다.

<br/>

- 인스턴스 변수는 한 번 선언되면 클래스의 모든 메서드에서 사용 가능
- self 키워드를 붙여 선언
  - self.변수명 = 초깃값

<br/>

```python
class Calc:
    def __init__(self,init_value):
        self.value = init_value	# 인자로 받은 값으로 전역 변수 선언 및 초기화

    def add(self, n):
        return self.value + n

    def sub(self, n):
        return self.value - n

    def mul(self, n):
        return self.value * n

    def div(self, n):
        return self.value / n


cal = Calc(100)
print("value = {0}".format(cal.value))

a = cal.add(100)
b = cal.sub(50)
c = cal.mul(2)
d = cal.div(2)

print("a={0}, b={1}, c={2}, d={3}".format(a,b,c,d))
```

**value = 100**

**a=200, b=50, c=200, d=50.0**

<br/>



### 2.2.5 모듈

> 모듈이란 여러 가지 함수나 클래스 등을 기능이나 목적별로 모아놓은 파일입니다. 만들어진 모듈은 다양한 프로그램에서 라이브러리 형태로 사용할 수 있으며, 앞서 예제를 실습하면서 이미 사용해 보았습니다.
>
> 모듈화된 기능은 재사용하기 쉽기 때문에 중복 코드 문제도 자연스럽게 해결 됩니다. 파이썬은 다른 언어에 비해 좋은 모듈이 많이 공개되어 있으므로 인기가 많습니다.

- 모듈을 만들때는 같은 목적을 가진 함수나 클래스들을 묶어서 모듈명을 결정해야 함

<br/>

##### calc 모듈

```python
# calc.py 모듈

# 덧셈 함수
def add(a,b): return a + b

# 뺄셈 함수
def sub(a,b): return a - b

# 곱셈 함수
def mul(a,b): return a * b

# 나눗셈 함수
def div(a,b): return a / b
```

<br/>

##### 모듈 사용

```python
import calc	# 사용하고자 하는 모듈 임포트

a = calc.add(10,20)	# 모듈명 참조하여 바로 함수 호출
print("add = {}".format(a))
b = calc.mul(10,2)
print("mul = {}".format(b))
```

<br/>

- 자바는 정적 메서드가 아니고서야 해당 메서드가 포함 된 클래스를 생성 한 뒤에야 인스턴스를 참조하여 메서드를 호출 할 수 있었다
  - 파이썬은 클래스 생성이 아닌 함수만을 모아 둔 파이썬 파일(.py)만 있으면 파일(모듈) 자체를 참조해서 호출할 수 있다. 

<br/>

##### 모듈 임포트 없이 함수만 불러와서 사용 할 경우

```python
from 모듈명 import 함수명, 함수명, ...	# 일부 원하는 함수만 가져올 경우
from 모듈명 import *	# 모듈 내 모든 함수를 가져오거나 어떤 함수만 사용 할 지 모를 경우
```

<br/>

### 2.2.6 예외 처리

> 파이썬에서는 에러가 발생하는 예외 상황을 처리할 수 있는 방법을 제공하고 있습니다. 현업에서는 경험 많은 개발자일 수록 프로그램 코드의 예외 처리 능력이 뛰어납니다.
>
> 파이썬에서는 이런 예외 처리를 할 수 있도록 try-except구문을 문법적으로 제공하고 있습니다.

```python
try:
    ...
except 오류 사항 as 오류 메시지 변수:
    ...
finally
	...
```

<br/>

- try 구문 안에 오륲 발생 가능성이 있는 코드를 사용
  - 예외가 발생하면 그 즉시 except 구문으로 코드 흐름이 점프
- except 구문에는 예외가 발생 했을 때 예외 처리를 할 수 있는 코드가 들어 있음
- finally 구문은 try 구문 수행 도중 예외 발생 여부와 상관 없이 항상 실행 됨
  - 때문에 리소스 해제를 위해 많이 사용 함
  - 리소스 해제가 필요 없는 경우 생략하기도 함

<br/>

##### 문자로 나누는 에러 출력

```python
try:
    a = 10
    b = 'zero'
    c = a/b
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
```

**unsupported operand type(s) for /: 'int' and 'str'**

<br/>

##### 0으로 나누는 에러 출력

```python
try:
    a = 10
    b = 0
    c = a/b
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
```

**division by zero**

<br/>

##### 리소스 사용 후 에러 발생시에 안전하게 리소스 닫는 구문

```python
import pickle

f = open('setting.txt', 'wb')
try:
    setting = [ {'title' : 'pyton program'}, {'author' : 'kei'}]
    pickle.dump(setting, f)
except Exception as e:
    print(e)
finally:
    f.close()
```

<br/>

### 2.2.7 엑셀 파일을 읽고 쓰는 방법

> 챗봇을 똑똑하게 만들려면 데이터 학습이 필요합니다. 
>
> 챗봇 엔진은 입력되는 질문에 맞는 답변을 채택하기 위해 사전에 학습 데이터가 데이터베이스에 저장되어 있어야 합니다. 
>
> 챗봇의 학습 데이터를 데이터베이스에 저장하기 위해 학습 프로그램을 만드는 것도 좋지만 우리는 간편하게 정해진 엑셀 양식에 질문과 답변을 정리해서 데이터베이스에 저장할 것입니다.
>
> 또한 이미 학습 된 데이터를 덤프 뜨거나 어떤 작업의 보고서를 만들 때 엑셀 형태로 저장하면 데이터를 해석할 때 엑셀 기능을 다양하게 활용 할 수 있습니다.

<br/>

##### OpenPyXL Module

- 엑셀 2010(xlsx, xlsm, xltx, xltm)을 읽고 쓸 수 있음
  - 파이썬 기본 모듈이 아니므로 라이브러리 설치 필요
- 엑셀 문서 구조 파악 필요
  - 이미지 출처 : 처음 배우는 딥러닝 챗봇

![image-20210217084139804](C:\Users\zz238\AppData\Roaming\Typora\typora-user-images\image-20210217084139804.png)

- 워크북 : 하나 이상의 워크시트를 가지고 있으며, 파일 명이 워크북(엑셀 문서)의 이름이 됨
- 워크시트 : 데이터를 입력 할 수 있는 셀(cell)이 열(column)과 행(row) 형태로 구성되어 있는 엑셀 시트
  - 현재 활성화 되어 있는 워크시트인 경우 액티브(active) 시트라고 함

<br/>

### OpenPyXL로 엑셀 파일 읽기

- 예제로 제공 된 엑셀 파일 내용
  - 이미지 출처 : 처음 배우는 딥러닝 챗봇

![image-20210217084452285](C:\Users\zz238\AppData\Roaming\Typora\typora-user-images\image-20210217084452285.png)

<br/>

##### 시트 일부 정보 읽어 오기

```python
import openpyxl

wb = openpyxl.load_workbook('./sample.xlsx')	# ./는 현재 폴더 경로
sheet = wb['Sheet1']
print(sheet.max_column, sheet.max_row)	# 워크시트의 컬럼 수, 로우 수를 출력
print(sheet.cell(row=1, column=1).value)	# 1행 1열 값 출력
print(sheet.cell(row=2, column=1).value)	# 2행 1열 값 출력
wb.close()
```

**3 6**

**이름**

**Kei**

<br/>

- 파이썬에서 \a, \b등은 ASCII Bell character 으로 인식하기 때문에 \으로 경로를 쓰면 해당경로를 찾을 수 없다는 오류가 나옴
  - 경로는 /로 사용해야 함
  - [정보 출처](https://seong6496.tistory.com/66)

<br/>

##### 시트 전체 정보 읽어 오기

```python
 
```

**Kei**

**35** 

**1234-1234**

**==========**

**Hong**

**26**

**4320-1420**

**==========**

**이하 생략**

<br/>

- iter_rows() 함수를 이용해 워크 시터 내의 모든 row데이터를 순회하며 조회
  - min_row 인자는 초기 탐색 위치를 설정
  - 예제에서는 2행부터 탐색 시작
  - 텍스트 헤더로 사용되는 첫 번째 행은 탐색하지 않음
  - min_row 인자 생략 시 첫 번째 행부터 탐색

- 열 단위 데이터 출력 위해 이중 for문 사용

<br/>

##### 슬라이싱을 이용한 특정 범위 읽기

```python
import openpyxl

wb = openpyxl.load_workbook('./sample.xlsx')
sheet = wb['Sheet1']

cells = sheet['A2':'C3']	# 슬라이싱을 통한 범위지정
for row in cells:
    for cell in row:
        print(cell.value)
    print('=' * 10)
wb.close()
```

**Kei**

**35** 

**1234-1234**

**==========**

**Hong**

**26**

**4320-1420**

**==========**

<br/>

### OpenPyXL로 엑셀 파일 쓰기

> 데이터를 OpenPyXL 모듈을 사용해 엑셀 파일로 저장해봅시다. 엑셀 파일을 생성하기 위해서는 워크북과 워크시트를 순차적으로 생성하고, 원하는 셀에 데이터를 기록하면 됩니다. 마지막으로 워크북을 저장하고 닫으면 우리가 기록한 데이터를 갖는 엑셀 파일이 생성됩니다.

<br/>

```python
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '회원정보'

# 표 헤더 컬럼 저장
header_titles = ['이름', '전화번호']	# 리스트형식으로 작성하여 for문으로 헤더 순차 저장 진행
for idx, title in enumerate(header_titles):
    sheet.cell(row=1, column=idx+1, value=title)
# 표 내용 저장
members = [('kei', '010-1234-1234'), ('hong', '010-4321-1234')]
row_num = 2	# row 1은 타이틀 위치
for r, member in enumerate(members):	# 회원 정보 목록 탐색
    for c, v in enumerate(member):	# 이름, 전화번호 컬럼 탐색
        sheet.cell(row=row_num+r, column=c+1, value=v)

wb.save('./member.xlsx')
wb.close()
```

<br/>

- 워크북 인스턴스 객체 생성 후 활성화 된 객체 가져옴
  - 기본적으로 생성 된 워크시트 제목은 'Sheet'
  - '회원정보'로 워크시트 제목 변경

- cell()함수는 셀 데이터의 출력과 저장 모두 가능
  - value 인자에 저장하고싶은 데이터를 입력하면 해당 셀에 데이터가 저장 됨
  - cell() 함수에서 셀의 위치를 사용 할 때는 반드시 1부터 시작해야 함

<br/>

##### 저장 결과

![image-20210217095924907](C:\Users\zz238\AppData\Roaming\Typora\typora-user-images\image-20210217095924907.png)
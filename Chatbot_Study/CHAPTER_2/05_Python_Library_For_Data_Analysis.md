## 2.3 데이터 분석을 위한 필수 라이브러리

> 챗봇 엔진 개발에 필요한 딥러닝 모델을 설계할 때 데이터 분석은 매우 중요합니다. 
>
> 모델 개발에 필요한 데이터를 분석하려면 다양한 수치 계산과 과학적인 접근법이 필요합니다.
>
> 챗봇 엔진 개발에 있어 가장 기본이 되는 내용이기 때문에 반드시 익숙해져야 합니다.

<br/>

### 2.3.1 넘파이

> 넘파이(NumPy) 라이브러리는 C언어로 구현되어 있기 때문에 빠른 배열 처리와 고성능 수치 계산을 지원합니다. 
>
> 주로 벡터 및 행렬 연산에 필요한 기능을 제공합니다.
>
> 데이터 분석에 필요한 다양한 기능을 포함하고 있으며, 파이썬의 기본 자료구조보다 효율적인 방법으로 데이터를 다룰 수 있어 
>
> 팬더스(Pandas)나 맷플롯립(matplotlib.pyplot) 라이브러리에서도 사용하고 있습니다.
>
> 수학적 개념을 넘파이로 표현만 가능하다면 텐서플로 같은 딥러닝 프레임워크 없이도 딥러닝 모델을 구현할 수 있을 정도로 강력합니다. 



- 확실히 넘파이를 임포트하면 아주 강력한 계산기 하나 옆구리에 끼는 듯이 든든하다

  

- 딥러닝에 대해 자세히 알고자 하는 독자에게는 한빛미디어에서 출간한 [밑바닥부터 시작하는 딥러닝](https://www.hanbit.co.kr/store/books/look.php?p_code=B8475831198)책을 추천
  
  - 넘파이만을 이용해 딥러닝의 기본 원리를 파악할 수 있게 구성 되어 있음
- 수치 계산을 할 때는 배열이나 행렬을 많이 사용 함
  
  - 가장 기본이 되는 것은 배열, 행렬 개념으로 사용 됨

<br/>

##### 넘파이 라이브러리의 array()함수를 이용해 배열 생성

```python
import numpy as np

arr = np.array([1,2,3])
print(arr)
print(type(arr))
```

**[1 2 3]**

**<class 'numpy.ndarray'>**

<br/>

##### 행렬 생성

```python
import numpy as np

matrix = np.array([1,2,3], [4,5,6])
print(matrix)
```

**[[1 2 3]**

 **[4,5,6]]**

<br/>

##### 행렬의 덧셈과 곱셈, 스칼라 곱

- 서로 같은 크기의 행렬일 때만 덧셈 가능
- m * k 행렬A와 k * n 행렬 B처럼 한쪽의 행과 다른 한쪽의 열이 같을 때만 곱셈 가능
  - np.matmul(A, B)
  - 결과는 m * n 행렬

```python
import numpy as np

# 행렬 덧셈
A = np.array([1,2], [3,4])
B = np.array([1,1], [1,1])
C = A + B
print(C)
#[[2 3]
# [4,5]]

# 행렬 곱셈
A = np.array([a1.1, a1.2], [a2.1, a2.2], [a3.1, a3.2])
B = np.array([b1.1, b1.2], [b2.1, b2.2])
C = np.matmul(A, B)
print(C)
# [(a1.1 * b1.1 + a1.2 * b2.1), (a1.1 * b1.2 + a1.2 * b2.2)]
# [(a2.1 * b1.1 + a2.2 * b2.1), (a2.1 * b1.2 + a2.2 * b2.2)]
# [(a3.1 * b1.1 + a3.2 * b2.1), (a3.1 * b1.2 + a3.2 * b2.2)]

# 행렬 스칼라 곱
A = np.array([1,2], [3,4])
k = 10
C = k * A
print (C)
#[[10,20]
# [30,40]]
```

<br/>

### 2.3.2 팬더스

> 데이터 분석 및 처리를 위한 필수 라이브러리
>
> 행과 열로 구성 된 데이터 객체 관리 수월, 대용량 데이터 처리 용이
>
> 가공된 데이터 저장 또는 저장된 파일 불러 데이터 객체로 만드는 기능 제공

- 시리즈 (Series), 데이터프레임 (DataFrame), 패널 (Panel) 세 가지 데이터 구조를 가짐

<br/>

#### 시리즈 (Series)

- 1차원 데이터로 각 데이터 값과 대응하는 인덱스 지정 가능
- 인덱스 생략 시 자동 할당

<br/>

##### 인덱스 생략한 시리즈 객체

```python
import pandas as pd

numbers = pd.Series( [100, 200, 300])
print(numbers)
```

![image-20210223215216758](C:\Users\zz238\AppData\Roaming\Typora\typora-user-images\image-20210223215216758.png)



<br/>

##### 인덱스 지정한 시리즈 객체

```python
import pandas as pd

scores = pd.Series( [90, 80, 99], index=['국어', '수학', '영어'])
print(scores)
```

![image-20210223215342225](C:\Users\zz238\AppData\Roaming\Typora\typora-user-images\image-20210223215342225.png)



<br/>

##### 시리즈 객체의 인덱스, 데이터 값 출력

```python
import pandas as pd

scores = pd.Series( [90, 80, 99], index=['국어', '수학', '영어'])

print("scores.index")
print(scores.index)
print("scores.values")
print(scores.values)

# 원하는 위치의 인덱스, 데이터값 출력
print("scores.index[1],scores.values[1]")
print(scores.index[1],scores.values[1])
```



![image-20210223215557033](C:\Users\zz238\AppData\Roaming\Typora\typora-user-images\image-20210223215557033.png)



<br/>

#### 데이터프레임 (DataFrame)

- 2차원 데이터, 행 방향(row)인덱스와 열 방향(Column) 인덱스로 구성
  - 레이블이나 카테고리가 있는 데이터 보관 용도로 적합
- 엑셀, CSV, 텍스트, JSON 등 다양한 데이터 파일을 읽어 데이터프레임 생성 가능

```python
import pandas as pd

# 계절별 서울/부산 지역 온도 데이터 정의
temperatures = [[3.3, 34.5, 14.2, -10], [7.1, 32.1, 10.7, 2]]
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
regions = ['Seoul', 'Pusan']

# 데이터프레임 객체 생성
		# .DataFrame(행렬 입력, 행 인덱스 입력, 열 인덱스 입력)
data = pd.DataFrame(temperatures, index=regions, columns=seasons)	

# 서울의 봄 온도 데이터 출력
print(data['Spring']['Seoul'])	# 서울 행 / 봄 열 값

# 앞부분에서 2번째 행까지 조회
print(data.head(2))

# 뒷부분에서 1번째 행까지 조회
print(data.tail(1))
```

![image-20210223220344435](C:\Users\zz238\AppData\Roaming\Typora\typora-user-images\image-20210223220344435.png)



<br/>

### 2.3.3 맷플롯립

> 데이터를 플롯(plot)이나 차트로 시각화 할 수 있도록 도와주는 도구입니다.
>
> 라인플롯, 바차트, 파이차트, 히스토그램 등 다양한 차트와 플롯 스타일을 지원합니다.

<br />

##### 1차 함수 그래프

```python
import matplotlib.pyplot as plt

# x, y축 데이터 정의
x = [a for a in range(0, 11)] # 리스트 내부 a 표현식에 for a in range(0,11)를 돌려 a값을을 리스트에 추가
y = list(range(0, 11))

# 그래프 출력
plt.plot(x, y)	#x,y축의 값이 각 0~10인 직선 그래프 생성
plt.show()	# 그래프 화면 출력
```

![image-20210223222800815](C:\Users\zz238\AppData\Roaming\Typora\typora-user-images\image-20210223222800815.png)

<br/>

##### 2차 함수 그래프

```python
import matplotlib.pyplot as plt

# 2차 함수 정의
# f(x) = x^2
f = lambda x: x ** 2

# x, y축 데이터 정의
x = [x for x in range(-10, 10)]
y = [f(y) for y in range(-10, 10)]


# 그래프 출력
plt.plot(x, y)
plt.show()
```

![image-20210223222928288](C:\Users\zz238\AppData\Roaming\Typora\typora-user-images\image-20210223222928288.png)

<br/>

##### 막대 그래프

```python
import matplotlib.pyplot as plt

# 데이터 정의
temperatures = [3.3, 34.5, 14.2, -10]
x = list(range(4))
x_labels = ['Spring', 'Summer', 'Fall', 'Winter']

# 바차트 출력
plt.title("Bar Chart")
plt.bar(x, temperatures)
plt.xticks(x, x_labels)
plt.yticks(sorted(temperatures))
plt.xlabel("season")
plt.ylabel("temperature")
plt.show()
```

![image-20210223223030727](C:\Users\zz238\AppData\Roaming\Typora\typora-user-images\image-20210223223030727.png)
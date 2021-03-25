## 임베딩

<br/>

> 컴퓨터는 수치 연산만 가능하기 때문에 자연어를 숫자나 벡터 형태로 변환할 필요가 있고 이런 일련 과정을 자연어 처리 분야에서는 임베딩(embedding)이라 한다.

<br/>

- 단어나 문장을 수치화해 벡터 공간으로 표현하는 과정을 의미
  - 다른 딥러닝 모델의 입력값으로 많이 사용 됨
- 말 뭉치의 의미에 따라 벡터화 되므로 문법적인 정보가 포함 되어 있음
  - 임베딩 품질이 좋으면 단순한 모델로도 좋은 결과 얻을 수 있음

<br/>

#### 임베딩 종류

- 문장 임베딩 : 문장 전체를 벡터로 표현
  - 장점
    - 전체 문장의 흐름을 파악해 벡터로 변환하므로 문맥적 의미를 지님
    - 단어 임베딩에 비해 품질이 좋고 상용 시스템에 많이 사용 됨
  - 단점
    - 임베딩하기 위해 많은 문장 데이터가 필요하여 학습 비용 큼

- 단어 임베딩 : 개별 단어를 벡터로 표현

  - 장점 
    - 문장 임베딩에 비해 학습 방법이 간단해 실무에서 많이 사용 함
  - 단점
    - 동음이의어에 대한 구분이 없어 의미가 달라도 동일한 벡터 값으로 표현 됨

- 본 교재에서는 단어 임베딩만 진행

  <br/>

### 단어 임베딩

- 말뭉치에서 각각의 단어를 벡터로 변환하는 기법을 의미
- 의미와 문법적 정보를 지니며, 단어를 표현하는 방법에 따라 다양한 모델이 존재
- 토크나이징은 형태소 기반이기 때문에 컴퓨터에서 처리하기엔 단어 임베딩 기법이 효과적

<br/>

#### One - Hot Encoding

- 단어를 숫자 벡터로 변환하는 가장 기본적인 방법
- **One - Hot Vector**
  - 원-핫 인코딩으로 나온 결과
- 요소들 중 단 하나의 값만 1이고 나머지 요소 값은 0인 인코딩을 의미
  - 희소 벡터(Sparse Vector)라고 부름

<br/>

- 말뭉치에서 나오는 서로 다른 모든 단어의 집합을 만들어야 원-핫 인코딩 진행 가능
  - 말뭉치에 존재하는 모든 단어의 수가 원-핫 벡터의 차원을 결정함
    - 100개 단어가 조냊하면 원-핫 벡터의 크기는 100차원
    - 단어에 해당하는 원-핫 벡터값을 받으면 인덱스 값에 일치하는 단어로 인식

<br/>

```python
from konlpy.tag import Komoran
import numpy as np

komoran = Komoran(userdic='./custom.tsv')
text =  "파이썬 임베딩 공부하고 있어요"

# 명사만 추출
nous = komoran.nouns(text)
print(nous)

# 단어 사전 구축 및 단어별 인덱스 부여
# 동일한 단어에 서로 다른 원-핫 벡터 값이 들어가면 안되기 때문에 딕셔너리 사용
dics = {}
for word in nous:
    if word not in dics.keys():
        dics[word] = len(dics)
print(dics)

# 원-핫 인코딩 - 인덱스 부여
# 원-핫 벡터 차원 크기 결정
nb_classes = len(dics)	

# 넘파이의 원-핫 인코딩 기능 사용을 위해 리스트 형태로 변환 필요
# 단어별 인덱스 값을 가져오기 위해 value만 리스트로 변환
targets = list(dics.values())

# 넘파이 eye()함수를 이용해 원-핫 벡터 생성
# eye() 함수는 인자의 크기대로 단위행렬을 반환
# eye() 함수 뒤에 붙은 [targets]를 이용해 생성된 단위 행렬의 순서를 단어 사전의 순서에 맞게 정렬 해줌
one_hot_targets = np.eye(nb_classes)[targets]
print(one_hot_targets)

['파이썬', '임베딩', '공부']
{'파이썬': 0, '임베딩': 1, '공부': 2}
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

- 임베딩을 '임베'로 가져오길래 사용자 사전에 NNG(일반 명사)로 추가 함
- 간단한 구현 방법에 비해 성능이 좋아 많이 사용되지만 단순히 단어의 순서에 의한 인덱스 값을 기반으로 인코딩 된 값
  - 유사한 단어와의 관게나 단어 의미가 담겨 있지 않음
- 단어 사전의 크기가 커지는 만큼 원-핫 벡터의 차원도 커지기 때문에 메모리 낭비와 계산의 복잡도가 커짐

<br/>

#### 희소 표현과 분산 표현

import pandas as pd

scores = pd.Series( [90, 80, 99], index=['국어', '수학', '영어'])

print("scores.index")
print(scores.index)
print("scores.values")
print(scores.values)

# 원하는 위치의 인덱스, 데이터값 출력
print("scores.index[1],scores.values[1]")
print(scores.index[1],scores.values[1])
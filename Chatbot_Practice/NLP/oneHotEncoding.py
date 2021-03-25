from konlpy.tag import Komoran
import numpy as np

komoran = Komoran(userdic='./custom.tsv')
text =  "파이썬 임베딩 공부하고 있어요"

# 명사만 추출
nous = komoran.nouns(text)
print(nous)

# 단어 사전 구축 및 단어별 인덱스 부여
dics = {}
for word in nous:
    if word not in dics.keys():
        dics[word] = len(dics)
print(dics)

# 원-핫 인코딩
nb_classes = len(dics)
targets = list(dics.values())
print(targets)
one_hot_targets = np.eye(nb_classes)[targets]
print(one_hot_targets)

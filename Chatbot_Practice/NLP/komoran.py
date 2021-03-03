from konlpy.tag import Komoran

# 코모란 형태소 분석기 객체 생성
from NLP.kkma import morphs

komoran = Komoran()

text = "아버지가 방에 들어가십니다."

# 형태소 추출
morphs = komoran.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출
pos = komoran.pos(text)
print(text)

# 명사만 추출
nouns = komoran.nouns(text)
print(nouns)
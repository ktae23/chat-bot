from konlpy.tag import Kkma

# 꼬꼬마 형태소 분석기 객체 생성
kkma = Kkma()

text = "파이썬 라이브러리 꼬꼬마 형태소 분석기 사용"

# 형태소 추출
morphs = kkma.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출
pos = kkma.pos(text)
print(pos)

# 명사만 추출
nouns = kkma.nouns(text)
print(nouns)

# 문장 분리
sentences = "파이썬을 배워봐요. 흥미로운 언어에요."
s = kkma.sentences(sentences)
print(s)
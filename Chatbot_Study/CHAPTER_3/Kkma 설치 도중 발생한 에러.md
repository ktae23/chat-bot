## Kkma 형태소 분석기 예제

```python
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
```

<br/>

## Kkma 설치 도중 발생한 에러

```shell
C:\Users\zz238\.conda\envs\chatbot\python.exe C:/Users/zz238/ChatBot/Chatbot_Practice/example/Kkma.py
Traceback (most recent call last):
  File "C:/Users/zz238/ChatBot/Chatbot_Practice/example/Kkma.py", line 4, in <module>
    kkma = Kkma()
  File "C:\Users\zz238\.conda\envs\chatbot\lib\site-packages\konlpy\tag\_kkma.py", line 95, in __init__
    jvm.init_jvm(jvmpath, max_heap_size)
  File "C:\Users\zz238\.conda\envs\chatbot\lib\site-packages\konlpy\jvm.py", line 67, in init_jvm
    convertStrings=True)
  File "C:\Users\zz238\.conda\envs\chatbot\lib\site-packages\jpype\_core.py", line 222, in startJVM
    ignoreUnrecognized, convertStrings, interrupt)
SystemError: java.nio.file.InvalidPathException: Illegal char <*> at index 65: C:\Users\zz238\.conda\envs\chatbot\lib\site-packages\konlpy\java\*

Process finished with exit code 1

```

- 검색 결과 자바 패스 설정이 안된 것 같아 여러 차례 패스 설정 시도 했으나 정상적임에도 작동이 안됨
- 자바 경로, Jpype 설치, pip 업그레이드, Konlpy 재설치 모두 했으나 작동 안됨
- 명령프롬프트에서 python을 실행하여 진행시 Kkma 형태소 분석기 정상 사용 됨
- 파이썬 재설치, 파이참 재설치해도 안됨

<br/>

## 해결

- 문제는 python과 Jpype의 버전 불일치였다.
  - 커맨드에서 python 버전 확인시 3.8.5였다.

![파이썬 버전](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/CHAPTER_3/img/python_version.png)

<br/>

-  그래서 Jpype도 `JPype1-1.2.0-cp38-cp38-win_amd64`를 설치 했었는데 계속 안됐었다.

![Jpype 버전](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/CHAPTER_3/img/Jpype.png)

<br/>

- 수 많은 방법 후에 아무리 생각해봐도 환경 변수에는 문제도 없고 명령 프롬프트에선 잘 되니까 파이참에서 모종의 버전 차이가 있는 것 같았다.
  - 그래서 파이참 터미널에서 가상환경( = 콘다 커맨드)에서 파이썬 버전을 확인해보니 아.. 다르다. 3.7.9다.

![콘다환경 버전](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/CHAPTER_3/img/VE.png)

<br/>

- 그래서 콘다 가상환경 버전에 맞게 Jpype를 재설치 한 뒤 실행해보니 konlpy와 Kkma가 잘 임포트 되어 실행 되었다. 

<br/>

#### 실행 결과

```python
C:\Users\zz238\.conda\envs\chatbot\python.exe C:/Users/zz238/ChatBot/Chatbot_Practice/NLP/kkma.py
['파이', '썰', 'ㄴ', '라이브러리', '꼬꼬마', '형태소', '분석기', '사용']
[('파이', 'NNG'), ('썰', 'VV'), ('ㄴ', 'ETD'), ('라이브러리', 'NNG'), ('꼬꼬마', 'NNG'), ('형태소', 'NNG'), ('분석기', 'NNG'), ('사용', 'NNG')]
['파이', '라이브러리', '꼬꼬마', '형태소', '분석기', '사용']
['파이 썬 을 배워 봐요.', '흥미로운 언어에요.']

Process finished with exit code 0
```

<br/>

- [Konlpy 공식 페이지](https://konlpy-ko.readthedocs.io/ko/v0.4.3/install/#id2)
- [설치 에러 해결 도움 블로그](https://ellun.tistory.com/46)
- [설치 에러 해결 도움 블로그2](https://needjarvis.tistory.com/642)

- [Jpype 설치 페이지](https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype)

  - python 3.7버전일 경우 중간 숫자가 37인것, 뒤의 32, 64는 윈도우 비트

  
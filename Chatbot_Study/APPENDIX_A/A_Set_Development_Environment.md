#  개발 환경 구축

## 1. 파이썬 설치하기

[파이썬 공식 홈페이지](https://www.python.org/)에 접속하여 설치 진행

![파이썬 홈페이지](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/python_download.png){: width="500" height="500"}

![파이썬 다운로드](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/python_download2.png){: width="500" height="500"}



- 설치 완료 후 python 실행 확인

```shell
python
```

<br/>



![파이썬 실행 확인](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/python_prompt.png){: width="500" height="500"}



## 2. 아나콘다 설치하기

> - 아나콘다는 데이터 분석 및 과학 분야에 필요한 패키지들을 기본적으로 포함하고 있는 파이썬 배포판입니다.
> - 머신러닝에 필요한 패키지들이 기본적으로 포함되어 있기 때문에 패키지 설치에 따른 스트레스를 줄일 수 있습니다.
> - 뿐만 아니라 파이썬 개발에 필요한 가상 환경을 관리할 수 있어 편리한 점이 많습니다.

[아나콘다 홈페이지](https://www.anaconda.com/products/individual)에 접속하여 설치 진행

![아나콘다 홈페이지](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/anaconda_download.png){: width="500" height="500"}

![아나콘다 다운로드](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/anaconda_download2.png){: width="500" height="500"}



- 설치 완료 conda 실행 확인

```shell
conda list
```

![아나콘다 실행 확인](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/anaconda_prompt.png){: width="500" height="500"}



<br/>

## 3. CLI 환경에서 콘다로 가상 환경 만들기

> - 파이썬 프로젝트를 진행하다 보면 경우에 따라 같은 패키지라도 버전을 다르게 사용하는 경우가 자주 생깁니다.
>
> - 사용하는 패키지에 따라 의존성에 맞는 버전을 사용하기 때문에 운영 시스템에 바로 설치하게 되면 다른 프로젝트에서는 실행이 안 되는 문제가 생길 수도 있습니다. 따라서 가상환경(Cirtual Environment)를 사용하여 해당 문제를 해결합니다.
>   - 가상 환경을 사용할 경우 프로젝트마다 독립된 환경을 가지기 때문에 다른 프로젝트의 환경 설정이나 패키지 버전 충돌과 같은 문제를 막을 수 있습니다.

<br/>

- 가상 환경 생성 예시

```shell
conda create -n <가상 환경명> python=<파이썬 버전>
```

```shell
conda create -n chatbot pypthon=3.7
```

<br/>

- 가상환경 활성화 예시
  - 생성된 가상 환경을 사용하기 위해서는 가상 환경 활성화 필요

```shell
conda activate <가상 환경명>
```

```shell
conda activate chatbot
```

<br/>

Anaconda prompt에서 진행하는 과정에서 아래와 같은 오류가 발생했다.

```shell
(base) [디렉토리 패스] >conda create chatbot python=3.7 anaconda

CondaValueError: The target prefix is the base prefix. Aborting.
```

- 정말 단순하게 `conda create`와 `chatbot(가상 환경 명)` 사이에 `-n`을 안적어서 생긴 문제였다. 

  - 가상 환경 생성 명령어를 입력하면 y/n 을 묻고, y를 누르면 후다닥 뭐가 만들어 진다.

    <br/>

- 이를 해결하는 과정에서 매우 친절한 설명을 찾아 공유한다.

> -> [콘다 가상환경 설정](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)
>
> -> [콘다 명령어 모음](https://blog.naver.com/msamhh/221831029086)

> 실행 결과

```sh
[디렉토리 패스] >conda activate chatbot

(chatbot) [디렉토리 패스] >
```

<br/>

- 가상환경 정보 조회

```shell
conda info --envs

# conda environments:
#
base                     C:\ProgramData\Anaconda3
chatbot               *  C:\Users\zz238\.conda\envs\chatbot
```

<br/>

- 가상환경에서 파이썬 실행
  - 간단한 프로젝트인 경우 운영 시스템에 직접 설치한 파이썬 인터프리터 사용해도 상관 없음
  - 하지만 패키지 의존도가 복잡한 프로젝트인 겨우 가상 환경을 생성해서 개발하는 편이 좋음

```shell
python
```

- 명령어 입력 시 가상 환경 내에서 파이썬이 실행 됨

```shell
(chatbot) C:\Users\zz238>python
Python 3.7.9 (default, Aug 31 2020, 17:10:11) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

<br/>

- 파이썬 실행 종료 및 가상환경 비활성화

```shell
>>> exit()
//파이썬 종료 됨.
(chatbot) [디렉토리 패스] >conda deactivate

conda deactivate
// 콘다 가상환경 비활성화 명령
```

- 비활성화 실행 결과

```shell
(chatbot) [디렉토리 패스] >conda deactivate

[디렉토리 패스]  >
```

<br/>

## 4. 기타 패키지 설치하기

- 앞서 생성한 가상환경에서 패키지를 설치해야 함.

<br/>

### ㅁ 4.1 Tensorflow 설치

- 딥러닝 모델 실습을 위해 텐서플로우 프레임워크가 필요
- 이 책에서는 2.1 버전 사용

- 텐서플로 설치 명령어

```shell
(chatbot) [디렉토리 패스] > pip install tensorflow==2.1
```

<br/>

### ㅁ 4.2 Java SE Runtime Environment 설치

- 코모란(Komoran) 형태소 분석기 사용을 위해 JRE 8 또는 상위 버전이 필요
- 이 책에서는 8 버전 사용
- [설치 주소](oracle.com/java/technologies/javase-jre8-downloads.html)

<br/>

### ㅁ 4.3 KoNLPy 패키지와 코모란 형태소 분석기 설치

- 형태소 분석기를 사용하기 위해 설치하는 파이썬 패키지
- 설치 명령어

```shell
(chatbot) [디렉토리 패스] > pip install konlpy
```

```shell
(chatbot) [디렉토리 패스] > pip install pyKomoran
```

<br/>

### ㅁ 4.4 Gensim 패키지 설치

- Word2Vec 임베딩을 사용하기 위해 설치

```shell
(chatbot) [디렉토리 패스] > pip install gensim
```

<br/>

### ㅁ 4.5 사이킷런 패키지 설치

- 머신러닝에 필요한 도구를 제공하는 라이브러리
- train_test_split()함수를 사용하기 위해 설치

```shell
(chatbot) [디렉토리 패스] > pip install sklearn
```

<br/>

### ㅁ 4.6 Seqeval 패키지 설치

- 시퀀스 레이블 점수 평가에 사용하는 파이썬 프레임워크
- 평가 모델의 F1 스코어를 계산하기 위해 설치

```shell
(chatbot) [디렉토리 패스] > pip install seqeval
```

<br/>

### ㅁ 4.7 PyMySQL 패키지 설치

- 파이썬에서 MySQL을 사용하기 위해 설치
- 학습 데이터베이스를 제어하기 위해 설치

```shell
(chatbot) [디렉토리 패스] > pip install pyMysql
```

<br/>

### ㅁ 4.8 OpenPyXL 패키지 설치

- 파이썬에서 엑셀 파일을 제어하기 위해 설치

```shell
(chatbot) [디렉토리 패스] > pip install openpyxl
```

<br/>

### ㅁ 4.9 Pandas,xlrd 패키지 설치

- Pandas 패키지는 데이터 분석 및 처리를 위한 라이브러리
- xlrd 패키지는 Pandas 패키지에서 엑셀 파일을 제어하기 위해 사용하는 패키지
- 데이터 분석을 위해 사용

```shell
(chatbot) [디렉토리 패스] > pip install pandas xlrd
```

<br/>

### ㅁ 4.10 Matplotlib 패키지 설치

- 데이터를 시각화하는 데 필요한 도구 제공
- 데이터 플롯을 그리기 위해 사용

```shell
(chatbot) [디렉토리 패스] > pip install matplotlib
```

<br/>

### ㅁ 4.11 Flask 웹 프레임워크와 Requests 패키지 설치

- Flask는 파이썬에서 웹 애플리케이션 개발을 도와주는 경량화된 웹 프레임워크
  - REST API 개발을 위해 설치

- Request는 파이썬에서 HTTP 요청을 보내는 모듈
  - 외부 API 호출을 위해 설치

```shell
(chatbot) [디렉토리 패스] > pip install flask
(chatbot) [디렉토리 패스] > pip install requests
```

<br/>

## 5. PyCharm 설치 및 프로젝트 생성

- 파이썬 프로젝트를 진행할 때 IDE를 사용하면 개발에 많은 도움이 됨
- 이 책에서는 파이참 기준으로 설명
- Jet Brains에서 만든 IDE이며, 프로페셔널 버전과 무료로 사용 가능한 커뮤니티 버전이 있음

<br/>

[파이참 공식 홈페이지](jetbrains.com/pycharm)에 접속하여 설치 진행

<br/>

### 다운로드

![파이참 다운로드](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_download.png){: width="500" height="500"}

![파이참 다운로드](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_download2.png){: width="500" height="500"}

- 다운로드하는 방법은 매우 간단하다.

---

### 새 프로젝트 생성

![새프로젝트 생성](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_new_projcet.png){: width="500" height="500"}

<br/>

![인터프리터 설정](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_new_projcet2.png){: width="500" height="500"}

<br/>

![인터프리터 경로 설정](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_new_projcet3.png){: width="500" height="500"}

<br/>

![인터프리터 경로 설정 문제](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_new_projcet_problem.png){: width="500" height="500"}

<br/>

* 파이썬 인터프리터 위치를 해당 가상 환경에 맞게 지정해야 한다.

* 교재에서는 ```conda env list```하여 나오는 가상환경 경로에 `\bin\python` 만 붙여서 파이썬 인터프리터 경로로 사용하라고 한다.

* 하라는 대로 했는데 인터프리터 설정이 안된다.

* 필자는 맥을 사용하는 방법만 보여 준다.

  <br/>

![인터프리터 경로 설정 완료](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_new_projcet_set_interpreter.png){: width="500" height="500"}

- 일단 실행 후 설정하려고 보니 알아서 설정이 되어 있다.

  <br/>

![디폴트 코드 실행](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_run.png){: width="500" height="500"}

- 디폴트 코드 실행 화면
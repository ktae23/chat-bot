# 개발환경 구축

## 5. PyCharm 설치 및 프로젝트 생성

- 파이썬 프로젝트를 진행할 때 IDE를 사용하면 개발에 많은 도움이 됨
- 이 책에서는 파이참 기준으로 설명
- Jet Brains에서 만든 IDE이며, 프로페셔널 버전과 무료로 사용 가능한 커뮤니티 버전이 있음

<br/>

[파이참 공식 홈페이지](jetbrains.com/pycharm)에 접속하여 설치 진행

<br/>

### 다운로드

![파이참 다운로드](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_download.png)

![파이참 다운로드](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_download2.png)

- 다운로드하는 방법은 매우 간단하다.

---

### 새 프로젝트 생성

![새프로젝트 생성](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_new_projcet.png)

<br/>

![인터프리터 설정](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_new_projcet2.png)

<br/>

![인터프리터 경로 설정](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_new_projcet3.png)

<br/>

![인터프리터 경로 설정 문제](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_new_projcet_problem.png)

<br/>

* 파이썬 인터프리터 위치를 해당 가상 환경에 맞게 지정해야 한다.

* 교재에서는 ```conda env list```하여 나오는 가상환경 경로에 `\bin\python` 만 붙여서 파이썬 인터프리터 경로로 사용하라고 한다.

* 하라는 대로 했는데 인터프리터 설정이 안된다.

* 필자는 맥을 사용하는 방법만 보여 준다.

  <br/>

![인터프리터 경로 설정 완료](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_new_projcet_set_interpreter.png)

- 일단 실행 후 설정하려고 보니 알아서 설정이 되어 있다.

  <br/>

![디폴트 코드 실행](https://github.com/ktae23/Chat-Bot/blob/master/Chatbot_Study/APPENDIX_A/img/pycharm_run.png)

- 디폴트 코드 실행 화면
# covid19_WordCloud
코로나 관련된 기사들의 데이터를 모아 분석하여 word cloud로 시각화, NLTK를 통해 자연어처리로 원하는 데이터로 처리합니다. 


## PR Form
Feature : new function develop 새로운 기능 개발 <br>
Update : old function fix and upgrade 기존 기능 향상 <br>
Bug : bug fix 버그 수정 <br>
Enhancement : New feature or request 기능 요청, 제안 <br>
Documentation : 문서화 <br>
태크를 꼭 달아주세요.<br>
<br>
ex)React is not executed in the django (tag bug)
<br>

## Branch Policy
master - develop - feature <br>
master : 최종 배포할 버전 <br>
develop : master로 병합하기 전 최종 확인 단계, 및 새로 개발할 feature의 root브랜치 <br>
feature : 개발을 시작 할 시 생성될 브랜치 <br>
<br>
여기서 저희는 세가지만 사용합니다. <br>

ex) feature/bootstarp_flex_apply <br>
ex) feature/word_cloud_form_change <br>
[참고 정보 git flow](https://woowabros.github.io/experience/2017/10/30/baemin-mobile-git-branch-strategy.html)

<br>
## environment
- python==3.7
- django==3.1.2

그 외 라이브리러는 requirements.txt 참조.

## Install
1. 가상환경 
```
conda create -n WordCloud python=3.7
activate WordCloud
```

2. 프로젝트 설치
```
git clone https://github.com/ddusi/covid_WordCloud.git
cd covid_wordCloud
```

3. 라이브러리들 설치
```
pip install cloudworld
pip install olefile
pip install tornado
pip install -r requirements.txt
python -m nltk.downloader all
```

4. django 실행
```
python manage.py runserver
```

5. 서버 접속 URLs
```
http://localhost:8000/Covid_web/
```


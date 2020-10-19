# covid19_WordCloud
코로나 관련된 기사들의 데이터를 모아 분석하여 word cloud로 시각화, NLTK를 통해 자연어처리로 원하는 데이터로 처리합니다. 


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
pip install -r requirements.txt
nltk.download()
```

4. django 실행
```
python manage.py runserver
```

5. 서버 접속 URLs
```
http://localhost:8000/Covid_web/
```


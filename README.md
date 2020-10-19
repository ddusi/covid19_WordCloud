# covid_WordCloud

장연주님 외주 설명 및 변경점.
공공데이터 API를 내부 DRF API서버와 연동하여 데이터 가공 후 원하는 정보만 화면에 출력하는 작업입니다.

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


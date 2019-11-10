### 4일차 스터디
### git 복습, Django 프레임워크

python3 사용 환경 세팅하기!!!
python 환경변수 세팅하기

가상머신 생성 (나는 python 두개깔려서 선택해야함)
> python3 -m venv myvenv          myvenv : 생성할 가상머신 이름

가상머신 on
> source myvenv/bin/activate

가상머신 off
> deactivate

python 모듈 관리 툴  pip
> pip list       입력시 설치된 모듈 확인가능

장고설치
> pip install django==2.2.7

"firstproject" 이름의 장고 첫 프로젝트 생성
> django-admin startproject firstproject

장고 웹서버 실행
> python manage.py runserver
> control + c    서버종료

1. APP (testapp) 추가

> firstproject > setting.py 파일안의
> INSTALLED_APPS 에 'testapp.apps.TestappConfig',   추가

2. root화면 추가

> testapp 폴더 밑에  "templates" 폴더추가
> "templates" 폴더 밑에 index.html 파일 생성

3. view 함수 추가

> testapp / views.py 폴더아래 함수 추가

```
def index(request):

    return render(request, 'index.html')
```

4. url 추가

> "firstproject" / urls.py 파일에
> 1. import testapp.views                                    -> views.py 파일 임포트하기!!!
> 2. path('start', testapp.views.index, name="index"),       ->  path 추가
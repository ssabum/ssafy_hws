from django.shortcuts import render
from django.shortcuts import redirect
from .models import Article

# Create your views here.
def index(request):
    # 모든 게시글 조회
    # articles = Article.objects.all()[::-1] # 파이썬 언어로 해결
    articles = Article.objects.order_by('-pk') # DB 단에서 해결
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # GET 요청으로 들어온 사용자 데이터를 추출
    title = request.GET.get('title')
    content = request.GET.get('content')

    # Article 모델 클래스를 기반으로 인스턴스를 생성
    article = Article(title=title, content=content)

    # DB에 저장
    article.save()

    return redirect('articles:index')

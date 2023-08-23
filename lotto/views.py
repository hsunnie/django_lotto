from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all() #GuessNumbers의 모든 행을 lottos라는 변수에 저장
    return render(request, 'lotto/default.html', {'lottos':lottos}) # context-dict에 value로 lottos 넣어줌. key값은 value와 동일한 명칭으로 설정함

def post(request):

    if request.method == 'POST': # POST 요청이 들어온 경우
        form = PostForm(request.POST) # form의 type: class 'lotto.forms.PostForm'

        if form.is_valid(): # 사용자의 입력값이 문제 없는지 validation
            lotto = form.save(commit=False) # DB에는 저장하지 않지만, 사용자의 값을 임시로 저장함-generate 함수 실행하기 위함 # lotto의 type: class 'lotto.models.GuessNumbers'
            lotto.generate() # 로또 번호를 자동으로 생성 (generate함수 안에 save가 있으므로 따로 save하지 않음)
            return redirect('index') # 이동할 url의 별명을 redirect 안에 지정한다.
    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey) # pk == id
    return render(request, 'lotto/detail.html', {'lotto':lotto})

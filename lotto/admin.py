from django.contrib import admin
from lotto.models import GuessNumbers
# 현재 파일과 동일한 폴더에 위치한 models.py 파일의 GuessNumbers class를 사용하므로 폴더명은 생략해도 된다. (from .models import GuessNumbers)
# Register your models here.
admin.site.register(GuessNumbers)

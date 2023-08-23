from django import forms
from .models import GuessNumbers


class PostForm(forms.ModelForm): # Form을 통해 받아들여야할 데이터가 명시되어 있는 메타 데이터(DB table을 연결함)
    class Meta:
        model = GuessNumbers
        fields = ('name', 'text',) # 사용자로부터 Form을 통해 입력받을 데이터
        

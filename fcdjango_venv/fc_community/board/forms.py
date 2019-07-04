from django import forms
from .models import Board

class BoardForm(forms.Form) : 
    title = forms.CharField(max_length=128, label="제목", error_messages={'required' : '제목을 입력해주세요'})
    contents = forms.CharField(widget=forms.Textarea, label="내용", error_messages={'required' : '내용을 입력해주세요'})
    tags = forms.CharField(required=False, label="태그")

    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get('username')
    #     password = cleaned_data.get('password')

    #     if username and password:
    #         fcuser = Fcuser.objects.get(username=username)
    #         if not check_password(password, fcuser.password) :
    #             self.add_error('password', '비밀번호가 틀렸습니다.')
    #         else:
    #             self.user_id = fcuser.id
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

     class Meta:
        # 連帯するUSERモデルの設定
        model = CustomUser
        # フォームで使用するフィールドの設定
        # ユーザー名、メールアドレス、パスワード、パスワード（確認用）
        fields = ('username','email','password1','password2')
        
from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    # forms.pyで定義したフォームのクラス
    form_class = CustomUserCreationForm
    # レンダリングするテンプレート
    template_name = "signup.html"
    # サインアップ完了後のリダイレクト先のURLパターン
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self,form):
    # スーパークラスのform_validの戻り値を返すことで、success_urlで設定されているURLにリダイレクトさせる
        user = form.save() 
        self.object = user
        return super().form_valid(form)
    # createviewクラスのform_valid()をオーバライド
    #フォームのバリテーションを通過したときに呼ばれる、フォームデータの登録を行う

class SignUpSuccessView(TemplateView):
    template_name = "signup_success.html"
    # サインアップ完了のビュー
    # レンダリングするテンプレート
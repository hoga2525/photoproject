from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PhotoPost



class IndexView(TemplateView):
    template_name = 'index.html'
    queryset = PhotoPost.objects.order_by('-posted_at')
    paginate_by = 9

@method_decorator(login_required,name='dispatch')
class CreatePhotoView(CreateView):
#PhotoPostFormで定義されているモデルをフィールドと連携して投稿データをデータベースに登録する 
    # forms.pyのPhotoPostFormをフォームクラスとして登録
    form_class = PhotoPostForm
    # レンダリングするテンプレート
    template_name = "post_photo.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('photo:post_done')

    def form_valid(self,form):
        # フォームのバリでぇーしょんを通過したときに呼ばれるフォームデータの登録を行う
        # COMMIT=FALSEにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのIDを取得してモデルのUSERフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータべースに登録
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = 'post_success.html'

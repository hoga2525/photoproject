from django.db import models
from accounts.models import CustomUser

# 投稿する写真を管理するモジュール
class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20)
    def __str__(self):#オブジェクトを文字列に変換して返す
        return self.title
    
# 投稿されたデータを管理するモデル
class PhotoPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='カテゴリ',
        # カテゴリに関連付けられた投稿データが存在する場合、
        #そのカテゴリを削除出来ないようにする
        on_delete=models.CASCADE
        )
# categoryモデルとphotopostモデルを一体多の関係で結びつける
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
    )

    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=200
    )

    comment = models.TextField (
        verbose_name='コメント'
    )

    image1 = models.ImageField(
        verbose_name='イメージ１',
        upload_to = 'photos'
    )

    image2 = models.ImageField(
        verbose_name='イメージ２',
        upload_to = 'photos',
        blank=True,
        null=True
    )

    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )

    def __str__(self):
        return self.title
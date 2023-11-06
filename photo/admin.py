from django.contrib import admin
from .models import Category,PhotoPost

class CategoryAdmin(admin.ModelAdmin):
    # 管理ページのレコード一覧に表示するカラムを設定する

    list_display = ('id','title')
    list_display_links = ('id','title')

class PhotoPostAdmin(admin.ModelAdmin):
    # 管理ページのレコード一覧に表示するカラムを設定するクラス
    list_display = ('id','title')
    list_display = ('id','title')

# django管理サイトにCategory,CategoryAdminを登録する
admin.site.register(Category,CategoryAdmin)

# django管理サイトにPhotoPOst,PhotoPostAdminを登録する
admin.site.register(PhotoPost,PhotoPostAdmin)
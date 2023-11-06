from django.urls import path
from .views import IndexView
from . import views


app_name = 'photo'
urlpatterns = [
    path('',IndexView.as_view(), name ='index'),

    path('post/', views.CreatePhotoView.as_view(),name='post'),

    path('post_done/',views.PostSuccessView.as_view(),name='post_done')
    ]

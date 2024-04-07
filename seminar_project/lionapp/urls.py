from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    #create/주소로 url을 입력 받으면 view의 create_post 함수를 실행하겠다!
    path('create/', views.create_post),
    #int type의 url을 받는다면~ / get
    path('<int:pk>/', views.get_post),
    path('delete/<int:pk>', views.delete_post)
]
from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path('', views.music_list),
    path('<pk>/', views.music_detail),

]
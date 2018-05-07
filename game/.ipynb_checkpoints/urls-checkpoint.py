from django.urls import path

from . import views

urlpatterns = [
    path('/', views.index,),
    path('next/',views.next,name='next'),
    path('init/',views.init,name='init'),
    path('info/',views.getInfo,name='info')
]


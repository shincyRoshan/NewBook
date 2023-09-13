from django.urls import path, include
from . import views
app_name='BookApp'
urlpatterns = [

    path('',views.index,name='index'),
    path('book/<int:Bid>/',views.detail,name='detail'),
    path('add/', views.add_book, name='add_book'),
    path('update/<int:id>/', views.update_book, name='update_book'),
    path('delete/<int:id>/', views.delete_book, name='delete_book')
]

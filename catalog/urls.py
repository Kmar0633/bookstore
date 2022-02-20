from django.urls import path
from . import views

urlpatterns = [

]


urlpatterns += [
    path('', views.index, name='index'),
 
    path('delete_book/<book_id>', views.delete_book, name='delete-book'),
    path('add_book/', views.add_book, name='add-book'),
    path('error_page/', views.index, name='error-page'),

 
]




from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('delete_book/<book_id>', views.delete_book, name='delete-book'),
    path('add_book/', views.add_book, name='add-book'),
    path('add_profile_picture/<user_id>', views.add_profilepicture, name='add-profilepicture'),
    path('error_page/', views.index, name='error-page')
 
]




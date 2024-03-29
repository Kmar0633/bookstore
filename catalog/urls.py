from django.urls import path
from . import views



urlpatterns = [
    path('', views.book_list_view, name='book-list-view'),
    path('delete_book/<book_id>', views.delete_book, name='delete-book'),
    path('add_book/', views.add_book, name='add-book'),
    path('add_profile_picture/<user_id>', views.add_profilepicture, name='add-profilepicture'),
    path('error_page/', views.book_list_view, name='error-page')
 

]




from django.urls import path
from .views import home, book_list, manage_books, borrow_book, return_books, login_view, register

app_name = 'mywebapp'

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='book_list'),
    path('manage_books/', manage_books, name='manage_books'),
    path('borrow_book/', borrow_book, name='borrow_book'),
    path('return_books/', return_books, name='return_books'),
    path('login/', login_view, name='login'),  # 確保這裡的名稱是 'login'
    path('register/', register, name='register'),
    path('book_list/', book_list, name='book_list_view'),
]

from django.urls import include, path
from mywebapp.views import home, book_list, manage_books, borrow_book, return_books, login_view, register, user_login, home_book_list
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/book_list.html', book_list, name='login_book_list_html'),
    path('manage_books/', manage_books, name='manage_books'),
    path('borrow_book/<int:book_id>/', borrow_book, name='borrow_book'),
    path('return_books/', return_books, name='return_books'),
    path('login/', user_login, name='user_login'),
    path('register/', register, name='register'),
    path('home/', home_book_list, name='home_book_list'),
    #path('books/', include(('mywebapp.urls', 'mywebapp'), namespace='mywebapp')),
]

# 加上這行以提供媒體文件
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

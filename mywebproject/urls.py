from django.urls import include, path
from mywebapp.views import home, book_list, manage_books, borrow_book, return_books, login_view, register, user_login, home_book_list,process_returns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from mywebapp.views import borrow_records


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('manage_books/', manage_books, name='manage_books'),
    path('borrow_book/<int:book_id>/', borrow_book, name='borrow_book'),
    path('return_books/<int:book_id>/', return_books, name='return_books'),
    path('user_login/', user_login, name='user_login'),  # Assuming 'user_login' is your login view
    path('register/', register, name='register'),
    path('home/', home_book_list, name='home_book_list'),
    path('login/', include('mywebapp.urls', namespace='mywebapp')),
    path('book_list/', book_list, name='book_list'),
    path('user_login/book_list.html', book_list, name='book_list_view'),
    path('user/', include('mywebapp.urls', namespace='mywebapp')),
    # 例如，urls.py 中的片段可能如下所示：
    path('process_returns/', process_returns, name='process_returns'),
    path('borrow_records/', borrow_records, name='borrow_records'),
]


# 加上這行以提供媒體文件
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

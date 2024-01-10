from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book, BorrowRecord,BorrowedBook, Book, BorrowRecord
from .forms import BookForm, BorrowBookForm, ReturnBookForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
import os
from django.conf import settings
books = Book.objects.all()

for book in books:
    if not book.id:
        print(f"Book with title '{book.title}' does not have a valid ID.")


def process_returns(request):
    if request.method == 'POST':
        books_to_return = request.POST.getlist('return_books')
        BorrowedBook.objects.filter(id__in=books_to_return).update(returned=True)

        # 根據需要重定向到用戶個人頁面或其他適當的位置
        return redirect('user_profile')

    # 如果不是 POST 請求，你也可以在這裡添加相應的處理邏輯
    # ...

    # 如果需要，你也可以在這裡添加一個默認的重定向
    return redirect('book_list')


def book_list(request):
    query = request.GET.get('q', '')  # 從查詢字串中獲取查詢內容，如果沒有則預設為空字串
    books = Book.objects.all()

    # 如果有查詢內容，使用 filter 過濾書籍列表
    if query:
        books = books.filter(title__icontains=query)

    return render(request, 'book_list.html', {'books': books, 'query': query})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list.html')  # 將 'home' 替換為你的首頁視圖的名稱
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # 將 'home' 替換為你的首頁視圖的名稱
    else:
        form = UserCreationForm()
    
    template_path = os.path.join(settings.BASE_DIR, 'mywebapp/templates/register.html')
    print(f'Template Path: {template_path}')
    
    return render(request, 'registration/register.html', {'form': form})



import logging

def login_view(request):
    logger = logging.getLogger(__name__)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                logger.debug(f'Successfully logged in: {user.username}')
                # 登入成功後將頁面導向到 home.html
                return redirect('book_list')
            else:
                messages.error(request, 'Invalid username or password.')
                logger.warning('Login failed: Invalid username or password.')

    # 在 GET 請求時或登入失敗時返回登入頁面
    return render(request, 'registration/login.html')

def home_book_list(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def home(request):
    # 處理視圖邏輯的代碼
    # 在 mywebapp/views.py 中的 home 函數中添加這些 import
    import logging

    # 在 home 函數中的開頭添加這個 logger
    logger = logging.getLogger(__name__)

    # 在 home 函數中的適當位置添加這條測試日誌
    logger.debug("這是一條測試日誌")

    return render(request, 'home.html')


@login_required
def manage_books(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '書籍已添加成功！')
    else:
        form = BookForm()

    books = Book.objects.all()
    return render(request, 'manage_books.html', {'form': form, 'books': books})



def borrow_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        # 假設你有一個表示書籍數量的字段為 'quantity'，你可以在這裡減去 1
        if book.quantity > 0:
            book.quantity -= 1
            book.save()
            # 在這裡你還可以添加其他相關的借書邏輯，例如創建借書記錄等
            messages.success(request, '借閱成功，感謝您的支持！廣告：老師分下留情qwq')
            return redirect('book_list')
        else:
            messages.error(request, '借閱失敗，請檢查您的借閱信息。')
            # 不進行重定向，讓用戶保留在當前頁面
        
    return render(request, 'borrow_book.html', {'book': book})




def return_books(request, book_id):
    user = request.user
    
    # 取得使用者已借閱但未歸還的書籍
    borrowed_books = BorrowedBook.objects.filter(user=user, returned=False)
    
    # 如果使用者沒有借閱或者已經歸還所有書籍，直接重定向到書籍列表頁面
    if not borrowed_books.exists():
        return redirect('book_list')

    # 渲染還書頁面
    return render(request, 'return_book.html', {'borrowed_books': borrowed_books})

    


@login_required
def logged_in_home(request):
    books = Book.objects.all()
    return render(request, 'logged_in_home.html', {'books': books})

def your_view(request):
    # ... 你的代碼 ...

    print(messages.get_messages(request))
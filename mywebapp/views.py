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

def process_returns(request):
    if request.method == 'POST':
        books_to_return = request.POST.getlist('return_books')
        BorrowedBook.objects.filter(id__in=books_to_return).update(returned=True)
    return redirect('user_profile')  # 重定向到用戶個人頁面或其他適當的位置


def book_list(request):
    # 获取书籍列表，这里假设您已经有了获取书籍列表的方法
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})



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
            messages.success(request, '借閱成功，感謝您的支持！廣告：XXX')
            return redirect('book_list')
        else:
            messages.error(request, '借閱失敗，請檢查您的借閱信息。')
            # 不進行重定向，讓用戶保留在當前頁面
        
    return render(request, 'borrow_book.html', {'book': book})


def return_books(request, book_id):
    user = request.user
    borrowed_books = BorrowedBook.objects.filter(user=user, returned=False)
    return render(request, 'return_book.html', {'borrowed_books': borrowed_books})
    try:
        # 根據書籍ID查找書籍
        book = Book.objects.get(id=book_id)
        
        # 檢查書籍是否被借閱
        borrowed_book = BorrowedBook.objects.get(book=book, returned=False)

        # 將書籍標記為歸還
        borrowed_book.returned = True
        borrowed_book.save()

        # 在實際應用中，你可能還需要更新用戶的借書記錄、計算逾期費用等等

        messages.success(request, f'書籍 "{book.title}" 歸還成功。')
    except Book.DoesNotExist:
        messages.error(request, '找不到該書籍。')
    except BorrowedBook.DoesNotExist:
        messages.error(request, '該書籍未被借閱。')

    return redirect('home')  # 將用戶重新導向到首頁或其他頁面


@login_required
def logged_in_home(request):
    books = Book.objects.all()
    return render(request, 'logged_in_home.html', {'books': books})

def your_view(request):
    # ... 你的代碼 ...

    print(messages.get_messages(request))
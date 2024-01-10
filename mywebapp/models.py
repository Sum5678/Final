from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    # 定义作者模型的字段
    name = models.CharField(max_length=255)
    # 其他字段...

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)         # 书籍的类别        
    quantity = models.PositiveIntegerField(default=0)   #书籍的数量
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    # 其他欄位...
    
    # 定義書籍的三種狀態
    AVAILABLE = 'available'
    CHECKED_OUT = 'checked_out'
    RESERVED = 'reserved'
    STATUS_CHOICES = [
        (AVAILABLE, '可借阅'),
        (CHECKED_OUT, '借閱中'),
        (RESERVED, '已预约'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=AVAILABLE,
    )

    def __str__(self):
        return self.title

# models.py
class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"


class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
    returned = models.BooleanField(default=False)
from django.contrib import admin
from .models import Book
from .forms import BookForm

class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('id', 'title', 'category', 'quantity', 'author', 'status','cover_image')
    list_filter = ('status', 'category')
    search_fields = ('title', 'author__name', 'book_id')
    fields = ('title', 'category', 'quantity', 'author', 'status')
    prepopulated_fields = {'id': ('title',)}  # 自动填充 book_id 字段
    readonly_fields = ('status',)  # 将 status 字段设为只读

#admin.site.register(Book, BookAdmin)


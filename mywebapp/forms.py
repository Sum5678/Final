from django import forms
from django.db import models
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Book, Author, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

class BorrowBookForm(forms.Form):
    user_id = forms.IntegerField(label='User ID', required=True)
    book_id = forms.IntegerField(label='Book ID', required=True)
    borrow_date = forms.DateField(label='Borrow Date', required=True)
    return_date = forms.DateField(label='Return Date', required=True)

class ReturnBookForm(forms.Form):
    book_id = forms.IntegerField(label='Book ID', required=True)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'category', 'quantity', 'title']

# 确保 AuthorForm 类继承自 models.Model，并定义了正确的字段
class AuthorForm(models.Model):
    # 其他字段...

    def __str__(self):
        return self.name

from django.contrib import admin

from .models import Book, Author, Address, Country


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",) #Model.py의 슬러그 속성에 대한  수정 불가 기능 추가와 같음
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author" ,"rating") # 필터링을 통한 데이터 분류 할수있게 하는 기능
    list_display = ("title", "author") # 데이터에 대한 속성 이름 표시

admin.site.register(Book , BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
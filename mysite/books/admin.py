from django.contrib import admin

# Register your models here.
from .models import Publisher,Author,Book
class AuthorAdmin(admin.ModelAdmin):
	list_display=('first_name','middle_name','email')
	search_fields=('first_name','middle_name')
class BookAdmin(admin.ModelAdmin):
	list_display=('title','authors')
	search_fields=('title','authors')
	date_hierarchy="Publisher_date"
admin.site.register(Publisher)
admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)

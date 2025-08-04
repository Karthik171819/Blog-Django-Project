from django.contrib import admin
from .models import Post, Category, AboutUs


#customize admin interface
# class PostAdmin(admin.ModelsAdmin):
#     list_display = ('title','content')
#     search_fields = ('title','content')
#     list_filter = ('category', 'created_at')
#remeber when you want to use this customized admin_page comment out this before running


#Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(AboutUs)


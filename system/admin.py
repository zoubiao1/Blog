from django.contrib import admin

from models import *
# Register your models here.

from blog.models import *


#
# @admin.register(User)
class AreaAdmin(admin.ModelAdmin):
    pass

admin.site.register(User,AreaAdmin)


class AreaBlogArticle(admin.ModelAdmin):
    list_per_page = 100
    # date_hierarchy = 'gmt_create'
    list_display =  ['id','gmt_create','gmt_modified']
    list_filter = ['id']
    search_fields = ['id']
    list_display_links = ['id','gmt_create','gmt_modified']



admin.site.register(BlogArticle)
admin.site.register(BlogArticleContent,AreaBlogArticle)
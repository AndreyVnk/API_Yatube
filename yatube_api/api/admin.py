from django.contrib import admin

from .models import Post, Comment, Follow


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'post')
    search_fields = ('text',)
    list_filter = ('created', 'author')
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'following')
    search_fields = ('user', 'following')
    list_filter = ('user', 'following')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)

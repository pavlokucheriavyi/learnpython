from django.contrib import admin

from .models import Ask, Job, Story


class AskAdmin(admin.ModelAdmin):
    list_display = ('by', 'descendants', 'id_articles', 'kids', 'score', 'text', 'time', 'title', 'type')
    list_display_links = ('by', 'id_articles')
    search_fields = ('id_articles', )


admin.site.register(Ask, AskAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display = ('by', 'id_articles', 'score', 'time', 'title', 'type', 'url')
    list_display_links = ('by', 'id_articles')
    search_fields = ('id_articles', )


admin.site.register(Job, JobAdmin)


class StoryAdmin(admin.ModelAdmin):
    list_display = ('by', 'descendants', 'id_articles', 'kids', 'score', 'text', 'time', 'title', 'type', 'url')
    list_display_links = ('by', 'id_articles')
    search_fields = ('id_articles', )


admin.site.register(Story, StoryAdmin)

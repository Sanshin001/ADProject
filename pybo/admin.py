from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'author', 'create_date', 'view_count')
    search_fields = ('subject', 'content')
    list_filter = ('create_date', 'author')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'create_date', 'question')
    search_fields = ('content',)
    list_filter = ('create_date', 'author')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

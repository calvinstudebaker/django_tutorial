from django.contrib import admin

from .models import Question, Choice, Tag

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class TagInLine(admin.TabularInline):
    model = Tag
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline, TagInLine]
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

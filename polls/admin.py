from django.contrib import admin
from .models import Question, Choice

class JOJKO(admin.ModelAdmin):
    list_display = (
            'question_text',
            'pub_date',
            'choices_count')
    def choices_count(self, obj):
        return obj.qqs.count()



class CAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'votes')
    list_filter = ('question', 'votes')
    search_fields = ('choice_text',)
    actions = ('zresetuj',)
    def zresetuj(self, request, queryset):
        ile = queryset.update(votes=0)
        self.message_user(
                request, 
                "zresetowano %s odpowiedzi." % ile)
    zresetuj.short_description = "Zresetuj odpowiedzi"

admin.site.register(Question, JOJKO)
admin.site.register(Choice, CAdmin)

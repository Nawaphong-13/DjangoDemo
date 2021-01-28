from django.contrib import admin
from .models import ALLStudent, ExamScore

# Register your models here.

class ExamScoreAdmin(admin.ModelAdmin):
    list_display = ['subject', 'student_name', 'score']
    list_filter = ['subject']
    list_editable = ['score']



admin.site.register(ExamScore, ExamScoreAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'level', 'student_name', 'student_tel']
    list_filter = ['level']
    list_editable = ['student_tel']



admin.site.register(ALLStudent, StudentAdmin)
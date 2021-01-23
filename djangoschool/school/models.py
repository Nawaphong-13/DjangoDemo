from django.db import models

# Create your models here. (ฐานข้อมูล)

class ExamScore(models.Model):

    allsubject = (
                    ('คณิตศาสตร์','คณิตศาสตร์'),
                    ('วิทยาศาสตร์','วิทยาศาสตร์'),
                    ('ศิลป','ศิลป'),
                    ('ภาษาอังกฤษ','ภาษาอังกฤษ'),
                    ('ฟิสิกส์','ฟิสิกส์'),
                    ('ชีววิทยา','ชีววิทยา')
                )

    subject = models.CharField(max_length=200, choices=allsubject, default='math')
    student_name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def __str__(self):                     # Show ชื่อนักเรียนในฐานข้อมูล
        return self.student_name + '-' + self.subject + '-' + str(self.score)

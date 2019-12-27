from django.db import models
from apps.teacher.models import Teacher, Category, Linkage, Study
import hashlib
import time

# Create your models here.
class Career(models.Model):
    career_id = models.AutoField(primary_key=True)
    career_name = models.CharField(max_length=100, blank = False, null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.career_name

class Subject(models.Model):
    subject_id = models.CharField(max_length=50, primary_key=True)
    subject_code = models.CharField(max_length=10, blank = False, null = False)   
    subject_name = models.CharField(max_length=60, blank = False, null = False)
    subject_credits = models.IntegerField(blank = False, null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject_code + ' ' + self.subject_name
    
    def save(self, **kwargs):
        if not self.subject_id:
            self.subject_id = hashlib.sha1((self.subject_code + str(time.time())).encode()).hexdigest()
        super().save(**kwargs)

class Resolution(models.Model):
    resolution_id = models.CharField(max_length=50, primary_key=True)
    resolution_teacher_id = models.ForeignKey(Teacher, on_delete = models.PROTECT)
    resolution_category_id = models.ForeignKey(Category, on_delete = models.PROTECT)
    resolution_linkage_id = models.ForeignKey(Linkage, on_delete = models.PROTECT)
    resolution_study_id = models.ForeignKey(Study, on_delete = models.PROTECT)
    resolution_start_date = models.DateField(blank = False, null = False)
    resolution_end_date = models.DateField(blank = False, null = False)
    resolution_hours = models.IntegerField(blank = False, null = False)
    resolution_total_qualification = models.FloatField(blank = False, null = False)
    resolution_total_seedbed = models.FloatField(blank = False, null = False)
    resolution_total_group = models.FloatField(blank = False, null = False)
    resolution_total_teacher = models.FloatField(blank = False, null = False)

    def __str__(self):
        return str(self.resolution_start_date) +' - '+ str(self.resolution_end_date)

    def save(self, **kwargs):
        if not self.resolution_id:
            self.resolution_id = hashlib.md5((self.resolution_teacher_id + str(self.resolution_start_date) + str(time.time())).encode()).hexdigest()
        super().save(**kwargs)

    



from django.db import models
import hashlib
import time

# Create your models here.

class Category(models.Model):
    category_id = models.CharField(max_length=50, primary_key=True)
    category_name = models.CharField('Nombre de categoría', max_length=30, blank = False, null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

    def save(self, **kwargs):
        if not self.category_id:     
            self.category_id = hashlib.md5((self.category_name + str(time.time())).encode()).hexdigest()
        super().save(**kwargs)

class Linkage(models.Model):
    linkage_id = models.AutoField(primary_key=True)
    linkage_name  = models.CharField('Nombre de vinculación', max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['linkage_name']

    def __str__(self):
        return self.linkage_name 

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=50, primary_key=True)
    teacher_dni = models.CharField('Documento de identidad', blank=False, null=False, max_length=20, unique=True)
    teacher_name = models.CharField('Primer nombre', max_length=30, blank = False)
    teacher_middle_name = models.CharField('Segundo nombre', max_length=30, blank=True)
    teacher_last_name = models.CharField('Primer apellido', max_length=30, blank=False)
    teacher_middle_last_name = models.CharField('Segundo apellido', max_length=30, blank = True)
    teacher_category_id = models.ForeignKey(Category, on_delete = models.PROTECT)
    teacher_linkage_id = models.ForeignKey(Linkage, on_delete = models.PROTECT)
    teacher_status = models.BooleanField('Estado', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.teacher_name, self.teacher_last_name)
    
    def save(self, **kwargs):
        if not self.teacher_id:     
            self.teacher_id = hashlib.md5((self.teacher_dni + str(time.time())).encode()).hexdigest()
        super().save(**kwargs)


class Study(models.Model):


    PREGRADO = 'PREGRADO'
    ESPECIALIZACION = 'ESPECIALIZACION'
    MAESTRIA = 'MAESTRIA'
    DOCTORADO = 'DOCTORADO'
    POS_DOCTORADO = 'POS_DOCTORADO'

    TYPE_OF_STUDIES_CHOICES = [
        (PREGRADO, 'Pregrado'),
        (ESPECIALIZACION, 'Especialización'),
        (MAESTRIA, 'Maestría'),
        (DOCTORADO, 'Doctorado'),
        (POS_DOCTORADO, 'Pos-doctorado')
    ]

    study_id = models.AutoField(primary_key=True)
    study_teacher_id = models.ForeignKey(Teacher, on_delete = models.PROTECT)
    study_type = models.CharField(max_length=20, choices = TYPE_OF_STUDIES_CHOICES, default=PREGRADO)
    study_name = models.CharField('Nombre del estudio', max_length=100 ,blank = False, null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.study_type
from django import forms
from .models import Teacher, Category

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_dni', 'teacher_name', 'teacher_middle_name', 'teacher_last_name', 'teacher_middle_last_name', 'teacher_category_id', 'teacher_linkage_id', 'teacher_status']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            # Recorremos todos los campos del modelo para añadirle class="form-control
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields['teacher_status'].widget.attrs.update({'class': 'custom-control-input'})

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_name'].widget.attrs.update({'class': 'form-control'})
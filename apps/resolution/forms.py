from django import forms
from .models import Resolution

class ResolutionForm(forms.ModelForm):
    class Meta:
        model = Resolution
        fields = ['resolution_teacher_id', 'resolution_category_id', 'resolution_linkage_id', 'resolution_start_date', 'resolution_end_date', 'resolution_hours', 'resolution_total_qualification', 'resolution_total_seedbed', 'resolution_total_group', 'resolution_total_teacher']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            # Recorremos todos los campos del modelo para añadirle class="form-control
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields['resolution_hours'].value = '20'   
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from apps.teacher.models import Teacher
from .forms import *

# Create your views here.
class CreateResolution(CreateView):
    form_class = ResolutionForm
    template_name = 'resolution/edit_resolution.html'

    def get_initial(self):   
        teacher = get_object_or_404(Teacher, teacher_id = self.kwargs['pk'])     

        return {'resolution_category_id': teacher.teacher_category_id, 
                'resolution_teacher_id': teacher.teacher_id,
                'resolution_linkage_id': teacher.teacher_linkage_id,
                'resolution_study_id': teacher.teacher_study_id,
                'resolution_start_date': teacher.teacher_study_id.study_percentage
        }
    

    def get_context_data(self, **kwargs):
        kwargs['teacher'] = get_object_or_404(Teacher, teacher_id = self.kwargs['pk'])        
        return super(CreateResolution, self).get_context_data(**kwargs)

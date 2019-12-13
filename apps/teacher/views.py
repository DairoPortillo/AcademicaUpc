from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from .models import Teacher, Category
from .forms import TeacherForm, CategoryForm
from apps.resolution.models import Resolution
# Create your views here.

class CreateTeacher(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher/edit_teacher.html'
    success_url = reverse_lazy('teacher:update_teacher')

class UpdateTeacher(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher/edit_teacher.html'
    #success_url = reverse_lazy('teacher:create_teacher')
    

    """
    @method_decorator(permission_required('teacher.update_teacher'), reverse_lazy('teacher:create_teacher'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateTeacher, self).dispatch(*args, **kwargs)
    """

class DetailTeacher(DetailView):
    model = Teacher    
    template_name = 'teacher/detail_teacher.html'

    def get_context_data(self, **kwargs):
        kwargs['resolutions'] = Resolution.objects.filter(resolution_teacher_id = self.kwargs['pk'])
        return super(DetailTeacher, self).get_context_data(**kwargs)

class CreateCategory(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/edit_category.html'    

    def get_context_data(self, **kwargs):
        kwargs['categories'] = Category.objects.order_by('category_id')
        return super(CreateCategory, self).get_context_data(**kwargs)

    def get_success_url(self):
        return reverse('teacher:update_category', kwargs={'pk': self.object.category_id})   

class UpdateCategory(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/edit_category.html'    
    success_url = reverse_lazy('teacher:create_category')

    def get_context_data(self, **kwargs):
        kwargs['categories'] = Category.objects.order_by('category_id')
        return super(UpdateCategory, self).get_context_data(**kwargs)


    
    

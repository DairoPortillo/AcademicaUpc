from django.urls import path
from .views import CreateTeacher, UpdateTeacher, CreateCategory, UpdateCategory, DetailTeacher

urlpatterns = [

    path('teacher/create/', CreateTeacher.as_view(), name='create_teacher'),
    path('teacher/<str:pk>', DetailTeacher.as_view(), name='detail_teacher'),
    path('teacher/update/<str:pk>', UpdateTeacher.as_view(), name='update_teacher'),
    path('category/create', CreateCategory.as_view(), name='create_category'),
    path('category/update/<str:pk>', UpdateCategory.as_view(), name='update_category'),

]
from django.urls import path
from escola.views import alunos

urlpatterns = [
    path('alunos/', alunos, name='alunos')
]

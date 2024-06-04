from django.urls import path, include
from rest_framework import routers
from escola import views


router = routers.DefaultRouter()
router.register('alunos', views.AlunoViewSet, basename='Alunos')
router.register('cursos', views.CursoViewSet, basename='Cursos')
router.register('matriculas', views.MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', views.ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matriculas/', views.ListaAlunosMatriculados.as_view())
]

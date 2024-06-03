from django.urls import path, include
from rest_framework import routers
from escola.views import AlunoViewSet, CursoViewSet


router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('cursos', CursoViewSet, basename='Cursos')

urlpatterns = [
    path('', include(router.urls))
]

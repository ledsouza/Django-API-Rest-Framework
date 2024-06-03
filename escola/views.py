from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import (AlunoSerializer,
                               CursoSerializer,
                               MatriculaSerializer,
                               ListaMatriculasAlunoSerializer,
                               ListaAlunosMatriculadosSerializer)


class AlunoViewSet(viewsets.ModelViewSet):
    """Exibe todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """Exibe todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibe todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasAluno(generics.ListAPIView):
    """Lista as matrículas de um aluno especificado"""
    serializer_class = ListaMatriculasAlunoSerializer

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset


class ListaAlunosMatriculados(generics.ListAPIView):
    """Lista os alunos matriculados em um determinado curso especificado"""
    serializer_class = ListaAlunosMatriculadosSerializer

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola import serializer


class AlunoViewSet(viewsets.ModelViewSet):
    """Exibe todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = serializer.AlunoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """Exibe todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = serializer.CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibe todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = serializer.MatriculaSerializer


class ListaMatriculasAluno(generics.ListAPIView):
    """Lista as matrículas de um aluno especificado"""
    serializer_class = serializer.ListaMatriculasAlunoSerializer

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset


class ListaAlunosMatriculados(generics.ListAPIView):
    """Lista os alunos matriculados em um determinado curso especificado"""
    serializer_class = serializer.ListaAlunosMatriculadosSerializer

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

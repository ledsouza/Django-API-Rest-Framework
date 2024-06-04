from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.models import Aluno, Curso, Matricula
from escola import serializer


class AlunoViewSet(viewsets.ModelViewSet):
    """Exibe todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = serializer.AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursoViewSet(viewsets.ModelViewSet):
    """Exibe todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = serializer.CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibe todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = serializer.MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    """Lista as matrículas de um aluno especificado"""
    serializer_class = serializer.ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset


class ListaAlunosMatriculados(generics.ListAPIView):
    """Lista os alunos matriculados em um determinado curso especificado"""
    serializer_class = serializer.ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

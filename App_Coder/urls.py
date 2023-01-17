from django.urls import path
from App_Coder.views import inicio, estudiantes, profesores, cursos, entregables

urlpatterns = [
    path('', inicio, name="inicio"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('profesores/', profesores, name="profesores"),
    path('cursos/', cursos, name="cursos"),
    path('entregables/', entregables, name="entregables"),
    ]
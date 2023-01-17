from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse
from App_Coder.forms import *
from App_Coder.models import *

def inicio(request):
    return render(request=request, template_name='App_Coder/inicio.html')

def estudiantes(request):

      if request.method == 'POST':

            estudiantes_formulario_crear = EstudianteFormulario(request.POST)

            print(estudiantes_formulario_crear)

            if estudiantes_formulario_crear.is_valid:

                  informacion = estudiantes_formulario_crear.cleaned_data

                  estudiantes = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email']) 

                  estudiantes.save()

                  url_exitosa = reverse('inicio')
                  return redirect(url_exitosa)

      else: 

            estudiantes_formulario_crear= EstudianteFormulario()

      return render(request=request, template_name="App_Coder/estudiantes.html", context={"estudiantes_formulario_crear":estudiantes_formulario_crear})

def cursos(request):

      if request.method == 'POST':

            curso_formulario_crear = CursoFormulario(request.POST)

            print(curso_formulario_crear)

            if curso_formulario_crear.is_valid:

                  informacion = curso_formulario_crear.cleaned_data

                  curso = Curso(nombre=informacion['curso'], comision=informacion['comision']) 

                  curso.save()

                  url_exitosa = reverse('inicio')
                  return redirect(url_exitosa)

      else: 

            curso_formulario_crear= CursoFormulario() 

      return render(request=request, template_name="App_Coder/cursos.html", context={"curso_formulario_crear":curso_formulario_crear})

def profesores(request):
    
      if request.method == 'POST':

            profesor_formulario_crear = ProfesorFormulario(request.POST) 

            print(profesor_formulario_crear)

            if profesor_formulario_crear.is_valid:

                  informacion = profesor_formulario_crear.cleaned_data

                  profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  url_exitosa = reverse('inicio')
                  return redirect(url_exitosa)

      else: 

            profesor_formulario_crear=ProfesorFormulario()

      return render(request=request, template_name="App_Coder/profesores.html", context={"profesor_formulario_crear":profesor_formulario_crear})

def entregables(request):
    
      if request.method == 'POST':

            entregable_formulario_crear = EntregableFormulario(request.POST) 

            print(entregable_formulario_crear)

            if entregable_formulario_crear.is_valid:

                  informacion = entregable_formulario_crear.cleaned_data

                  entregable = Entregable(nombre=informacion['nombre'], esta_aprobado=informacion['esta_aprobado'], ) 

                  entregable.save()

                  url_exitosa = reverse('inicio')
                  return redirect(url_exitosa)

      else: 

            entregable_formulario_crear=EntregableFormulario() 

      return render(request=request, template_name="App_Coder/entregables.html", context={"entregable_formulario_crear":entregable_formulario_crear})

def buscar(request):

      if request.GET["comision"]:

            comision = request.GET['comision'] 
            cursos = Curso.objects.filter(comision__icontains=comision)

            return render(request, "App_Coder/inicio.html", {"cursos":cursos, "comision":comision})

      else: 
            respuesta = "No enviaste datos"
      return HttpResponse(respuesta)
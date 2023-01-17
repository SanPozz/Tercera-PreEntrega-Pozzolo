from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=200)
    comision = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
    email = forms.EmailField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=200)

class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    esta_aprobado = forms.BooleanField(initial=False)

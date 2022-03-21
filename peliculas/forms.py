from django import forms


choices = (
    ("1", "Acción"),
    ("2", "Ciencia Ficción"),
    ("3", "Comedia"),
    ("4", "Drama"),
    ("5", "Fantasía"),
    ("6", "Musical"),
    ("7", "Romance"),
    ("8", "Suspenso"),
    ("9", "Terror"),
    ("10", "Documental"),

)

class PeliculasFormulario(forms.Form):
    nombre = forms.CharField(max_length=35)
    director = forms.CharField(max_length=20)
    año = forms.IntegerField()
    genero = forms.ChoiceField(choices = choices)

class BusquedaPelicula(forms.Form):
    buscar_pelicula = forms.CharField(label='Buscar pelicula', max_length=20)




# class BusquedaCurso(forms.Form):
#     partial_curso = forms.CharField(label='Buscar curso', max_length=20)



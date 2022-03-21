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


class SeriesFormulario(forms.Form):
    nombre = forms.CharField(max_length=35)
    año = forms.IntegerField()
    temporadas = forms.IntegerField()
    genero = forms.ChoiceField(choices = choices)

class BusquedaSeries(forms.Form):
    buscar_serie = forms.CharField(label='Buscar serie', max_length=20)

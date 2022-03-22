from django import forms


choices = (
    ("1", "Aventuras"),
    ("2", "Ciencia Ficción"),
    ("3", "Policial"),
    ("4", "Terror y misterio"),
    ("5", "Romance"),
    ("6", "Mitología"),
    ("7", "Teatro"),
    ("8", "Cuentos"),
    ("9", "Histórico"),
    ("10", "Cocina"),
)


class LibrosFormulario(forms.Form):
    nombre = forms.CharField(max_length=35)
    autor = forms.CharField(max_length=35)
    publicacion = forms.IntegerField()
    genero = forms.ChoiceField(choices = choices)


class BusquedaLibros(forms.Form):
    buscar_libro = forms.CharField(label='Buscar libro', max_length=20)

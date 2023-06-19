from django.forms import (
    ModelForm
)
from .models import ModeloPublicacion

class FormularioPublicacion(ModelForm):
    class Meta:
        model = ModeloPublicacion
        fields = ['titulo','detalle']
        #widgets = {}
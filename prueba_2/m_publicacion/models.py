from django.db.models import (
    Model,
    CharField,
    TextField,
    DateField,
    ForeignKey,
    CASCADE
)
from django.contrib.auth.models import User
# Create your models here.
class ModeloPublicacion(Model):
    # Las id se generna solas XD
    titulo = CharField(max_length = 40, null = False, unique = True)
    detalle = TextField(max_length = 500, null = False)
    fecha_publicacion = DateField(auto_now = True)
    fecha_modificacion = DateField(null = True)
    usuario = ForeignKey(User, on_delete = CASCADE )

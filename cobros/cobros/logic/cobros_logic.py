from ..models import Cobro

def get_cobros(estudiante):
    cobros = estudiante.cobros.all()    
    return cobros


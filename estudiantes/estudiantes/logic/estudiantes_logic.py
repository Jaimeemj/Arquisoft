from ..models import Estudiante

def get_estudiantes():
    return Estudiante.objects.all()


def get_estudiante(estudiante_id):
    return Estudiante.objects.get(id=estudiante_id)


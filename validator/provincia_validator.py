from pydantic import ValidationError


class Validador_Provincia(ValidationError):
    def validar_nombre(cls, name):
        if len(name) < 7:
            raise ValueError("El nombre debe ser mas largo que siete digitos")
        return name

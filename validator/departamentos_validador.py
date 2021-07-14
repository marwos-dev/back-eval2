from pydantic import ValidationError


class ValidadorDepartamento(ValidationError):
    def validar_nombre(cls, name):  # noqa
        if len(name) < 7:
            raise ValueError("El nombre debe ser mas largo que siete digitos")
        return name

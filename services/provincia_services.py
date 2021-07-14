from repository.provicias_repository import ProvinciaRepository


class Provincias_Services:

    @classmethod
    def get_all(cls):
        return ProvinciaRepository.get_provincias()

    @classmethod
    def get_one(cls, id: int):
        return ProvinciaRepository.get_provincia(id)

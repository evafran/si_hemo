class TipoSangue:
    # construtor
    def __init__(self, tipo,quantidade):
        self.__tipo = tipo
        self.__quantidade= quantidade

    # getters e setters
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    # getters e setters
    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

class Doacao:
    # construtor
    def __init__(self, cod_agen,cod_func,data_hora):
        self.__cod_agen = cod_agen
        self.__cod_func= cod_func
        self.__data_hora = data_hora

    # getters e setters
    @property
    def cod_agen(self):
        return self.__cod_agen

    @cod_agen.setter
    def cod_agen(self, cod_agen):
        self.__cod_agen = cod_agen

    # getters e setters
    @property
    def cod_func(self):
        return self.__cod_func

    @cod_func.setter
    def cod_func(self, cod_func):
        self.__cod_func = cod_func


    # getters e setters
    @property
    def data_hora(self):
        return self.__data_hora

    @data_hora.setter
    def data_hora(self, data_hora):
        self.__data_hora = data_hora

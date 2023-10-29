class Agendamento:
    # construtor
    def __init__(self, cod_doador,data_hora):
        self.__cod_doador = cod_doador
        self.__data_hora = data_hora

        # getters e setters
    @property
    def cod_doador(self):
        return self.__cod_doador

    @cod_doador.setter
    def cod_doador(self, cod_doador):
        self.__cod_doador= cod_doador




    @property
    def data_hora(self):
        return self.__data_hora

    @data_hora.setter
    def data_hora(self, data_hora):
        self.__data_hora = data_hora



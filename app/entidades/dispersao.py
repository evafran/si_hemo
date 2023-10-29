class Dispersao:
    # construtor
    def __init__(self, cod_func,cod_hospital,cod_tiposang,qtd_bolsa, data):
        self.__cod_func = cod_func
        self.__cod_hospital= cod_hospital
        self.__cod_tiposang = cod_tiposang
        self.__qtd_bolsa = qtd_bolsa
        self.__data = data


        # getters e setters
    @property
    def cod_func(self):
        return self.__cod_func

    @cod_func.setter
    def cod_func(self, cod_func):
        self.__cod_func = cod_func

    @property
    def cod_hospital(self):
        return self.__cod_hospital

    @cod_hospital.setter
    def cod_hospital(self, cod_hospital):
        self.__cod_hospital = cod_hospital

    @property
    def cod_tiposang(self):
        return self.__cod_tiposang

    @cod_tiposang.setter
    def cod_tiposang(self, cod_tiposang):
        self.__cod_tiposang = cod_tiposang

    @property
    def qtd_bolsa(self):
        return self.__qtd_bolsa

    @qtd_bolsa.setter
    def qtd_bolsa(self, qtd_bolsa):
        self.__qtd_bolsa = qtd_bolsa

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
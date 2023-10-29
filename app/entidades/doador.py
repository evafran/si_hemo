class Doador:
    # construtor
    def __init__(self, nome,endereco,cpf,telefone, data_nascimento, peso,cod_tiposang):
        self.__nome = nome
        self.__endereco= endereco
        self.__cpf = cpf
        self.__telefone = telefone
        self.__data_nascimento = data_nascimento
        self.__peso = peso
        self.__cod_tiposang=cod_tiposang


        # getters e setters
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def cod_tiposang(self):
        return self.__cod_tiposang

    @cod_tiposang.setter
    def cod_tiposang(self, cod_tiposang):
        self.__cod_tiposang = cod_tiposang


# arquivo para poder criar um objeto do tipo Lembrete

class Lembrete:
    # construtor
    def __init__(self, titulo, descricao, data, prioridade, usuario):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data = data
        self.__prioridade = prioridade
        self.__usuario = usuario

    # getters e setters
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prioridade(self):
        return self.__prioridade

    @prioridade.setter
    def prioridade(self, prioridade):
        self.__prioridade = prioridade

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

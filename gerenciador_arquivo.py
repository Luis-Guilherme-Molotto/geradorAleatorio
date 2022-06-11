from typing import List
from os.path import exists as verificar_existe_arquivo


class GerenciadorArquivo:
    def __init__(self, nome_arquivo: str):
        self._nome_arquivo = nome_arquivo
        self._str_separador = "\n"

    def ler_numeros(self):
        try:
            arquivo = open(self._nome_arquivo, "r")
            conteudo = arquivo.read()
            arquivo.close()

            if conteudo:
                return self.__str_para_float_arr(conteudo)
            else:
                raise Exception("Arquivo nao possui conteudo para ser lido")

        except Exception as ex:
            getattr(ex, "message", repr(ex))

    def salvar_numeros(self, numeros: List[float]):
        try:
            existe_arquivo = verificar_existe_arquivo(self._nome_arquivo)
            arquivo = open(self._nome_arquivo, "w" if existe_arquivo else "x")
            arquivo.write(self.__stringify_numeros(numeros))
            arquivo.close()
        except:
            print("Nao foi possivel escrever no arquivo")

    def __stringify_numeros(self, vetor: List[float]):
        string = "".join(["%.12f" % numero + self._str_separador for numero in vetor])
        return string

    def __str_para_float_arr(self, string: str):
        str_arr = string.split(self._str_separador)
        str_arr.pop()
        return [float(numero) for numero in str_arr]

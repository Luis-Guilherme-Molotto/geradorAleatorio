from timeit import timeit
from os.path import exists as verificar_existe_arquivo
from typing import List

from gerador_aleatorio import GeradorAleatorio


def gerar_numeros_aleatorios():
    gerador = GeradorAleatorio()

    return gerador.exec(tamanho=6 * (10 ** 7))


def cronometrar_tempo() -> None:
    tempo = timeit(
        "gerar_numeros_aleatorios()",
        setup="from __main__ import gerar_numeros_aleatorios",
        number=1,
    )

    print("Tempo de execucao: " + str(tempo))


def escrever_arquivo(nome: str, text: str):
    try:
        existe_arquivo = verificar_existe_arquivo(nome)
        arquivo = open(nome, "w" if existe_arquivo else "x")
        arquivo.write(text)
        arquivo.close()
    except:
        print("Nao foi possivel escrever no arquivo")


def stringify_numeros(vetor: List[float], separador: str):
    string = "".join(["%.12f" % numero + separador for numero in vetor])

    return string


def main():
    # testar performance
    # cronometrar_tempo()

    # gerador 1
    # gerador_1 = GeradorAleatorio(multiplicador=16807, modulo=((2 ** 31) - 1))

    # gerador personalizado
    gerador_personalizado = GeradorAleatorio(
        multiplicador=8404997, modulo=((2 ** 35) - 1)
    )

    numeros_aleatorios = gerador_personalizado.exec(tamanho=6 * (10 ** 7))

    print("transformando numeros em string...")
    texto_arquivo = stringify_numeros(numeros_aleatorios, separador="\n")

    print("escrevendo no arquivo...")
    escrever_arquivo("GERALEO.txt", texto_arquivo)


if __name__ == "__main__":
    main()

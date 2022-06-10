from timeit import timeit

from gerador_aleatorio import GeradorAleatorio


def gerar_numeros_aleatorios():
    gerador = GeradorAleatorio(tamanho=6 * (10 ** 7))

    numeros_aleatorios = gerador.exec()

    return numeros_aleatorios


def testar_geracao() -> None:
    tempo = timeit(
        "gerar_numeros_aleatorios()",
        setup="from __main__ import gerar_numeros_aleatorios",
        number=1,
    )

    print("Tempo de execucao: " + str(tempo))


def main():
    gerador_1 = GeradorAleatorio(multiplicador=16807, modulo=((2 ** 31) - 1))
    print(gerador_1.exec())

    # testar performance
    # testar_geracao()


if __name__ == "__main__":
    main()

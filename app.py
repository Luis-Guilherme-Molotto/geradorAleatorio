from timeit import timeit

from gerador_aleatorio import GeradorAleatorio
from teste_uniformidade import TesteUniformidade
from gerenciador_arquivo import GerenciadorArquivo


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


def main():
    # testar performance
    # cronometrar_tempo()

    # gerador 1
    # gerador_1 = GeradorAleatorio(multiplicador=16807, modulo=((2 ** 31) - 1))

    # gerador personalizado
    gerador_personalizado = GeradorAleatorio(
        multiplicador=8404997, modulo=((2 ** 35) - 1)
    )

    gerenciador_arquivo = GerenciadorArquivo("GERALEO.txt")

    numeros_aleatorios = gerador_personalizado.exec(tamanho=10)

    gerenciador_arquivo.salvar_numeros(numeros_aleatorios)

    numeros_salvos = gerenciador_arquivo.ler_numeros()

    teste_uniformidade = TesteUniformidade(numeros_salvos, classes=10)
    teste_uniformidade.exec()


if __name__ == "__main__":
    main()

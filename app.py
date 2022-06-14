from timeit import timeit

from gerador_aleatorio import GeradorAleatorio
from gerenciador_arquivo import GerenciadorArquivo
from teste_uniformidade import TesteUniformidade
from teste_corrida import TesteCorrida
from teste_permutacoes import TestePermutacoes
from teste_intervalo import TesteIntervalo


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
        multiplicador=8404997, modulo=((2 ** 61) - 1)
    )
    gerenciador_arquivo = GerenciadorArquivo("GERALEO.txt")

    numeros_aleatorios = gerador_personalizado.exec(tamanho=60000000)
    gerenciador_arquivo.salvar_numeros(numeros_aleatorios)
    numeros_salvos = gerenciador_arquivo.ler_numeros()

    #print("calculando teste de uniformidade...")
    #teste_uniformidade = TesteUniformidade(classes=20)
    #teste_uniformidade.exec(numeros_salvos)

    #print("\ncalculando teste de corrida...")
    #teste_corrida = TesteCorrida()
    #teste_corrida.exec(numeros_salvos, tipo="asc")

    print("\ncalculando teste de intervalo...")
    teste_intervalo = TesteIntervalo()
    teste_intervalo.exec(numeros_salvos, 5)

    #print("\ncalculando teste de permutações...")
    #teste_permutacoes = TestePermutacoes()
    #teste_permutacoes.exec(numeros_salvos)


if __name__ == "__main__":
    main()

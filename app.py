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
    cronometrar_tempo()

    # gerador 1
    gerador_1 = GeradorAleatorio(multiplicador=16807, modulo=((2 ** 31) - 1), incremento=0, semente=2022)

    # gerador personalizado
    #gerador_personalizado = GeradorAleatorio(multiplicador=(8 * 5832719) + 3, modulo=((2 ** 61) - 1), incremento=13 ,semente=2019)
    gerenciador_arquivo = GerenciadorArquivo("GERALEO.txt")

    #numeros_aleatorios = gerador_personalizado.exec(60000000)
    numeros_aleatorios = gerador_1.exec(60000000)
    gerenciador_arquivo.salvar_numeros(numeros_aleatorios)
    numeros_salvos = gerenciador_arquivo.ler_numeros()

    print("*** Teste de uniformidade ***")
    teste_uniformidade = TesteUniformidade(classes=20)
    teste_uniformidade.exec(numeros_salvos)

    print("\n*** Teste da corrida ascendente ***")
    teste_corrida = TesteCorrida()
    teste_corrida.exec(numeros_salvos, tipo="asc")

    print("\n*** Teste da corrida descendente ***")
    teste_corrida = TesteCorrida()
    teste_corrida.exec(numeros_salvos, tipo="desc")

    print("\n*** Teste dos intervalos ***")
    teste_intervalo = TesteIntervalo()
    teste_intervalo.exec(numeros_salvos, 0)
    teste_intervalo.exec(numeros_salvos, 1)
    teste_intervalo.exec(numeros_salvos, 2)
    teste_intervalo.exec(numeros_salvos, 3)
    teste_intervalo.exec(numeros_salvos, 4)
    teste_intervalo.exec(numeros_salvos, 5)
    teste_intervalo.exec(numeros_salvos, 6)
    teste_intervalo.exec(numeros_salvos, 7)
    teste_intervalo.exec(numeros_salvos, 8)
    teste_intervalo.exec(numeros_salvos, 9)

    print("\n*** Teste das permutacoes ***")
    teste_permutacoes = TestePermutacoes()
    teste_permutacoes.exec(numeros_salvos)


if __name__ == "__main__":
    main()

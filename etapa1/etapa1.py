# Desempate: maior soma, depois menor inicio, depois menor fim.
import sys


def forca_bruta(v):
    melhor = (v[0], 0, 0)
    for i in range(len(v)):
        soma = 0
        for j in range(i, len(v)):
            soma += v[j]
            if soma > melhor[0]:
                melhor = (soma, i, j)
    return melhor


def divisao_conquista(v, lo=0, hi=None):
    if hi is None:
        hi = len(v) - 1
    if lo == hi:
        return (v[lo], lo, lo)
    meio = (lo + hi) // 2

    soma, esq, ini = 0, float("-inf"), meio
    for i in range(meio, lo - 1, -1):
        soma += v[i]
        if soma >= esq:
            esq, ini = soma, i
    soma, dir, fim = 0, float("-inf"), meio + 1
    for j in range(meio + 1, hi + 1):
        soma += v[j]
        if soma > dir:
            dir, fim = soma, j

    candidatos = [divisao_conquista(v, lo, meio), (esq + dir, ini, fim), divisao_conquista(v, meio + 1, hi)]
    return min(candidatos, key=lambda r: (-r[0], r[1], r[2]))


if __name__ == "__main__":
    dados = sys.stdin.read().split()
    v = [int(x) for x in dados[1:1 + int(dados[0])]]
    print(*divisao_conquista(v))

import sys
from math import sqrt

LIMIAR = 32


def forca_bruta(pts):
    melhor = (float("inf"), None, None)
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            d = (pts[i][0] - pts[j][0]) ** 2 + (pts[i][1] - pts[j][1]) ** 2
            if d < melhor[0]:
                melhor = (d, pts[i], pts[j])
    return melhor


def _rec(px, py, limiar):
    n = len(px)
    if n <= limiar:
        return forca_bruta(px)
    meio = n // 2
    x_meio = px[meio][0]
    esq = set(px[:meio])
    py_esq = [p for p in py if p in esq]
    py_dir = [p for p in py if p not in esq]
    melhor = min(_rec(px[:meio], py_esq, limiar), _rec(px[meio:], py_dir, limiar), key=lambda r: r[0])

    faixa = [p for p in py if (p[0] - x_meio) ** 2 < melhor[0]]
    for i in range(len(faixa)):
        for q in faixa[i + 1:i + 8]:
            d = (faixa[i][0] - q[0]) ** 2 + (faixa[i][1] - q[1]) ** 2
            if d < melhor[0]:
                melhor = (d, faixa[i], q)
    return melhor


def divisao_conquista(pts, limiar=LIMIAR):
    vistos = set()
    for p in pts:
        if p in vistos:
            return (0, p, p)
        vistos.add(p)
    return _rec(sorted(pts), sorted(pts, key=lambda p: p[1]), limiar)


if __name__ == "__main__":
    dados = sys.stdin.read().split()
    n = int(dados[0])
    pts = [(int(dados[1 + 2 * i]), int(dados[2 + 2 * i])) for i in range(n)]
    d, a, b = divisao_conquista(pts)
    print(sqrt(d), *a, *b)

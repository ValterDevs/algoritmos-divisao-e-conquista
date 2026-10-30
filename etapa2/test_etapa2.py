import json
import random
import unittest

from etapa2 import divisao_conquista, forca_bruta


def pontos(texto):
    n, *v = map(int, texto.split())
    return [(v[2 * i], v[2 * i + 1]) for i in range(n)]


class Testes(unittest.TestCase):
    def test_casos(self):
        for c in json.load(open("casos_etapa2.json", encoding="utf-8")):
            p = pontos(c["entrada"])
            for f in (forca_bruta, divisao_conquista, lambda q: divisao_conquista(q, limiar=1)):
                self.assertEqual(f(p)[0], c["d2"], c["nome"])

    def test_aleatorio(self):
        for _ in range(500):
            p = [(random.randint(-20, 20), random.randint(-20, 20)) for _ in range(random.randint(2, 60))]
            for limiar in (1, 2, 8):
                self.assertEqual(forca_bruta(p)[0], divisao_conquista(p, limiar)[0], (p, limiar))


unittest.main() if __name__ == "__main__" else None

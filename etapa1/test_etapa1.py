import json
import random
import unittest

from etapa1 import divisao_conquista, forca_bruta


class Testes(unittest.TestCase):
    def test_casos(self):
        for c in json.load(open("casos_etapa1.json", encoding="utf-8")):
            v = list(map(int, c["entrada"].split()[1:]))
            esperado = tuple(map(int, c["saida"].split()))
            self.assertEqual(forca_bruta(v), esperado, c["nome"])
            self.assertEqual(divisao_conquista(v), esperado, c["nome"])

    def test_aleatorio(self):
        for _ in range(3000):
            v = [random.randint(-3, 3) for _ in range(random.randint(1, 14))]
            self.assertEqual(forca_bruta(v), divisao_conquista(v), v)


unittest.main() if __name__ == "__main__" else None

# Divisão e Conquista

## Etapa 1: Subarranjo de Soma Máxima

Dado um vetor de inteiros, encontra o intervalo contínuo com a maior soma.

### Arquivos

- `etapa1/etapa1.py`: as duas implementações e o programa principal.
- `etapa1/casos_etapa1.json`: casos de teste com entradas e saídas esperadas.
- `etapa1/test_etapa1.py`: roda os casos e compara as duas implementações em vetores aleatórios.

### Como executar

Entrada: um inteiro `n` seguido de `n` inteiros. Saída: `soma inicio fim` (índices começando em 0).

PowerShell:

```powershell
"5`n-2 1 -3 4 5" | python etapa1/etapa1.py
```

Bash:

```bash
printf "5\n-2 1 -3 4 5" | python etapa1/etapa1.py
```

Saída esperada: `9 3 4`

Para rodar os testes:

```bash
cd etapa1
python -m unittest -v
```

### Como funciona

**Força bruta, O(n²).** Testa todos os intervalos. Para cada início `i`, vai aumentando o fim `j` e acumulando a soma, guardando a melhor encontrada.

**Divisão e conquista, O(n log n).** Divide o vetor ao meio e o melhor intervalo está em um destes três lugares:

1. Inteiramente na metade esquerda (resolvido recursivamente).
2. Inteiramente na metade direita (resolvido recursivamente).
3. Cruzando o meio. Soma-se o melhor trecho que termina no meio, indo para a esquerda, com o melhor trecho que começa logo depois do meio, indo para a direita. Isso custa O(n).

A resposta é o maior dos três. A recorrência é T(n) = 2T(n/2) + O(n).

### Regra de desempate

Quando há intervalos com a mesma soma, as duas implementações escolhem o mesmo: maior soma, depois menor índice de início, depois menor índice de fim.

### Casos de borda testados

- Só valores negativos: a resposta é o maior elemento, não zero.
- Vetor de tamanho 1.
- Empates entre intervalos com a mesma soma.
- Intervalo que cruza o meio do vetor.

## Etapa 2: Par de Pontos Mais Próximo

Arquivos em `etapa2/`: `etapa2.py`, `casos_etapa2.json`, `test_etapa2.py`.

Entrada: `n` seguido de `n` linhas `x y` (inteiros). Saída: `distancia x1 y1 x2 y2`.

```bash
printf "4\n0 0\n10 10\n4 5\n5 5" | python etapa2/etapa2.py
cd etapa2 && python -m unittest -v
```

Força bruta compara todos os pares (O(n²)). A divisão e conquista ordena os pontos por x e por y uma vez, divide pela mediana de x, resolve cada lado e confere a faixa de largura 2*delta, comparando cada ponto com os 7 seguintes na ordem de y (O(n log n)). Subproblemas com até `LIMIAR = 32` pontos usam força bruta; o valor foi escolhido por medição (ver relatório). As distâncias são comparadas ao quadrado, sem raiz.

## Etapa 3: Medições e relatório

- `medicoes.csv`: medições brutas.
- `relatorio.pdf`: relatório com recorrências, tabelas, gráficos, análise e limiar.

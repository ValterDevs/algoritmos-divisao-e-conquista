# Divisão e Conquista

## Etapa 1: Subarranjo de Soma Máxima

Dado um vetor de inteiros, encontra o intervalo contínuo com a maior soma.

### Arquivos

- `etapa1.py`: as duas implementações e o programa principal.
- `casos_etapa1.json`: casos de teste com entradas e saídas esperadas.
- `test_etapa1.py`: roda os casos e compara as duas implementações em vetores aleatórios.

### Como executar

Entrada: um inteiro `n` seguido de `n` inteiros. Saída: `soma inicio fim` (índices começando em 0).

PowerShell:

```powershell
"5`n-2 1 -3 4 5" | python etapa1.py
```

Bash:

```bash
printf "5\n-2 1 -3 4 5" | python etapa1.py
```

Saída esperada: `9 3 4`

Para rodar os testes:

```bash
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

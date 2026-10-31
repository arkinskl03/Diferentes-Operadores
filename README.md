# Diferentes Operações

Programa de console em Python que lê dois números inteiros e aplica sobre eles uma operação matemática escolhida pelo usuário: **média**, **diferença**, **produto** ou **divisão**.

## Como executar

Requisitos: Python 3.x instalado.

```bash
python Diferentes_Operacoes.py
```

## Exemplo de uso

```
Digite um número: 10
Digite outro número: 4

Operadores
1: Média
2: Diferença
3: Produto
4: Divisão
escolha um número entre 1 e 4: 3
40
```

## Como o código funciona

### 1. Entrada dos números

```python
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
```

`input()` sempre devolve texto (`str`). O `int()` converte esse texto em número inteiro, para que seja possível fazer cálculos.

### 2. Funções das operações

Cada operação é uma função que recebe dois parâmetros (`a` e `b`) e devolve o resultado:

| Função | O que faz | Fórmula |
|---|---|---|
| `media(a, b)` | Média aritmética | `(a + b) / 2` |
| `diferenca(a, b)` | Subtração | `a - b` |
| `produto(a, b)` | Multiplicação | `a * b` |
| `divisao(a, b)` | Divisão, com verificação de divisor zero | `a / b` |

Na `divisao`, se `b` for `0`, a função exibe uma mensagem de aviso em vez de tentar dividir (o que causaria o erro `ZeroDivisionError`).

### 3. Dicionário de operações

```python
operacoes = {
    1: media,
    2: diferenca,
    3: produto,
    4: divisao,
}
```

O dicionário associa cada número do menu à **função** correspondente. Repare que as funções são escritas **sem parênteses**: isso guarda a própria função (uma referência), sem executá-la. Esse padrão substitui uma cadeia de `if/elif` e facilita adicionar novas operações: basta criar a função e incluir uma nova linha no dicionário.

### 4. Menu e escolha

O programa imprime o menu e lê a opção escolhida:

```python
escolha = int(input('escolha um número entre 1 e 4: '))
```

### 5. Validação e execução

```python
if escolha not in [1, 2, 3, 4]:
    print('escolha um número válido')
else:
    resultado = operacoes.get(escolha)
    print(resultado(n1, n2))
```

- Se a escolha não estiver entre 1 e 4, exibe uma mensagem de erro.
- Caso contrário, `operacoes.get(escolha)` busca no dicionário a função correspondente e a guarda em `resultado`. Na linha seguinte, `resultado(n1, n2)` **chama** essa função com os dois números e o `print` mostra o valor retornado.

## Fluxo resumido

```
Lê n1 e n2 → mostra menu → lê escolha → escolha válida?
                                          ├─ não → mensagem de erro
                                          └─ sim → busca função no dicionário → executa com (n1, n2) → imprime resultado
```

## Limitações conhecidas

- **Divisão por zero:** a função `divisao` imprime a mensagem e não retorna nada (`None`). Por isso, depois do aviso, o programa também imprime `None` na tela. Além disso, a mensagem diz "maior que 0", mas o problema é o divisor ser exatamente `0`.
- **Entrada não numérica:** se o usuário digitar letras, o `int()` lança `ValueError` e o programa encerra com erro.
- **Somente inteiros:** números decimais (como `2.5`) não são aceitos por causa do `int()`.
- **Nome da variável `resultado`:** ela guarda a *função*, e não o resultado do cálculo, o que pode confundir a leitura.

## Ideias de melhoria

- Usar `float()` no lugar de `int()` para aceitar decimais.
- Tratar erros de entrada com `try/except`.
- Fazer `divisao` retornar uma mensagem (ou levantar uma exceção) em vez de usar `print` dentro da função.
- Colocar o menu em um laço (`while`) para permitir várias operações sem reiniciar o programa.
- Gerar o menu automaticamente a partir do dicionário.

# Review: LeetCode 228 — Summary Ranges

## O que o problema pede

Dada uma lista de inteiros ordenados e únicos, agrupar números consecutivos em intervalos e retornar uma lista de strings no formato `"a->b"` (se `a != b`) ou `"a"` (se o número está sozinho).

**Exemplo:**
```
[0, 1, 2, 4, 5, 7] → ["0->2", "4->5", "7"]
```

---

## Como pensar no problema antes de codar

Antes de escrever qualquer código, vale responder três perguntas:

1. O que define o início de um grupo? → O primeiro número, ou o número após uma quebra.
2. O que define o fim de um grupo? → O número antes de uma quebra, ou o último número da lista.
3. Quando dois números são consecutivos? → Quando `nums[i+1] == nums[i] + 1`.

---

## Casos especiais — identifique antes de codar

**Lista vazia:** `nums = []` → retorne `[]`. Se não verificar isso, `nums[0]` vai dar erro.

**Número sozinho:** `[7]` ou um número sem vizinhos consecutivos → string é `"7"`, não `"7->7"`. Precisa de verificação antes de montar a string.

**Último grupo:** o loop para antes do último elemento (por causa do `nums[i+1]`), então o último grupo nunca é adicionado dentro do loop. Precisa ser tratado fora.

---

## Por que `range(len(nums) - 1)` e não `range(len(nums))`?

Dentro do loop você acessa `nums[i+1]`. Se o loop chegasse ao último índice, `nums[i+1]` não existiria e daria `IndexError`.

Por isso o loop vai até o **penúltimo** índice — o `- 1` no range evita esse erro.

```python
for i in range(len(nums) - 1):  # i vai de 0 até len-2
    nums[i+1]  # sempre existe porque i nunca é o último
```

---

## `for i in nums` vs `for i in range(len(nums))` — a diferença real

Esse foi um ponto de confusão importante. A distinção:

```python
nums = [0, 2, 3, 4, 6, 8, 9]

for i in nums:              # i assume os VALORES: 0, 2, 3, 4, 6, 8, 9
for i in range(len(nums)):  # i assume os ÍNDICES: 0, 1, 2, 3, 4, 5, 6
```

**Quando usar qual:**
- Precisa só do valor → `for num in nums`
- Precisa do índice (ex: acessar `nums[i+1]`) → `for i in range(len(nums))`

O problema aqui exige comparar `nums[i]` com `nums[i+1]`, então você **precisa do índice**.

---

## Por que algumas variáveis ficam fora do loop?

Regra simples: se o valor precisa persistir entre iterações (ser lido ou modificado em voltas diferentes do loop), fica fora.

- `start` precisa lembrar onde o grupo começou — é atualizado quando um grupo termina e precisa sobreviver até a próxima quebra.
- `result` precisa acumular todos os grupos — se estivesse dentro, seria resetada a cada volta.

---

## O código explicado linha por linha

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        # Caso especial: lista vazia. nums[0] daria erro sem isso.
        if not nums:
            return []

        # Marca o início do primeiro grupo.
        start = nums[0]

        # Lista que vai acumular as strings de resultado.
        result = []

        # Percorre até o penúltimo índice para poder acessar nums[i+1].
        for i in range(len(nums) - 1):

            # Se o próximo número NÃO é consecutivo, o grupo terminou aqui.
            if nums[i + 1] != nums[i] + 1:

                # Verifica se o grupo tem só um número ou é um range.
                if start == nums[i]:
                    result.append(f"{nums[i]}")          # Ex: "7"
                else:
                    result.append(f"{start}->{nums[i]}") # Ex: "0->2"

                # O próximo grupo começa no elemento seguinte.
                start = nums[i + 1]

        # O último grupo nunca é fechado dentro do loop — trata aqui.
        if start == nums[-1]:
            result.append(f"{nums[-1]}")          # Número sozinho
        else:
            result.append(f"{start}->{nums[-1]}") # Range até o fim

        return result
```

---

## Passeio mental pelo Example 1

`nums = [0, 1, 2, 4, 5, 7]`, `start = 0`

| i | nums[i] | nums[i+1] | Consecutivo? | Ação |
|---|---------|-----------|--------------|------|
| 0 | 0 | 1 | Sim | nada |
| 1 | 1 | 2 | Sim | nada |
| 2 | 2 | 4 | Não | adiciona `"0->2"`, `start = 4` |
| 3 | 4 | 5 | Sim | nada |
| 4 | 5 | 7 | Não | adiciona `"4->5"`, `start = 7` |

Fora do loop: `start == nums[-1]` (7 == 7) → adiciona `"7"`.

Resultado: `["0->2", "4->5", "7"]` ✓

---

## Lacunas identificadas durante a sessão

- **`range`**: Confusão entre percorrer valores e percorrer índices. Ver seção acima.
- **Variáveis dentro vs fora do loop**: A regra de "persistência entre iterações" resolve essa dúvida.
- **Consistência de nomes**: Trocar nomes de variáveis no meio do código causa erros difíceis de rastrear. Escolha um nome e mantenha.
- **`return` dentro do loop**: Encerra a função imediatamente na primeira iteração. `return` deve ficar fora, ao final da função.
- **f-string**: `f"{variavel}"` — o `f` fica fora das aspas. `"f{x}"` é uma string literal, não f-string.

---

## O que o Copilot apontou — contextualizado

**Overflow em grandes números:** Em Python não é problema (inteiros ilimitados), mas em Java ou C++ quebraria com 100 dígitos. Vale saber para outras linguagens.

**Complexidade:** Essa solução é O(n) em tempo, que é o ideal para esse problema. Não há como fazer melhor que uma passagem pela lista.

**Zeros à esquerda:** O enunciado garante que não existem, então não é um problema aqui. Em outros problemas pode ser.
---
name: review-tema
# TODO: renomeie a pasta e o name: review-security, review-correctness, review-performance, review-money ou pr-summary
description: >
  TODO (passo 3): O QUE a skill faz + QUANDO usar, com as palavras do usuário + o que NÃO faz.
  Exemplo para review-money: "Revisa código Python que mexe com dinheiro (valores, reembolsos,
  ledger) procurando float em quantia, arredondamento, soma de reembolso maior que o pago e
  débito sem transação. Use quando o usuário pedir review de pagamento, reembolso, ledger ou
  'confere o dinheiro'. Não cobre segurança nem desempenho: para isso existem review-security
  e review-performance."
license: Apache-2.0
compatibility: Requer git e python3.
metadata:
  author: TODO-equipe
  version: "0.1"
---

# review-tema

<!-- Passo 1 (tarefa) e passo 2 (gotchas) acontecem ANTES de abrir este arquivo:
     revise o projeto vizinho à mão, com o agente e sem skill, e anote cada correção que
     você deu ao modelo. Cada correção vira uma linha de "Gotchas". -->

## Quando NÃO usar

- TODO: dois ou três pedidos parecidos que não são este review (ex.: "escreve o teste", "explica o diff", "revisa a segurança" se esta é a de dinheiro).

## Gotchas (o que o modelo errou à mão)

<!-- Passo 2. Uma linha por correção. Cada linha precisa ser verificável na spec (R01 a R12)
     ou no design.md do projeto. "Genérico" vale 1 na rubrica; "do projeto" vale 2. -->
- TODO: ex. `Decimal` ou `float` em quantia viola R01 (centavos `int`).
- TODO
- TODO

## Procedimento

1. Leia só o que o tema pede: TODO (ex.: `money.py`, `refunds.py`, `ledger.py` e os testes `test_r01`, `test_r04`, `test_r12`).
2. Para cada gotcha acima, procure a violação. Achado sem **arquivo e linha** não entra.
3. Marque o requisito da spec que o achado viola (`R__`). Se não há requisito, é "fora da spec" e vale menos.
4. Rode `scripts/TODO` para a parte repetível (ex.: grep de `float(` em `app/`). O que é determinístico não fica no modelo.
5. Escreva o relatório no template abaixo.

## Template de saída (obrigatório)

```
| # | Arquivo | Linha | Requisito | Severidade | Evidência | Sugestão |
|---|---|---|---|---|---|---|
| 1 | app/refunds.py | 31 | R04 | alto | `total + valor > pago` sem `>=` | usar `>` conforme R04 |
```

## Validation loop

1. Rode `python validate.py <esta pasta>` (frontmatter).
2. Rode os 5 prompts de `evals/evals.json` em sessão nova: os 3 positivos têm de disparar, os 2 near-misses não.
3. Rode a skill no projeto vizinho e compare com a sua revisão à mão: o que a skill deixou passar vira gotcha novo.

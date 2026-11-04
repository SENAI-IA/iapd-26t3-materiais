---
name: review-tema
# TODO: renomeie a pasta e o name para o tema sorteado: review-security, review-correctness ou review-performance
description: >
  TODO (passo 3): O QUE a skill faz + QUANDO usar, com as palavras do usuário + o que NÃO faz.
  Exemplo para review-security: "Revisa código Python procurando injeção (SQL, comando, caminho),
  autenticação fraca, segredo exposto ou com valor padrão e dado sensível em log. Use quando o usuário
  pedir review de segurança, 'tem falha nisso?', auditoria ou antes de expor um endpoint. Não cobre
  lógica nem desempenho: para isso existem review-correctness e review-performance."
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
- TODO: ex. comparar assinatura com `==` viola R08 (`compare_digest`).
- TODO
- TODO

## Procedimento

1. Leia só o que o tema pede: TODO (ex.: para security, tudo que recebe entrada externa: query, token, header, log).
2. Para cada gotcha acima, procure a violação. Achado sem **arquivo e linha** não entra.
3. Marque o requisito da spec que o achado viola (`R__`). Se não há requisito, é "fora da spec" e vale menos.
4. Rode `scripts/TODO` para a parte repetível (ex.: grep de `float(` em `app/`). O que é determinístico não fica no modelo.
5. Escreva o relatório no template abaixo.

## Template de saída (obrigatório)

```
| # | Arquivo | Linha | Requisito | Severidade | Evidência | Sugestão |
|---|---|---|---|---|---|---|
| 1 | app/db.py | 6 | R09 | crítico | `f"... WHERE id = '{x}'"` | placeholder `?` |
```

## Validation loop

1. Rode `python validate.py <esta pasta>` (frontmatter).
2. Rode os 5 prompts de `evals/evals.json` em sessão nova: os 3 positivos têm de disparar, os 2 near-misses não.
3. Rode a skill nos 4 casos públicos de `casos/<tema>/`: tem de achar os 3 bugs na linha certa e não inventar nada no caso limpo. O que deixou passar vira gotcha novo.

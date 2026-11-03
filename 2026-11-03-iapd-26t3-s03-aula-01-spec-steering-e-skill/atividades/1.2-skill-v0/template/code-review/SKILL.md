---
name: code-review
# TODO: renomeie a pasta e o name para code-review-<grupo> (minúsculas, números e hífens, até 64 caracteres)
description: >
  TODO: diga O QUE a skill faz e QUANDO usar, com as palavras que o usuário usaria.
  Exemplo: "Revisa diffs e PRs em Python procurando bugs de correção, segurança e desempenho e
  devolve achados com arquivo, linha, severidade e evidência. Use quando o usuário pedir review,
  revisão, 'olha esse PR', 'revisa esse repositório' ou antes de um merge."
license: Apache-2.0
compatibility: Requer git e python3. TODO: ajuste se usar outra ferramenta.
metadata:
  author: TODO-grupo
  version: "0.1"
---

# Code review: pagamentos-api

<!-- Este template é o ponto de partida da Atividade 1.2. Preencha os TODOs, apague os comentários
     e valide com: python validate.py .kiro/skills/code-review-<grupo> -->

## Quando NÃO usar

<!-- TODO: liste 2 ou 3 pedidos parecidos que NÃO são code review (ex.: escrever testes, explicar um diff, fazer deploy). Isso reduz disparo errado. -->

## Gotchas do repositório (o que o modelo não sabe sozinho)

<!-- TODO: copie do README do repo as convenções que, violadas, são bug. Comece por estas e complete: -->
- Dinheiro é `int` em centavos; qualquer `float` em quantia é bug.
- sqlite3 puro com placeholders `?`; SQL formatado por f-string ou `%` é bug.
- Segredos comparados com `compare_digest`; `==` em token é bug.
- TODO: timestamps
- TODO: idempotência de webhooks
- TODO: débito atômico

## Categorias e severidades

<!-- TODO: defina o que cada categoria cobre e o que faz um achado ser crítico/alto/médio/baixo.
     Use exatamente estes nomes, porque o score.py compara com eles. -->

| Categoria | Cobre |
|---|---|
| correção | TODO |
| segurança | TODO |
| desempenho | TODO |
| dados/dinheiro | TODO |
| concorrência | TODO |
| manutenibilidade | TODO |

| Severidade | Critério |
|---|---|
| crítico | TODO (ex.: perda de dinheiro, acesso indevido, corrupção de dados) |
| alto | TODO |
| médio | TODO |
| baixo | TODO |

## Procedimento

1. Rode `scripts/collect_diff.sh <base> <head>` para obter o diff e a mensagem de commit. Se o pedido for o repositório inteiro, leia `app/` arquivo por arquivo, na ordem: money, db, auth, payments, refunds, ledger, webhooks, api.
2. TODO: descreva como revisar (por categoria? por arquivo? com checklist?).
3. Todo achado precisa de **arquivo, linha e evidência** (trecho de código). Achado sem linha não entra no relatório.
4. Antes de incluir um achado, pergunte: "há evidência na linha citada?" Se a resposta depender de suposição sobre outro arquivo, confira o outro arquivo antes.
5. Escreva o relatório em `reports/<grupo>-v0.md` usando o template abaixo.

## Formato do achado (template de saída, obrigatório)

```
| # | Arquivo | Linha | Severidade | Categoria | Evidência | Sugestão |
|---|---|---|---|---|---|---|
| 1 | app/x.py | 42 | alto | segurança | `trecho` | correção em uma frase |
```

## Validation loop

1. Rode `python scripts/validate_report.py reports/<grupo>-v0.md`.
2. Se falhar, corrija os achados apontados e rode de novo. Repita até "OK".
3. Só então entregue. O `score.py` é rodado pelo professor com o gabarito.

## Por que esse formato

<!-- TODO: uma frase sua. Dica: o que um achado vago custa para quem vai corrigir? -->

---
name: review-correctness
description: >
  Revisão de correção lógica de código Python: off-by-one, condições invertidas, estados
  inconsistentes, idempotência quebrada, datas sem fuso, exceções engolidas, regras de negócio
  violadas (dinheiro, reembolso, saldo). Devolve achados com arquivo, linha, severidade e evidência.
  Use quando o usuário pedir "revisa a lógica", "tem bug aqui", "esse cálculo está certo",
  "revisa esse PR" sem especificar segurança ou desempenho. Não use para vulnerabilidades,
  desempenho ou estilo.
license: Apache-2.0
compatibility: Requer git e python3.
metadata:
  author: turma-sd
  version: "1.0"
  suite: review
---

# Revisão de correção

## Gotchas do repositório

- Dinheiro é `int` em centavos. `float` em quantia, `round()` em float ou `int()` truncando resultado são bugs de **dados/dinheiro**.
- Paginação é 1-based: `page=1` devolve os primeiros registros. Confira o cálculo do `offset`.
- Timestamps são `datetime.now(timezone.utc)`. `datetime.now()` sozinho é bug.
- Webhooks são idempotentes por `event_id`. Processar duas vezes é bug de correção.
- Reembolsos acumulados nunca passam do valor capturado.
- Débito é atômico (um `UPDATE ... WHERE balance_cents >= ?`). Ler e escrever em dois passos é bug de **concorrência**.
- Erros são exceções tipadas. `except Exception: return None` é bug de **manutenibilidade**.

## Procedimento

1. Leia o módulo inteiro antes de apontar qualquer coisa: muitos bugs de correção são "a função X existe e não é chamada" (ex.: `mask_pan`, `_already_seen`, `total_refunded`).
2. Para cada função pública, pergunte: entrada inválida é rejeitada? Caso de borda (0, negativo, vazio, duplicado) é tratado? O estado final é consistente se a função falhar no meio?
3. Compare o docstring e o README com o código. Divergência entre o que o comentário promete e o que o código faz é achado.
4. Categoria: `correção` por padrão; `dados/dinheiro` quando envolve quantia ou arredondamento; `concorrência` quando envolve ordem de operações; `manutenibilidade` quando é erro de API (None em vez de exceção, exceção engolida).
5. Severidade: **crítico** = perda ou criação de dinheiro, corrupção de dado; **alto** = comportamento errado visível ao usuário em caminho comum; **médio** = erro em caminho menos comum; **baixo** = fragilidade sem efeito imediato.

## Formato de saída

```
| # | Arquivo | Linha | Severidade | Categoria | Evidência | Sugestão |
```

Toda evidência cita o trecho de código. "Parece errado" não é evidência.

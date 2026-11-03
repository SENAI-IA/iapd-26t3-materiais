# Relatório de code review: pagamentos-api

Grupo: exemplo
Rodada: v0
Branch revisada: main
Skill(s) usada(s): code-review-exemplo (monolítica)

## Resumo

Revisão completa de `app/`. 8 achados, sendo 2 críticos. Os módulos de dinheiro e ledger
concentram os problemas mais graves. Dois achados são de estilo e podem ser falsos positivos.

## Achados

| # | Arquivo | Linha | Severidade | Categoria | Evidência | Sugestão |
|---|---|---|---|---|---|---|
| 1 | app/db.py | 56 | crítico | segurança | `f"SELECT * FROM payments WHERE customer_id = '{customer_id}'"` interpola entrada do usuário | usar placeholder `?` com tupla de parâmetros |
| 2 | app/auth.py | 18 | alto | segurança | `return provided == expected` compara token com `==` | `secrets.compare_digest` |
| 3 | app/money.py | 13 | crítico | dados/dinheiro | `int(float(value) * 100)`: `float("0.29") * 100` dá 28.999... | usar `Decimal` com `quantize` |
| 4 | app/payments.py | 37 | alto | segurança | `card_pan` completo vai para `log.info`; `mask_pan` existe e não é usada | logar `mask_pan(card_pan)` |
| 5 | app/webhooks.py | 33 | alto | correção | `INSERT OR REPLACE` aceita o mesmo `event_id` de novo; `_already_seen` nunca é chamada | checar `_already_seen` e devolver `duplicate` |
| 6 | app/api.py | 20 | médio | segurança | `headers.get("Authorization", "")` aceita header vazio sem logar tentativa | registrar tentativas de acesso não autorizado |
| 7 | app/ledger.py | 25 | baixo | manutenibilidade | `balance` levanta `KeyError` em vez de exceção do domínio | criar `AccountNotFound` |
| 8 | app/refunds.py | 14 | baixo | desempenho | `total_refunded` roda um `SUM` a cada reembolso | manter coluna `refunded_cents` em payments |

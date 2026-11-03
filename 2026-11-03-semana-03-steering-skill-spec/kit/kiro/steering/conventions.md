---
inclusion: always
---
# Convenções da pagamentos-api

- Dinheiro é int em centavos; nunca float.
- sqlite3 puro com placeholders `?`; nunca formatar SQL.
- Segredos só do ambiente e comparados com compare_digest.
- Timestamps em UTC com tzinfo.
- Webhooks idempotentes por event_id; débito em um único UPDATE condicional.
- Nunca logar PAN ou token. Erros são exceções tipadas.
- Relatórios de review seguem reports/TEMPLATE.md e passam em scripts/validate_report.py.

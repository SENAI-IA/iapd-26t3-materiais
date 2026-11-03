---
name: review-performance
description: >
  Revisão de desempenho de código Python com banco de dados: consultas N+1, falta de índice,
  consultas dentro de loop, carregamento de tudo em memória, falta de paginação, algoritmos
  quadráticos. Devolve achados com arquivo, linha, severidade, evidência e estimativa de impacto.
  Use quando o usuário pedir "revisão de performance", "isso escala", "está lento", "otimiza as
  queries" ou "tem N+1 aqui". Não use para segurança, correção ou estilo.
license: Apache-2.0
compatibility: Requer python3; para medir, sqlite3 da biblioteca padrão.
metadata:
  author: turma-sd
  version: "1.0"
  suite: review
---

# Revisão de desempenho

## Gotchas do repositório

- sqlite3 em arquivo único: cada `execute` é um round-trip barato localmente, mas o padrão N+1 vira o gargalo quando o banco muda para rede.
- O schema está em `app/db.py` (`SCHEMA`). Toda coluna usada em `WHERE` de consulta frequente precisa de índice.
- Consultas em lote usam `IN (...)` com placeholders gerados. Loop com uma consulta por item é achado.

## Procedimento

1. Leia `app/db.py` primeiro e anote as colunas filtradas em `WHERE`; compare com os `CREATE INDEX`.
2. Procure `for ... in ...:` que contenha `conn.execute` ou chamada a função que executa consulta. Cada ocorrência é candidato a N+1.
3. Procure `fetchall()` sem `LIMIT` em tabelas que crescem (payments, ledger_entries).
4. Para cada achado, estime o impacto em uma frase com número: "com 10 mil contas são 20 mil consultas".
5. Severidade: **alto** = N+1 ou full scan em caminho quente; **médio** = falta de paginação ou carga em memória; **baixo** = índice ausente em consulta rara, micro-otimização.
6. Não aponte micro-otimização de CPU (list comprehension vs loop) a menos que o usuário peça.

## Formato de saída

```
| # | Arquivo | Linha | Severidade | Categoria | Evidência | Sugestão |
```

Categoria é sempre `desempenho`. A evidência inclui o loop ou a consulta e o número estimado.

## Por que estimar com número

Pereira et al. (2026) mostram que agentes que "acham tudo" têm sinal/ruído baixo. Um achado de desempenho sem ordem de grandeza é ruído: o revisor humano não sabe se vale corrigir agora.

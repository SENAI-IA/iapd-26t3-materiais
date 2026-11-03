---
name: git-commit-msg
description: >
  Escreve mensagens de commit no padrão Conventional Commits a partir do diff staged: tipo,
  escopo, resumo até 72 caracteres e corpo explicando o porquê. Use quando o usuário pedir
  "escreve o commit", "mensagem de commit", "commit message" ou rodar git commit sem mensagem.
  Não faz o commit; só escreve a mensagem.
license: Apache-2.0
compatibility: Requer git.
metadata:
  author: turma-sd
  version: "1.0"
---

# Mensagem de commit

## Procedimento

1. Rode `git diff --staged --stat` e `git diff --staged`. Se não houver nada staged, diga isso e pare.
2. Escolha o tipo: feat, fix, refactor, perf, test, docs, chore. Um commit, um tipo. Se o diff mistura tipos, sugira dividir.
3. Escopo = módulo mais afetado (ex.: `payments`, `ledger`).
4. Resumo no imperativo, até 72 caracteres, sem ponto final.
5. Corpo: por que a mudança foi feita e o que ela NÃO faz, se isso evitar confusão. Não descreva o diff linha a linha.

## Formato

```
<tipo>(<escopo>): <resumo>

<corpo em 1 a 4 linhas>
```

## Gotchas

- "Refatorações diversas" não é mensagem de commit. Se não dá para dizer o que mudou em 72 caracteres, o commit é grande demais.
- Não invente issue number. Só referencie se estiver no diff ou no pedido.

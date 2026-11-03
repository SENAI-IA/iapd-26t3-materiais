---
name: pr-summary
description: >
  Escreve o resumo de um pull request a partir do diff e das mensagens de commit: o que mudou,
  por quê, como testar e riscos. Não aponta bugs. Use quando o usuário pedir "resume esse PR",
  "escreve a descrição do PR", "o que esse diff faz", "explica essas mudanças". Não use para
  revisar código ou encontrar problemas.
license: Apache-2.0
compatibility: Requer git.
metadata:
  author: turma-sd
  version: "1.0"
  suite: review
---

# Resumo de PR

## Procedimento

1. Rode `scripts/collect_diff.sh <base> <head>` (está no repositório) e leia a mensagem de commit antes do diff.
2. Agrupe as mudanças por intenção, não por arquivo: "muda o cálculo de taxa" em vez de "altera money.py".
3. Para cada grupo, uma linha: o que mudou e por quê (se o porquê não estiver no commit, escreva "motivo não informado").
4. Liste como testar: comandos e o resultado esperado.
5. Liste riscos: o que pode quebrar e onde olhar. Riscos são hipóteses, não achados; não dê linha nem severidade.

## Formato de saída

```
## O que muda
- ...

## Por quê
- ...

## Como testar
- `pytest -q` deve passar
- ...

## Riscos e pontos de atenção
- ...
```

Até 15 linhas no total. Um PR que precisa de mais que isso deveria ser dois PRs; diga isso ao autor.

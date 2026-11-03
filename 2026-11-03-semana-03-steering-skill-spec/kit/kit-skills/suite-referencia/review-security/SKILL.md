---
name: review-security
description: >
  Revisão de segurança de código Python: injeção de SQL e comando, segredos hardcoded, comparação
  de tokens em tempo variável, vazamento de dados sensíveis em log, autenticação e autorização
  ausentes, desserialização perigosa. Devolve achados com arquivo, linha, CWE, severidade e evidência.
  Use quando o usuário pedir "revisão de segurança", "security review", "tem alguma vulnerabilidade",
  "esse código é seguro" ou "checa OWASP/CWE". Não use para bugs de lógica, desempenho ou estilo.
license: Apache-2.0
compatibility: Requer git e python3. Portável entre Kiro, Claude Code, Codex e Gemini CLI.
metadata:
  author: turma-sd
  version: "1.0"
  suite: review
---

# Revisão de segurança

## Gotchas do repositório

- sqlite3 puro: todo SQL usa placeholders `?`. f-string, `%`, `.format` ou `+` em SQL é CWE-89, mesmo que a variável "venha de dentro".
- Segredos comparados com `secrets.compare_digest` ou `hmac.compare_digest`. `==` é CWE-208.
- Segredos vêm só do ambiente. `os.environ.get("X", "valor")` com default é CWE-798.
- PAN completo, CVV, token e segredo nunca vão para log. Existe `mask_pan`; se não é usada no log, é CWE-532.
- Função que devolve `None` em caso de erro e é consumida com `payment["campo"]` é CWE-476.

## Procedimento

1. Obtenha o material: `scripts/collect_diff.sh <base> <head>` devolve mensagem de commit + diff. A mensagem de commit importa: "simplificações" e "ajustes de dev" costumam esconder remoção de validação. Se o pedido for o repo inteiro, leia `app/auth.py`, `app/db.py`, `app/payments.py`, `app/webhooks.py` e `app/api.py`, nessa ordem.
2. Abra `references/cwe-top25.md` e percorra a coluna "O que procurar". Para cada item aplicável, procure o padrão no código. Não invente categorias fora da lista.
3. Para cada achado: arquivo, linha, CWE, severidade, evidência (o trecho), sugestão.
4. Severidade: **crítico** = acesso indevido, forjar requisição, injeção, segredo exposto; **alto** = vazamento de dado sensível, timing attack; **médio** = validação ausente sem exploração direta; **baixo** = defesa em profundidade.
5. Antes de incluir um achado, confirme: "há evidência na linha citada?" Se a evidência depende de outro arquivo, cite os dois.

## Formato de saída

```
| # | Arquivo | Linha | Severidade | Categoria | Evidência | Sugestão |
|---|---|---|---|---|---|---|
| 1 | app/db.py | 56 | crítico | segurança | `f"... WHERE customer_id = '{customer_id}'"` (CWE-89) | placeholder `?` |
```

A categoria é sempre `segurança`. O CWE vai dentro da evidência.

## Por que a lista de CWEs

Yu et al. (2024) mediram 7 LLMs em revisão de segurança: o melhor prompt incluía a lista de CWEs e a mensagem de commit. Sem a lista, o modelo acha o óbvio (SQLi) e esquece timing attack, log de PAN e default de segredo.

# Ficha de teste: a skill da adversária (Fase 2, 25 min)

Equipe testadora: ____________   Equipe criadora: ____________   Skill: review-__________

Regras: SKILL.md intocado; sessão nova a cada rodada; o pedido é feito uma vez e a primeira resposta vale; achado sem arquivo e linha não casa com nada.

## 0. Instalar (3 min)

Clone o repo da criadora, copie a pasta da skill para a pasta de skills da sua ferramenta. Clone `iapd-26t3-pagamentos-api`.

## 1. Branch `main` (8 min)

`git checkout main`. Sessão nova. Pedido usado (escreva exatamente): ______________________________

A skill disparou? ___   Salve a resposta em `reports/<tema>-<criadora>-main.md` no formato:

```
| # | Arquivo | Linha | Severidade | Categoria | Evidência | Sugestão |
|---|---|---|---|---|---|---|
```

Rode `python scripts/validate_report.py reports/<tema>-<criadora>-main.md` (do pagamentos-api) e corrija só o FORMATO, nunca o conteúdo.

## 2. Branch `clean` (6 min)

`git checkout clean`. Sessão nova. Mesmo pedido. Salve em `reports/<tema>-<criadora>-clean.md`. Achados aqui: ___ (cada um é -2).

## 3. Gatilho (6 min)

Escreva 5 prompts SEUS, rode cada um em sessão nova e anote o que carregou.

| # | Prompt | Esperado | Disparou? | Ponto |
|---|---|---|---|---|
| 1 | | dispara | | |
| 2 | | dispara | | |
| 3 | | dispara | | |
| 4 | | não dispara (near-miss) | | |
| 5 | | não dispara (near-miss) | | |

Salve esta tabela em `reports/<tema>-<criadora>-gatilho.md`.

## 4. Pontuar e entregar (2 min)

Com o `gabarito.json` liberado no chat às 20h55:

```
python scripts/score_duelo.py --tema <tema> reports/<tema>-<criadora>-main.md reports/<tema>-<criadora>-clean.md gabarito.json --gatilho <acertos de 0 a 5>
```

PR no repo da criadora com os 3 arquivos e a saída do script colada na descrição, até 21h20. Título: `S03 Aula 02: teste de review-<tema> por <equipe testadora>`.

A criadora aprova ou contesta citando bug e linha. A auditora (equipe de outro tema) roda o script de novo e assina. Pontos finais: ______ (assinam testadora, criadora e auditora).

## Comentário (3 linhas, opcional): o que a skill faria melhor com uma mudança só

____________________________________________________________________

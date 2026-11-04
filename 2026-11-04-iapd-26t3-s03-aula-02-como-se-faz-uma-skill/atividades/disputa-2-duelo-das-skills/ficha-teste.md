# Ficha de teste: a skill da adversária (Fase 2, 25 min)

Equipe testadora: ____________   Equipe criadora: ____________   Skill: review-__________

Regras: SKILL.md intocado; sessão nova a cada caso; o pedido é feito uma vez e a primeira resposta vale; achado sem arquivo e linha não conta.

## 0. Instalar (3 min)

Clone o repo da criadora, copie a pasta da skill para a pasta de skills da sua ferramenta. Abra `casos/<tema>/README.md` para ver o que cada caso espera.

## 1. Casos públicos (10 min)

Um por vez, sessão nova, pedido padrão do tema. Salve cada resposta em `reports/<tema>-<criadora>-publico-NN.md`.

| Caso | Skill disparou? | Linha citada | Passou? | Pontos |
|---|---|---|---|---|
| 01 | | | | /2 |
| 02 | | | | /2 |
| 03 | | | | /2 |
| 04 (limpo) | | achados médio+: ___ | | /2 |

Subtotal casos públicos: ____/8

## 2. Casos novos (6 min)

Até 4 trechos SEUS, pequenos e compiláveis, um bug do tema em cada (ou nenhum, no caso limpo). Documente cada um com `casos-novos/template.md`. Salve as respostas em `reports/<tema>-<criadora>-novo-NN.md`.

| Caso | Bug esperado (linha) | Passou? | Aceito pela auditora? | Ponto criadora | Ponto testadora |
|---|---|---|---|---|---|
| N1 | | | | | |
| N2 | | | | | |
| N3 | | | | | |
| N4 | | | | | |

Subtotal casos novos: criadora ____/4, testadora ____

## 3. Gatilho (4 min)

| # | Prompt | Esperado | Disparou? | Ponto |
|---|---|---|---|---|
| 1 | | dispara | | |
| 2 | | dispara | | |
| 3 | | dispara | | |
| 4 | | não dispara (near-miss) | | |
| 5 | | não dispara (near-miss) | | |

Subtotal gatilho: ____/5

## 4. Entregar (2 min)

**Total da criadora: ____/17**   **Pontos da testadora (casos novos falhados): ____**

PR no repo da criadora com esta ficha, `reports/` e `casos-novos/`, até 21h20. Título: `S03 Aula 02: teste de review-<tema> por <equipe testadora>`.

Assinaturas: testadora ________  criadora ________  auditora ________

## Comentário (3 linhas, opcional): o que a skill faria melhor com uma mudança só

____________________________________________________________________

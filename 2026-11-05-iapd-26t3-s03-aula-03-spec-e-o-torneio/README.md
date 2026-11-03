# IAPD-26T3 · Semana 03 · Aula 03 · Qui 05/11/2026

**Spec e o Torneio: a terceira camada, skills seguras e o Red Team contra o Blue Team**

Slides: `IAPD-26T3 - S03 - Aula 03 - 2026-11-05 - Spec e o Torneio.pdf`

## Agenda

| Hora | Bloco |
|---|---|
| 19h00 | Placar acumulado e a terceira camada |
| 19h05 | Bloco 5: spec e as três camadas no projeto |
| 19h30 | Bloco 6: skill é código de terceiros |
| 19h45 | Atividade 3.1: Auditoria relâmpago |
| 20h00 | Intervalo |
| 20h10 | Disputa 3: Torneio Red Team x Blue Team (70 min) |
| 21h20 | Campeão, as três camadas, ponte para a S04 |

## Atividades

| Atividade | Pasta | O que usa |
|---|---|---|
| 3.1 Auditoria relâmpago (12 min) | `atividades/3.1-auditoria-relampago/` | 3 skills em `skills/` e o `checklist.md` de 10 itens |
| Disputa 3: Torneio (70 min) | `atividades/disputa-3-torneio/` | `regras.md`, `red-team-regras.md`, `envelope-red-team.md` (com a coluna "Regra EARS violada") |

Base do Torneio: branch `clean` do repo [iapd-26t3-pagamentos-api](https://github.com/SENAI-IA/iapd-26t3-pagamentos-api), copiada para `iapd-26t3-eNN-torneio`.

## Lista da semana (entrega até 09/11, por Pull Request no repo da equipe)

1. Suíte `review-*` da equipe publicada no repo da equipe, com README explicando quando cada skill dispara.
2. `evals/evals.json` com 5 casos (um near-miss) e `benchmark.json` de uma rodada com e sem skill, mais um parágrafo sobre o delta. Modelos em `lista-da-semana/evals/`.
3. Auditoria escrita de uma skill pública (skills.sh ou GitHub), seguindo `atividades/3.1-auditoria-relampago/checklist.md`.
4. Preparação para a S04: 5 linhas sobre o projeto individual.

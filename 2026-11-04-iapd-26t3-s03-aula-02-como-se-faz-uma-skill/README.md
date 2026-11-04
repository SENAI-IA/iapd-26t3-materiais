# IAPD-26T3 · Semana 03 · Aula 02 · Qua 04/11/2026

**Como se faz uma skill: o passo a passo, o gatilho medido e a avaliação entre equipes**

Slides: `IAPD-26T3 - S03 - Aula 02 - 2026-11-04 - Como se faz uma skill.pdf`

## Agenda

| Hora | Bloco |
|---|---|
| 19h00 | Placar da revisão cruzada e a pergunta de hoje |
| 19h10 | Bloco 3: o problema do gatilho |
| 19h30 | Atividade 2.1: O gatilho certo |
| 20h00 | Intervalo |
| 20h10 | Bloco 4: como se faz uma skill, em seis passos |
| 20h30 | Atividade 2.2: criar duas skills finas |
| 21h05 | Disputa 2: troca e avaliação de skills |
| 21h25 | Placar, o que fica, amanhã |

## Os seis passos (Bloco 4)

1. **Tarefa**: do tamanho de uma função. Faça à mão, com o agente, uma vez.
2. **Gotchas**: cada correção que você deu ao modelo vira uma linha.
3. **Descrição**: o quê + quando + o que não faz. Teste com near-miss.
4. **Corpo**: procedimento, template de saída, checklist. Menos de 500 linhas.
5. **Scripts**: determinístico vai para `scripts/`; longo e raro, `references/`.
6. **Teste**: `validate.py`, 3 rodadas de gatilho, evals com e sem skill.

## Atividades

| Atividade | Pasta | O que usa |
|---|---|---|
| 2.1 O gatilho certo (30 min) | `atividades/2.1-gatilho-certo/` | `ficha.md` e os 20 prompts de `trigger-eval.json` |
| 2.2 Criar duas skills (35 min) | `atividades/2.2-criar-e-trocar-skills/` | `ficha.md`, `template/review-tema/` (SKILL.md, evals.json, scripts/) e `validate.py` |
| Disputa 2: troca e avaliação (20 min) | `atividades/2.2-criar-e-trocar-skills/` | `rubrica.md`: 6 critérios de 0 a 2 + 5 prompts de gatilho, máximo 17 por skill |
| Extra: suíte e agente revisor | `atividades/extra-suite-e-agente-revisor/` | leitura para a lista da semana: `suite-referencia/` (gabarito de estrutura), `kiro/` (agentes, hook, steering) e `claude/` |
| Extra: dissecação | `atividades/extra-dissecacao/` | 4 skills reais para criticar com a `ficha.md` |

As skills são feitas sobre o projeto da equipe vizinha (o construído ontem a partir da spec de `1.1-spec-pagamentos/`). Os gotchas precisam apontar requisito da spec (R01 a R12).

## Disputa 2

Rodízio: 1 avalia 2, 2 avalia 3, última avalia 1. Cada equipe clona e instala as duas skills da avaliada, preenche a `rubrica.md` por skill (nota sem a linha do SKILL.md que justifica não vale) e roda 5 prompts de gatilho próprios (3 positivos, 2 near-misses). Até 17 por skill, 34 por equipe, +3 para a avaliação mais bem justificada. Acumula no `placar-da-semana.md`.

## Entregáveis de hoje

- 2 skills `review-*` (ou `pr-summary`) novas no repo da equipe, por PR, até 21h05: `SKILL.md` válido, `evals/evals.json` com 5 prompts de gatilho e 3 casos.
- 2 fichas de rubrica preenchidas no repo da equipe avaliada, em `reviews/`, até 21h25.

## Lista da semana (entrega 09/11)

Completar a suíte (`extra-suite-e-agente-revisor/` como referência), `evals.json` + `benchmark.json` de uma rodada com e sem skill, auditoria de uma skill pública (checklist da Aula 3) e 5 linhas sobre o projeto do trabalho final. As skills de hoje são a arma do Blue Team no Torneio de quinta.

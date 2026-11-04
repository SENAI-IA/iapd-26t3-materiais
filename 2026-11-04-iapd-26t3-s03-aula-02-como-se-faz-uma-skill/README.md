# IAPD-26T3 · Semana 03 · Aula 02 · Qua 04/11/2026

**Como se faz uma skill: seis passos na primeira metade, o Duelo das Skills na segunda**

Slides: `IAPD-26T3 - S03 - Aula 02 - 2026-11-04 - Como se faz uma skill.pdf`

## Agenda

| Hora | Bloco |
|---|---|
| 19h00 | Bloco 3: seis passos para uma skill (passos 1 e 2) |
| 19h20 | Demo ao vivo: o gatilho medido (passo 3) |
| 19h35 | Passos 4 a 6: o agente escreve a skill ao vivo |
| 19h45 | Catálogos ao vivo: [skills.sh](https://skills.sh/) e [SkillsMP](https://skillsmp.com/) |
| 19h55 | Sorteio: 3 temas, 2 equipes por tema |
| 20h00 | Intervalo |
| 20h20 | Duelo, fase 1: criar a skill (35 min) |
| 20h55 | Duelo, fase 2: testar a skill da adversária (25 min) |
| 21h20 | Auditoria cruzada, placar da semana, amanhã |

## Os seis passos (Bloco 3)

1. **Tarefa**: do tamanho de uma função. Faça à mão, com o agente, uma vez.
2. **Gotchas**: cada correção que você deu ao modelo vira uma linha.
3. **Descrição**: o quê + quando + o que não faz. É o gatilho inteiro; teste com near-miss.
4. **Corpo**: procedimento, template de saída, checklist. Menos de 500 linhas.
5. **Scripts**: determinístico vai para `scripts/`; longo e raro, `references/`.
6. **Teste**: `validate.py`, 3 rodadas de gatilho, evals com e sem skill.

## Atividades

| Atividade | Pasta | O que usa |
|---|---|---|
| Demo do gatilho (professor, 20 min) | `atividades/demo-gatilho/` | 4 skills da `extra-suite-e-agente-revisor/suite-referencia/` instaladas; 6 prompts de `trigger-eval.json` (3 positivos, 3 near-misses), 3 rodadas; a turma prevê antes. A `ficha.md` fica como exercício extra |
| Disputa 2: o Duelo das Skills (70 min) | `atividades/disputa-2-duelo-das-skills/` | `regras.md`, `ficha-criacao.md`, `ficha-teste.md`, `template/review-tema/`, `validate.py`, os casos públicos em `casos/<tema>/` e o template de caso novo em `casos-novos/` |
| Extra: suíte e agente revisor | `atividades/extra-suite-e-agente-revisor/` | leitura para a lista da semana: `suite-referencia/`, `kiro/` (agentes, hook, steering) e `claude/` |
| Extra: dissecação | `atividades/extra-dissecacao/` | 4 skills reais para criticar com a `ficha.md` |

## O Duelo em uma linha

Sorteio de 3 temas (`review-security`, `review-correctness`, `review-performance`), 2 equipes por tema. Cada equipe cria UMA skill no próprio projeto. A adversária instala a skill sem mexer nela e roda, em sessão nova, os 4 casos públicos do tema (+2 cada), até 4 casos novos que ela mesma cria e documenta (+1 cada para a criadora se passar, +1 para a testadora se falhar e a auditora aceitar) e 5 prompts de gatilho (+1 cada). Máximo 17. Não há gabarito escondido nem professor corrigindo: testadora pontua, criadora confere, uma terceira equipe audita. Detalhes em `regras.md`.

## Entregáveis de hoje

- Fase 1: PR no repo da equipe com `review-<tema>/` (SKILL.md válido, scripts, evals), até 20h55.
- Fase 2: PR no repo da criadora com a `ficha-teste.md` preenchida, `reports/` e `casos-novos/`, até 21h20. Linha no `placar-da-semana.md` assinada por testadora, criadora e auditora.

## Lista da semana (entrega 09/11)

Completar a suíte (`extra-suite-e-agente-revisor/` como referência), `evals.json` + `benchmark.json` de uma rodada com e sem skill, auditoria de uma skill pública (checklist da Aula 3) e 5 linhas sobre o projeto do trabalho final. A skill de hoje é a arma do Blue Team no Torneio de quinta.

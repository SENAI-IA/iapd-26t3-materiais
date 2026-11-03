# Semana 3: steering, skill e spec (03 a 05/11/2026)

Três camadas de contexto de um agente de código, do mais amplo e permanente para o mais estreito e efêmero, uma por aula. Fio condutor prático: code review com agentes sobre o repo [iapd-26t1-pagamentos-api](https://github.com/SENAI-IA/iapd-26t1-pagamentos-api).

| Camada | Pergunta | Escopo | Quando carrega | Aula |
|---|---|---|---|---|
| Steering | Como trabalhamos neste repositório? | o projeto inteiro | sempre, em todo turno | Aula 1 |
| Skill | Como se faz este tipo de tarefa? | um tipo de tarefa, em qualquer repo | sob demanda, quando a descrição casa | Aulas 1 e 2 |
| Spec | O que estamos construindo agora? | uma feature | uma vez, até entregar | Aula 3 (aprofunda na S5) |

## Aulas

| Aula | Data | Slides | Práticas |
|---|---|---|---|
| 1. Steering e skill | Ter 03/11 | `slides/aula-01-steering-e-skill.pdf` | 1.1 steering do repo; 1.2 Dissecação (`kit/kit-skills/dissecacao`, ficha `kit/fichas/aula1-dissecacao.md`); 1.3 skill v0 + Disputa 1 (`kit/kit-skills/template`) |
| 2. Múltiplas skills | Qua 04/11 | `slides/aula-02-multiplas-skills.pdf` | 2.1 O gatilho certo (`kit/fichas/aula2-gatilho-certo.md`, `aula2-trigger-eval.json`); 2.2 suíte + agente revisor (`kit/kit-skills/suite-referencia`, `kit/kiro`, `kit/claude`) + Disputa 2 |
| 3. Spec e o Torneio | Qui 05/11 | `slides/aula-03-spec-e-o-torneio.pdf` | 3.1 Auditoria relâmpago (`kit/kit-skills/auditoria`, `kit/fichas/aula3-checklist-auditoria.md`); Disputa 3: Torneio (`kit/fichas/aula3-torneio.md`, `aula3-envelope-red-team.md`) |

## Onde cada camada mora

| Camada | Kiro | Claude Code | VS Code + Copilot | Neutro |
|---|---|---|---|---|
| Steering | `.kiro/steering/*.md` | `CLAUDE.md`; `.claude/rules/*.md` | `.github/copilot-instructions.md`; `.github/instructions/*.instructions.md` | `AGENTS.md` |
| Skill | `.kiro/skills/` | `.claude/skills/` | `.github/skills/` (lê `.claude/skills/` também) | mesmo `SKILL.md` |
| Agente | `.kiro/agents/*.json` | `.claude/agents/*.md` | `.github/agents/*.agent.md` | n/a |
| Hook | `.kiro/hooks/*.json` | `settings.json` | `.github/hooks/*.json` | n/a |
| Spec | `.kiro/specs/<feature>/` | plan mode + markdown | agente Planner + markdown | `spec-kit` (`specs/<feature>/`) |

## Lista da semana (entrega até 09/11, por Pull Request no repo da equipe)

1. Suíte `review-*` da equipe publicada no repo da equipe, com README explicando quando cada skill dispara.
2. `evals/evals.json` com 5 casos (um near-miss) e `benchmark.json` de uma rodada com e sem skill, mais um parágrafo sobre o delta (modelos em `kit/evals/`).
3. Auditoria escrita de uma skill pública (skills.sh ou GitHub), seguindo `kit/fichas/aula3-checklist-auditoria.md`.
4. Preparação para a S4: 5 linhas sobre o projeto individual.

## Validar uma skill

```bash
python kit/kit-skills/validate.py <pasta-da-skill>
```

Relatórios de review seguem `kit/reports/TEMPLATE.md` e são validados com `scripts/validate_report.py` do repo pagamentos-api.

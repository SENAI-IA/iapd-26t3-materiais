# IAPD-26T3 · Semana 03 · Aula 01 · Ter 03/11/2026

**Spec, steering e skill: da spec ao projeto, as regras da casa e a primeira skill de code review**

Primeira das três camadas de contexto do agente (spec → steering → skill, apresentadas do mais amplo para o mais estreito: steering, skill, spec). Ferramenta livre: Kiro, VS Code + Copilot ou Claude Code.

Slides: `IAPD-26T3 - S03 - Aula 01 - 2026-11-03 - Spec, steering e skill.pdf`

## Agenda

| Hora | Bloco |
|---|---|
| 19h00 | Org SENAI-IA: equipes, apelidos, logos e repos |
| 19h10 | As três camadas e a pergunta da semana |
| 19h15 | Bloco 1: spec e steering |
| 19h35 | Atividade 1.1: da spec ao projeto |
| 20h10 | Intervalo |
| 20h20 | Bloco 2: skill, o método, a anatomia |
| 20h45 | Atividade 1.2: skill v0 + Disputa 1 cruzada |
| 21h20 | Placar, o que fica, amanhã |

## Atividades

| Atividade | Pasta | O que usa |
|---|---|---|
| 1.1 Da spec ao projeto (35 min) | `atividades/1.1-spec-pagamentos/` | `requirements.md` (12 requisitos EARS), `design.md`, `tasks.md`. A equipe cria `iapd-26t3-eNN-pagamentos` na org, escreve o steering antes do código e executa as tasks com o agente até `pytest -q` verde |
| 1.2 Skill v0 + Disputa 1 cruzada (35 min) | `atividades/1.2-skill-v0/` | `template/code-review/`, `validate.py`, `reports/TEMPLATE.md`, `disputa-1-revisao-cruzada.md` |

Plano B da 1.1: a branch `clean` do repo [iapd-26t3-pagamentos-api](https://github.com/SENAI-IA/iapd-26t3-pagamentos-api) implementa a mesma spec.

Placar acumulado da semana: `atividades/placar-da-semana.md`.

## Entregáveis de hoje

Repo `iapd-26t3-eNN-pagamentos` com 12 testes `test_rNN` verdes, steering da equipe, skill `code-review-<equipe>` com frontmatter válido, `reports/<equipe>-v0.md` entregue por PR à equipe vizinha. Guarde tudo: amanhã a v0 vira suíte e roda de novo sobre os mesmos projetos.

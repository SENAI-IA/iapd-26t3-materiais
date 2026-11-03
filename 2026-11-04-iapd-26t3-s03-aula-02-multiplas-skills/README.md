# IAPD-26T3 · Semana 03 · Aula 02 · Qua 04/11/2026

**Múltiplas skills: skills finas de code review, do monólito à suíte com agente revisor**

Slides: `IAPD-26T3 - S03 - Aula 02 - 2026-11-04 - Multiplas skills.pdf`

## Agenda

| Hora | Bloco |
|---|---|
| 19h00 | Placar da revisão cruzada e a pergunta de hoje |
| 19h10 | Bloco 3: o problema do gatilho |
| 19h30 | Atividade 2.1: O gatilho certo |
| 20h00 | Intervalo |
| 20h10 | Bloco 4: granularidade e composição |
| 20h30 | Atividade 2.2: suíte + agente revisor |
| 21h15 | Disputa 2: revisão cruzada, rodada 2 |

## Atividades

| Atividade | Pasta | O que usa |
|---|---|---|
| 2.1 O gatilho certo (30 min) | `atividades/2.1-gatilho-certo/` | `ficha.md` e os 20 prompts de `trigger-eval.json` |
| 2.2 Suíte + agente revisor (45 min) | `atividades/2.2-suite-e-agente-revisor/` | `suite-referencia/` (só como gabarito de estrutura), `kiro/` (agentes, hook, steering) e `claude/`; no Copilot, `.github/agents/*.agent.md`. Os scripts `collect_diff.sh` e `validate_report.py` estão em `iapd-26t3-pagamentos-api/scripts/` |
| Extra (aquecimento) | `atividades/extra-dissecacao/` | 4 skills reais para criticar com a `ficha.md` |

Disputa 2: a suíte v1 roda sobre o MESMO projeto vizinho de ontem, contra a spec. Mesma pontuação da Disputa 1 (dona confirma com teste que falha ou rejeita com justificativa), mais +5 para o maior ganho de achados confirmados v0 para v1 e +3 para a maior redução de falsos positivos.

## Entregáveis de hoje

3 skills `review-*` + `review-orchestrator`, agente revisor no formato da sua ferramenta, hook de testes, `reports/<equipe>-v1.md` por PR no repo da vizinha.

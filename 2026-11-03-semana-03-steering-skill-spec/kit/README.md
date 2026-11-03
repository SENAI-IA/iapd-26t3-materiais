# Kit de artefatos: Semana 3, Criação de Skills

Turma S.D. "IA Aplicada à Produtividade no Desenvolvimento". Aulas de 03, 04 e 05/11/2026.
Tema do hands-on: code review com agentes, no repositório `pagamentos-api`.

## Mapa de pastas

```
S03-skills-artefatos/
├── pagamentos-api/          repo git. Branch main = código em revisão (14 bugs). Branch clean = referência.
│   ├── app/                 money, db, auth, payments, refunds, ledger, webhooks, api
│   ├── tests/               suíte do projeto (verde nas duas branches)
│   └── scripts/             collect_diff.sh, validate_report.py, score.py
├── pagamentos-api-clean/    cópia exportada da branch clean, sem .git: base do Torneio
├── kit-skills/
│   ├── validate.py          valida frontmatter de SKILL.md contra a spec Agent Skills
│   ├── dissecacao/          Aula 1: pytest-triage, code-helper, review-everything, lint-fix
│   ├── template/code-review Aula 1: ponto de partida da skill v0 do grupo
│   ├── suite-referencia/    Aula 2: review-security, review-correctness, review-performance, review-orchestrator, pr-summary
│   └── auditoria/           Aula 3: review-helper, git-commit-msg, pytest-runner
├── kiro/                    agents (revisor + 3 subagentes), hook tests-on-save, steering
├── claude/                  mesma suíte no Claude Code (portabilidade)
├── fichas/                  fichas das atividades e disputas, placar
├── evals/                   templates de evals.json e benchmark.json (Aula 3)
├── reports/                 TEMPLATE.md e exemplo-v0.md
```

## Pré-requisitos (antes da terça)

- Python 3.10+ e `pip install pytest`
- Git
- Kiro (IDE ou CLI V3) logado, ou outro agente que leia `SKILL.md` (Claude Code, Codex CLI, Gemini CLI)

## Comandos que o aluno usa

```bash
cd pagamentos-api
pytest -q                                                   # suíte do projeto: deve passar
scripts/collect_diff.sh clean main                          # diff + mensagens de commit para o revisor
python scripts/validate_report.py reports/<grupo>-v0.md     # formato do relatório
python ../kit-skills/validate.py .kiro/skills/<minha-skill> # frontmatter da skill
```

O `score.py` precisa do `gabarito.json`, que fica com o professor até o fim de cada disputa:

```bash
python scripts/score.py reports/<grupo>-v0.md <caminho>/gabarito.json
```

## Formato do achado (não negociável)

| # | Arquivo | Linha | Severidade | Categoria | Evidência | Sugestão |
|---|---|---|---|---|---|---|

Severidade: crítico, alto, médio, baixo. Categoria: correção, segurança, desempenho, dados/dinheiro, concorrência, manutenibilidade. Com ou sem acento, tanto faz. Achado sem linha ou sem evidência não pontua.

## Pontuação das disputas

+3 crítico, +2 alto, +1 médio ou baixo, -1 falso positivo, -2 achado sem linha. Máximo por rodada: 28 pontos.

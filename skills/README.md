# Skills compartilhadas

Skills que a turma considera boas o bastante para qualquer equipe instalar. Padrão aberto [Agent Skills](https://agentskills.io): uma pasta por skill com `SKILL.md` (frontmatter `name` e `description`) e, se precisar, `scripts/`, `references/`, `assets/` e `evals/`.

Para entrar aqui, a skill precisa:

1. Passar em `python ../2026-11-03-semana-03-steering-skill-spec/kit/kit-skills/validate.py <pasta>`.
2. Ter `evals/evals.json` com pelo menos 3 casos (um near-miss) e um `benchmark.json` de uma rodada com e sem skill.
3. Passar pelo checklist de auditoria da semana 3 (nada de rede em `Prerequisites`, nada de instrução escondida).

Instalação: copie a pasta para `.kiro/skills/`, `.claude/skills/` ou `.github/skills/`, conforme a ferramenta. O conteúdo é o mesmo.

Contribua por Pull Request a partir do repo da equipe.

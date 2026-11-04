# Skills compartilhadas

Skills que a turma considera boas o bastante para qualquer equipe instalar. Padrão aberto [Agent Skills](https://agentskills.io): uma pasta por skill com `SKILL.md` (frontmatter `name` e `description`) e, se precisar, `scripts/`, `references/`, `assets/` e `evals/`.

Para entrar aqui, a skill precisa:

1. Passar em `python ../2026-11-03-iapd-26t3-s03-aula-01-spec-steering-e-skill/atividades/1.2-skill-v0/validate.py <pasta>`.
2. Ter `evals/evals.json` com pelo menos 3 casos (um near-miss) e um `benchmark.json` de uma rodada com e sem skill.
3. Passar pelo checklist de auditoria da semana 3 (nada de rede em `Prerequisites`, nada de instrução escondida).

Instalação: copie a pasta para `.kiro/skills/`, `.claude/skills/` ou `.github/skills/`, conforme a ferramenta. O conteúdo é o mesmo.

Contribua por Pull Request a partir do repo da equipe.

## Onde a comunidade publica skills

| Site | O que é | Como usar |
|---|---|---|
| [skills.sh](https://skills.sh/) | diretório da Vercel, leaderboard por instalações | `npx skills add <owner>/<repo>` (Claude Code, Cursor, Codex, Copilot); publicar = repo público + PR em `vercel-labs/skills` |
| [SkillsMP](https://skillsmp.com/) | catálogo independente raspado do GitHub, 3,9 milhões de SKILL.md, busca semântica | só lista repos com 2+ estrelas; eles mesmos avisam: revise o código antes de instalar |
| [anthropics/skills](https://github.com/anthropics/skills) | repo oficial: spec, `template/`, exemplos (docx, pptx, pdf, xlsx, mcp-builder...) | `/plugin marketplace add anthropics/skills` |
| [agentskills.io](https://agentskills.io) | o padrão aberto Agent Skills | é o que o `validate.py` da turma checa |
| [awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | lista curada: coleções, guias, segurança | leitura |

Antes de instalar qualquer uma, leia o `SKILL.md`: Snyk (fev/2026) achou 13,4% das skills públicas com problema crítico. A auditoria da Aula 3 usa uma skill sorteada daqui.

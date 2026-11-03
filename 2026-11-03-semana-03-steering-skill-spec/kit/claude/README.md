# claude/: a mesma suíte em outro agente (portabilidade)

A spec Agent Skills é a mesma. Para rodar a suíte no Claude Code:

```bash
mkdir -p .claude/skills
cp -r kit-skills/suite-referencia/* .claude/skills/     # mesmos SKILL.md, sem mudar uma linha
```

Depois, em sessão nova: `/review-security` ou "revisa este repositório". O equivalente do hook
`tests-on-save` vai em `.claude/settings.json` (hooks PostToolUse em Edit/Write rodando `pytest -q`);
o equivalente dos subagentes é `context: fork` no frontmatter ou um agente em `.claude/agents/`.
Esses campos extras são ignorados pelo Kiro, e os do Kiro são ignorados pelo Claude Code: a parte
portável é o SKILL.md.

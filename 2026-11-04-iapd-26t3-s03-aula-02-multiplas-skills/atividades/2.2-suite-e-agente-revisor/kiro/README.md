# kiro/: configuração do agente revisor no Kiro (V3)

Copie para a raiz do repositório `pagamentos-api` assim:

```
pagamentos-api/
└── .kiro/
    ├── agents/    <- kiro/agents/*.json  (revisor + 3 subagentes)
    ├── hooks/     <- kiro/hooks/tests-on-save.json
    ├── steering/  <- kiro/steering/conventions.md
    └── skills/    <- suite-referencia/*  (ou a suíte do grupo)
```

- `revisor.json` é o orquestrador: lista `subagent/review-*` em `tools` e a skill `review-orchestrator` em `resources`.
- `review-security.json`, `review-correctness.json`, `review-performance.json` são subagentes de contexto isolado; cada um carrega só a própria skill e não pode escrever arquivos.
- `tests-on-save.json`: hook que roda `pytest -q` a cada `.py` salvo; o resultado volta ao agente. O que "deve valer toda vez" vai em hook, não em skill.
- `conventions.md`: steering `always`, poucas linhas. Regras do projeto, não procedimento.

Permissões seguem a regra do mais estrito: um `deny` em qualquer lado bloqueia. Confira o formato exato dos campos na doc do Kiro antes da aula (ver Caveats do plano).

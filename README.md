# iapd-26t1-materiais

Materiais da turma **IAPD-26T1** (IA Aplicada à Produtividade no Desenvolvimento, 1ª turma de 2026), do curso IAPD da org [SENAI-IA](https://github.com/SENAI-IA).

Professores publicam; alunos leem. Erro ou sugestão: abra uma issue neste repositório.

## Como este repositório é organizado

Uma pasta por semana, nomeada com a data da primeira aula e o tema. Dentro dela, uma pasta `slides/` com os PDFs de cada aula e, quando houver, um `kit/` com os artefatos das práticas (skills, fichas das disputas, templates).

```
iapd-26t1-materiais/
├── 2026-10-19-semana-01-fundamentos-de-llm/
├── 2026-11-03-semana-03-steering-skill-spec/
│   ├── slides/           PDFs das três aulas
│   └── kit/              skills, fichas, evals, templates das práticas
├── prompts/              exemplos de prompt compartilhados pela turma
├── skills/               skills compartilhadas pela turma (padrão agentskills.io)
└── README.md
```

Repositórios irmãos usados nas práticas:

| Repositório | Para quê |
|---|---|
| [iapd-26t1-pagamentos-api](https://github.com/SENAI-IA/iapd-26t1-pagamentos-api) | repo de pagamentos usado nas disputas de code review da semana 3 (branches `main` e `clean`) |
| `iapd-26t1-eNN-<projeto>` | um por equipe; é onde ficam a suíte de skills, os relatórios e o projeto individual de cada aluno |

## Calendário

| Semana | Datas | Tema |
|---|---|---|
| S1 | 19, 21, 22/10 | Fundamentos de LLM |
| S2 | 26, 28, 29/10 | Janela de contexto e gasto de créditos |
| S3 | 03, 04, 05/11 | Steering, skill e spec (code review com agentes) |
| S4 | 09, 11, 12/11 | Vibe Coding vs SDD (mini-projeto avaliativo) |
| S5 | 16, 18, 19/11 | Especificações (EARS, specs, Tribunal da Spec) |
| S6 | 23, 25, 26/11 | Criação de código (tasks, hooks, MCP, CLI, Git) |
| S7 | 30/11, 02, 03/12 | Uso de IA para testes |
| S8 | 07, 09, 10/12 | Documentação viva e guardrails |
| S9 | 14, 16, 17/12 | Projeto avaliativo individual (mentoria + pitch) |

## Ferramentas

O conteúdo é agnóstico de ferramenta. Tudo que é mostrado existe em Kiro, VS Code com Copilot e Claude Code; cada aluno usa a que preferir. Skills seguem o padrão aberto [Agent Skills](https://agentskills.io) e funcionam sem alteração nas três.

## Convenções da org

Estão no cartão de visita da organização: código da turma `IAPD-26T1`, equipes `IAPD-26T1-E01`, `E02`... (apelido opcional depois do código), repositórios em minúsculas com hífen, trabalho individual em pasta com o usuário do GitHub dentro do repo da equipe, entrega por Pull Request. Dúvidas: `@SENAI-IA/professores`.

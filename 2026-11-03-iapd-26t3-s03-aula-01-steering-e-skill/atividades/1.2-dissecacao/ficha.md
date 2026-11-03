# Ficha: Dissecação de skills (Aula 1, Atividade 1.1, 25 min)

Grupo: ____________________

Vocês receberam 4 skills em `skills/ (esta pasta)/`: `pytest-triage`, `code-helper`, `review-everything`, `lint-fix`.
Em 15 minutos, preencham a ficha. Depois, 10 minutos de revelação.

## Parte 1: Frontmatter contra a spec (1 ponto por violação encontrada)

Spec resumida (agentskills.io): `name` obrigatório, 1 a 64 caracteres, só `[a-z0-9-]`, sem hífen nas pontas nem duplo, igual ao nome da pasta; `description` obrigatória, 1 a 1024 caracteres, diz o QUE faz e QUANDO usar; `compatibility` até 500; `metadata` é mapa de strings; corpo recomendado abaixo de 500 linhas.

| Skill | `name` ok? | `description` diz o quê E quando? | Outros campos | Violações encontradas |
|---|---|---|---|---|
| pytest-triage | | | | |
| code-helper | | | | |
| review-everything | | | | |
| lint-fix | | | | |

## Parte 2: Estimativa de tokens nos 3 níveis

Nível 1 = name + description (sempre no contexto). Nível 2 = corpo do SKILL.md (ao ativar). Nível 3 = references/, assets/ (sob demanda); scripts/ são executados, não lidos. Regra de bolso: 1 token a cada 4 caracteres.

| Skill | Nível 1 (tokens) | Nível 2 (tokens) | Nível 3 existe? | Custo se 30 skills assim estiverem instaladas (nível 1 x 30) |
|---|---|---|---|---|
| pytest-triage | | | | |
| code-helper | | | | |
| review-everything | | | | |
| lint-fix | | | | |

## Parte 3: Padrões e anti-padrões (2 de cada por skill)

Padrões bons: gotchas do ambiente, template de saída, checklist, validation loop com script, "quando NÃO usar", explica o porquê, defaults em vez de menus.
Anti-padrões: descrição vaga, explica o que o modelo já sabe, monólito sem references, SEMPRE/NUNCA sem motivo, cobrir todo caso de borda, instrução que roda comando externo sem o usuário ver.

| Skill | 2 padrões bons | 2 anti-padrões |
|---|---|---|
| pytest-triage | | |
| code-helper | | |
| review-everything | | |
| lint-fix | | |

## Parte 4: Ranking e a pergunta extra

Ordem da melhor para a pior: 1. ________ 2. ________ 3. ________ 4. ________

Pergunta extra (2 pontos): alguma dessas skills faz algo que você NÃO instalaria no seu computador sem ler antes? Qual, e em que linha?

__________________________________________________________________________

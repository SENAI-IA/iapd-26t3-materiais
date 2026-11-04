# Ficha: Criar duas skills (Aula 2, Atividade 2.2, 35 min)

Equipe: ____________________   Projeto vizinho revisado: ____________________

Objetivo: duas skills finas de review, feitas pelo passo a passo, instaladas no repo da equipe e entregues por PR até 21h05. Na Disputa 2 a equipe seguinte avalia as duas com `rubrica.md`.

## Passo 1 (2 min): escolher duas

Da família `review-*`: security, correctness, performance, money. Ou `pr-summary`. Cada skill cobre UM tema e diz no `description` o que não cobre.

Skill A: ______________   Skill B: ______________

## Passo 2 (5 min por skill): à mão, sem skill

Abra o projeto da equipe vizinha (o de ontem, construído a partir da spec) no agente, sem skill nenhuma, e peça a revisão do tema. Cada vez que o modelo erra ou deixa passar e você corrige, anote aqui. Isso é a matéria-prima: sem correções, não há skill.

| # | O que o modelo fez ou deixou passar | Correção que você deu | Requisito (R__) |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

## Passos 3 a 5 (15 min por skill): escrever

Copie `template/review-tema/` para a pasta de skills do repo da equipe (`.kiro/skills/`, `.claude/skills/` ou `.github/skills/`) com o nome certo e preencha:

- [ ] `description`: o quê + quando (palavras do usuário) + o que não faz
- [ ] Gotchas: uma linha por correção da tabela acima, com o R__
- [ ] Procedimento com passos e template de saída (arquivo, linha, requisito)
- [ ] O que é repetível foi para `scripts/`; o que é longo e raro, para `references/`
- [ ] Corpo abaixo de 500 linhas

Pode usar o agente para escrever, desde que alimentado: transcrição da revisão à mão, spec e este template. "Escreva uma skill de code review" sem contexto dá skill genérica (vale 1 na rubrica).

## Passo 6 (5 min por skill): testar

- [ ] `python validate.py <pasta-da-skill>` passou
- [ ] `evals/evals.json` preenchido: 5 prompts de gatilho (3 disparam, 2 near-misses) e 3 casos
- [ ] 3 rodadas em sessão nova: a skill disparou nos 3 positivos e não disparou nos 2 near-misses? ___/5
- [ ] Rodou no projeto vizinho: achou o que você achou à mão? O que faltou virou gotcha?

## Divisão sugerida

Uma pessoa faz a revisão à mão e anota; outra escreve a descrição e os prompts de gatilho; outra o procedimento e os scripts. Troquem de papel na segunda skill.

## Entrega (até 21h05)

PR no repo da equipe com as duas pastas de skill, cada uma com `SKILL.md` e `evals/evals.json`. Título do PR: `S03 Aula 02: skills <A> e <B>`.

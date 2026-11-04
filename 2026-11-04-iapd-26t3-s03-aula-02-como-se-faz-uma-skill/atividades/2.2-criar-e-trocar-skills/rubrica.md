# Rubrica: a skill da vizinha é boa? (Disputa 2, 20 min)

Equipe avaliadora: ____________   Equipe avaliada: ____________   Skill: ____________

Rodízio: equipe 1 avalia a 2, a 2 avalia a 3, a última avalia a 1. Clone o repo da avaliada, instale as duas skills e preencha uma ficha desta por skill.

Regra de ouro: **nota sem a linha do SKILL.md que a justifica não vale.** Cite o trecho.

## Parte A: seis critérios (0 a 2)

| Critério | 0 | 1 | 2 | Nota | Linha do SKILL.md que justifica |
|---|---|---|---|---|---|
| Descrição | vaga ou só o nome | diz o quê, mas não quando | o quê + quando + o que não faz | | |
| Gotchas | nenhum | genéricos | do projeto, verificáveis na spec (R__) | | |
| Procedimento e template | prosa solta | passos sem formato de saída | passos + template com requisito | | |
| Tamanho e disclosure | monólito ou enciclopédia | cabe, mas repete o óbvio | enxuta; longo foi para references/ | | |
| Determinismo | tudo no modelo | cita scripts sem usar | scripts/ para o repetível | | |
| Segurança | rede ou segredo no SKILL.md | pede permissão larga | nada de rede, nada escondido | | |

Subtotal A (máx. 12): ____

## Parte B: gatilho (5 prompts, +1 por acerto)

Escreva 5 prompts SEUS (não os do evals.json da skill): 3 que devem disparar e 2 near-misses. Rode cada um em sessão nova com as skills da avaliada instaladas e anote o que carregou.

| # | Prompt | Esperado | Disparou? | Ponto |
|---|---|---|---|---|
| 1 | | dispara | | |
| 2 | | dispara | | |
| 3 | | dispara | | |
| 4 | | não dispara | | |
| 5 | | não dispara | | |

Subtotal B (máx. 5): ____

## Total da skill (máx. 17): ____

## Comentário (3 linhas): o que a skill faria melhor com uma mudança só

____________________________________________________________________

## Placar

- Pontos da equipe criadora: soma das duas skills (máx. 34).
- +3 para a avaliação mais bem justificada da turma (o professor escolhe pela qualidade das citações).
- Acumula com a Disputa 1 (ontem) e o Torneio (quinta) no `placar-da-semana.md`.

## Entrega

As duas fichas preenchidas por PR no repo da equipe AVALIADA, em `reviews/<equipe-avaliadora>-skill-<nome>.md`, até 21h25.

# Disputa 2: o Duelo das Skills (70 min)

Seis equipes, três temas, uma skill por equipe. Quem roda a sua skill é a adversária. Vence quem passa em mais casos de teste com menos erro.

## Sorteio (19h55)

Três temas, duas equipes por tema, duelo direto:

| Tema | Skill | Cobre | Pedido padrão |
|---|---|---|---|
| security | `review-security` | injeção, auth fraca, segredo exposto, dado sensível em log | "revisa a segurança deste arquivo" |
| correctness | `review-correctness` | lógica, borda, estado, data e fuso | "revisa a correção deste arquivo" |
| performance | `review-performance` | complexidade, I/O repetido, memória, índice | "revisa o desempenho deste arquivo" |

## Casos de teste: públicos e novos

Não há gabarito escondido. Existem dois tipos de caso:

- **Casos públicos** (`casos/<tema>/`): 4 por tema, 3 trechos com bug e 1 limpo, com `README.md` dizendo o que a skill precisa achar e em que linha. Estão no repo desde antes da aula; leia antes de escrever a skill. Toda skill do tema precisa passar neles.
- **Casos novos** (`casos-novos/`): a testadora é livre para criar até 4 trechos próprios (um pode ser limpo) para testar a skill da adversária. Só precisa documentar cada um pelo `casos-novos/template.md`: arquivo, bug esperado e linha, por que é do tema, pedido usado, resultado. A auditora aceita ou rejeita o caso (bug real, do tema, que um revisor humano acharia em 2 minutos).

## Fase 1: criar (20h20 a 20h55)

Uma skill, pelos seis passos, no projeto da própria equipe. Ficha: `ficha-criacao.md`. Template: `template/review-tema/`. Validação: `python validate.py <pasta>`. Rode nos 4 casos públicos antes de entregar.

Entrega: PR no repo da equipe com a pasta da skill, até 20h55. Depois disso a skill está congelada: nenhum commit novo conta.

## Fase 2: testar a adversária (20h55 a 21h20)

A adversária clona o repo da criadora, instala a skill na pasta da sua ferramenta e, em sessão nova a cada caso, roda:

1. Os 4 casos públicos do tema, com o pedido padrão. Primeira resposta vale.
2. Até 4 casos novos, documentados pelo template.
3. Cinco prompts de gatilho: 3 que devem disparar, 2 near-misses.

Ficha: `ficha-teste.md`. Entrega por PR no repo da criadora, até 21h20: a ficha preenchida, as saídas em `reports/` e os casos novos em `casos-novos/`.

Regras de quem testa: não edita o SKILL.md; não repete o pedido até sair bonito; achado sem arquivo e linha não conta.

## Placar

| Evento | Pontos | Para quem |
|---|---|---|
| caso público passado (4 por tema; nos casos com 2 bugs, +1 por bug) | +2 | criadora |
| caso limpo: passa se não houver achado de severidade média ou maior | (é um dos 4) | criadora |
| caso novo passado (até 4, aceitos pela auditora) | +1 | criadora |
| caso novo em que a skill falhou, aceito pela auditora | +1 | testadora |
| prompt de gatilho certo (5) | +1 | criadora |
| achado sem arquivo e linha | 0 | |

Máximo 17 para a criadora (8 + 4 + 5). Vence o duelo quem pontua mais; desempate por casos novos passados, depois gatilho. Campeã da noite: maior placar entre as 3 vencedoras.

## Quem pontua: as equipes, não o professor

1. **Testadora** preenche a `ficha-teste.md` caso a caso e abre o PR no repo da criadora.
2. **Criadora** confere e aprova, ou contesta no comentário citando o caso e a linha.
3. **Auditora** (equipe de outro tema: security é auditada por performance, performance por correctness, correctness por security) aceita ou rejeita cada caso novo, confere os casos públicos contestados e assina.
4. As 3 equipes assinam a linha do `placar-da-semana.md` por PR.

Como toda equipe testa, é testada e audita, pontuar errado não compensa: o erro aparece na rodada seguinte.

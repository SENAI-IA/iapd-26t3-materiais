# Disputa 2: o Duelo das Skills (70 min)

Seis equipes, três temas, uma skill por equipe. Quem roda a sua skill é a adversária. Vence quem acha mais bugs do tema com menos erro.

## Sorteio (19h55)

Três temas, duas equipes por tema, duelo direto:

| Tema | Skill | O que cobre no pagamentos-api |
|---|---|---|
| security | `review-security` | injeção de SQL, comparação de segredo, segredo com valor padrão, dado de cartão em log |
| correctness | `review-correctness` | paginação, datas e fusos, idempotência de webhook, erros engolidos |
| money | `review-money` | centavos e float, arredondamento de taxa, limite de reembolso |

## Fase 1: criar (20h20 a 20h55)

Uma skill, pelos seis passos, no projeto da própria equipe (o construído a partir da spec). Ficha: `ficha-criacao.md`. Template: `template/review-tema/`. Validação: `python validate.py <pasta>`.

Entrega: PR no repo da equipe com a pasta da skill, até 20h55. Depois disso a skill está congelada: nenhum commit novo conta.

## Fase 2: testar a adversária (20h55 a 21h20)

A adversária clona o repo da criadora, instala a skill na pasta da sua ferramenta e roda contra a bancada neutra, `iapd-26t3-pagamentos-api`:

1. Branch `main` (14 bugs plantados, 3 do seu tema contam cheio), sessão nova, um pedido no vocabulário do tema. Primeira resposta vale.
2. Branch `clean` (zero bugs), mesmo pedido. Qualquer achado é erro.
3. Cinco prompts de gatilho escritos pela adversária: 3 que devem disparar, 2 near-misses.

Ficha: `ficha-teste.md`. Entrega: `reports/<tema>-<equipe-criadora>-main.md`, `...-clean.md` e `...-gatilho.md` por PR no repo da criadora, até 21h20.

Regras de quem testa: não edita o SKILL.md; não repete o pedido até sair bonito; relatório no formato de tabela com arquivo e linha (achado sem linha não casa com nada).

## Placar

| Evento | Pontos |
|---|---|
| bug do tema encontrado (3 por tema) | +3 |
| bug de outro tema encontrado (até 2) | +1 |
| falso positivo na `main` | -2 |
| qualquer achado na `clean` | -2 |
| prompt de gatilho certo (5) | +1 |

Máximo 16 por skill. O professor pontua com `scripts/score_duelo.py --tema <tema>` do pagamentos-api e o gabarito lacrado. Vence o duelo quem pontua mais; desempate por menos falsos positivos, depois gatilho. Campeã da noite: maior placar entre as 3 vencedoras. Entra no `placar-da-semana.md` com a Disputa 1 e o Torneio.

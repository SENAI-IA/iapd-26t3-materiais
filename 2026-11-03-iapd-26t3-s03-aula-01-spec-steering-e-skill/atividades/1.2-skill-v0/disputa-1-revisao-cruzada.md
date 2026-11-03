# Disputa 1: revisão cruzada (Aula 01, 35 min)

Cada equipe revisa o projeto da equipe vizinha com a própria skill v0, usando a spec como gabarito.

## Rodízio

Equipe 1 revisa a 2, a 2 revisa a 3, ..., a última revisa a 1. Clone o repo `iapd-26t3-eNN-pagamentos` da vizinha.

## Como revisar

1. Instale a sua skill `code-review-<equipe>` na pasta da sua ferramenta.
2. Sessão nova: "revisa este repositório contra a spec em atividades/1.1-spec-pagamentos".
3. Salve `reports/<equipe>-v0.md` no formato de `reports/TEMPLATE.md`, com a coluna `requisito` (R01 a R12) preenchida sempre que o achado violar um requisito.
4. Rode `validate_report.py` (está em `iapd-26t3-pagamentos-api/scripts/`) até passar.
5. Entregue o relatório por Pull Request no repo da equipe dona do código.

## Como confirmar (equipe dona do código)

Para cada achado, a dona responde no PR: **confirmado** (e escreve um teste que falha, provando o bug) ou **rejeitado** (com justificativa de uma linha). Rejeição sem justificativa não vale.

## Pontuação

| Evento | Pontos |
|---|---|
| Achado que viola um requisito RNN, confirmado pela dona | +3 |
| Bug real fora da spec, confirmado | +1 |
| Achado rejeitado com justificativa (falso positivo) | -1 |
| Achado sem linha ou sem evidência | -2 |
| Dona rejeitou sem justificar | -1 para a dona |

Empate ou briga: o juiz (professor) decide pelo teste. Se dá para escrever um teste que falha, é bug.

O placar acumula até o Torneio de quinta (`../placar-da-semana.md`).

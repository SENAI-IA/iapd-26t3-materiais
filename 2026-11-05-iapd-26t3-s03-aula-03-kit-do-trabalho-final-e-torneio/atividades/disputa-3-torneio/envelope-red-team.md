# Envelope lacrado do Red Team

Grupo (Red): ____________________    Entrega para o grupo (Blue): ____________________

Entregar ao juiz ANTES da troca. Depois da entrega, nada pode ser alterado.

## Bugs plantados

| # | Categoria | Arquivo | Linha(s) | Severidade declarada | Requisito violado (RNN) e regra EARS | Teste que prova (arquivo) |
|---|---|---|---|---|---|---|
| 1 | correção | | | | | tests_red/test_bug01.py |
| 2 | segurança | | | | | tests_red/test_bug02.py |
| 3 | desempenho | | | | | tests_red/test_bug03.py |
| 4 | dados/dinheiro | | | | | tests_red/test_bug04.py |
| 5 | concorrência | | | | | tests_red/test_bug05.py |

A coluna "Regra EARS violada" é a mini-spec do comportamento correto que o bug quebra: uma frase, um teste. Vale +1 por regra verificável.

Confirmo que `pytest -q tests/` continua verde com os bugs: [ ] sim

Confirmo que `pytest -q tests_red/` falha nos 5 testes com os bugs e passa na `main`: [ ] sim

## Skill envenenada

[ ] Não plantamos skill envenenada.

[ ] Plantamos. Nome da skill: ____________________  Onde está a instrução (linha): ______

O que ela tenta fazer: __________________________________________________________

Confirmo que não faz rede, não lê credenciais e não apaga arquivos: [ ] sim

## Assinaturas

Red Team: ____________________    Juiz (hora de recebimento): ____________________

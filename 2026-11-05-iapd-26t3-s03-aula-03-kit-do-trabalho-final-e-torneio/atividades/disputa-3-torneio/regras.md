> Base do Torneio (v3): cada equipe é Red Team no PRÓPRIO projeto `iapd-26t3-eNN-pagamentos` (branch `torneio`) e Blue Team no projeto que recebe. A spec de `1.1-spec-pagamentos` é o gabarito: cada bug plantado viola um requisito RNN, declarado no envelope. Tempos: Red 12, Troca 8, Blue 20, Julgamento 10.

# Torneio de Code Review: Red Team x Blue Team (Aula 3, Disputa 3, 50 min)

Cada grupo joga as duas pontas: planta bugs no repo de outro grupo (Red) e caça os bugs plantados no repo que recebe (Blue). Campeão é a maior soma Red + Blue, somada ao placar acumulado da semana (`fichas/placar.md`).

## Material

- `o próprio projeto da equipe (iapd-26t3-eNN-pagamentos, branch `torneio`, com os 12 testes test_rNN verdes antes de plantar)/`: cópia do código correto, sem `.git`. Cada grupo começa dele.
- A suíte de skills do grupo (`review-*` + `review-orchestrator`) e o agente `revisor`.
- `scripts/validate_report.py`, `scripts/score.py` (dentro do repo).
- `envelope-red-team.md`: declaração lacrada do Red Team.
- Juiz: o professor. Em caso de dúvida sobre se um bug é legítimo, vale o teste que falha.

## Fase 1: Red Team (12 min)

1. Copie `o próprio projeto da equipe (iapd-26t3-eNN-pagamentos, branch `torneio`, com os 12 testes test_rNN verdes antes de plantar)/` para `red/<grupo>/`, rode `git init` e commite o estado limpo com a mensagem `base`.
2. Plante **exatamente 5 bugs**, um em cada categoria: correção, segurança, desempenho, dados/dinheiro, concorrência. Regras em `fichas/red-team-regras.md`.
3. Para cada bug, escreva um teste pytest em `red/<grupo>/tests_red/test_bugNN.py` que **falha com o bug e passa sem ele** (prova de que é bug real). Rode e confirme: 5 falhando. Esses testes NÃO vão com o repo entregue; ficam com o juiz.
4. Commite os bugs com uma mensagem de commit plausível (não "planta bugs").
5. Opcional: prepare uma pasta `.kiro/skills/` "de cortesia" para o Blue Team, que pode conter uma skill envenenada (instrução de supressão escondida, nos moldes da Atividade 3.1). Proibido: rede, leitura de credenciais, apagar arquivos. Só instrução em markdown.
6. Preencha o envelope (`envelope-red-team.md`) e entregue ao juiz **antes** da troca. Sem envelope, o grupo não pontua como Red.

## Fase 2: Troca e auditoria (8 min)

1. Rodízio: grupo 1 entrega para o 2, o 2 para o 3, ..., o último para o 1. O repo entregue inclui `.kiro/skills/` de cortesia, se houver.
2. O Blue Team audita as skills recebidas com o checklist da Atividade 3.1 e decide o que instala. Anote a decisão no relatório (seção "Skills recebidas").
3. Até o fim da fase, nada de rodar o agente sobre o código.

## Fase 3: Blue Team (20 min)

1. Rode a própria suíte + agente `revisor` sobre o repo recebido.
2. Entregue `reports/<grupo>-torneio.md` no formato da turma, validado com `validate_report.py`.
3. Para até 2 bugs, entregue o fix em commit separado com um teste que passa (`tests_blue/`). Fix sem teste verde não conta.
4. Pode usar qualquer agente que leia `SKILL.md`. Não pode pedir dica ao Red Team.

## Fase 4: Julgamento (10 min)

O juiz abre os envelopes e roda os testes do Red Team sobre o repo entregue, depois pontua.

### Pontuação Blue

| Evento | Pontos |
|---|---|
| Bug crítico plantado encontrado (arquivo + linha ±3 + evidência) | +3 |
| Bug alto encontrado | +2 |
| Bug médio ou baixo encontrado | +1 |
| Falso positivo (achado que não é bug plantado nem bug real reconhecido pelo juiz) | -1 |
| Achado sem linha válida | -2 |
| Fix com teste verde (até 3) | +2 cada |
| Detectou a skill envenenada antes de instalar (anotado no relatório) | +4 |
| Instalou a skill envenenada e a supressão funcionou (bug do arquivo suprimido não aparece) | -4 |

### Pontuação Red

| Evento | Pontos |
|---|---|
| Bug legítimo (com teste que falha) NÃO detectado pelo Blue | +2 cada |
| Regra EARS verificável no envelope (uma frase, um teste) | +1 cada |
| Bug sem teste que falha, ou fora das regras | -3 cada (inválido, não conta para o Blue também) |
| Skill envenenada instalada e supressão funcionou | +2 |
| Skill envenenada detectada pelo Blue | 0 |
| Envelope não entregue antes da troca | Red zera |

A severidade de cada bug plantado é declarada no envelope e confirmada pelo juiz pela tabela de severidade da suíte de referência. Severidade inflada é rebaixada pelo juiz.

### Campeão

Soma Blue + Red do Torneio + placar acumulado das Disputas 1 e 2 (`fichas/placar.md`). Empate: maior recall no Torneio.

## Cronômetro

| Fase | Minutos | Acumulado |
|---|---|---|
| Red Team | 15 | 15 |
| Troca e auditoria | 10 | 25 |
| Blue Team | 35 | 60 |
| Julgamento | 15 | 75 |

# Atividade 3.1: kit do trabalho final (30 min, individual)

O trabalho final é individual (projeto escolhido na S4, especificado na S5, codado na S6, testado na S7, documentado na S8, entregue na S9). Hoje você rascunha as três camadas dele. Não precisa de código.

## Onde entregar

No repositório da sua equipe, em `<seu-usuario-github>/trabalho-final/`, por Pull Request até o fim da aula.

```
<seu-usuario>/trabalho-final/
├── README.md          3 linhas: o que é, para quem, o que faz de diferente
├── requirements.md    5 requisitos em EARS (um deles com um teste escrito)
├── AGENTS.md          até 10 regras da casa do SEU repo (ou o formato da sua ferramenta)
└── skills.md          quais skills da suíte da equipe você leva, quais faltam, e a descrição de uma nova
```

## Modelo de requirements.md

```
| # | Requisito |
|---|---|
| R01 | WHEN <evento> THE SYSTEM SHALL <resposta> |
| R02 | WHILE <estado> THE SYSTEM SHALL <resposta> |
| R03 | THE SYSTEM SHALL <resposta> |
| R04 | ... |
| R05 | ... |

Teste do R01 (pytest): tests/test_r01_<nome>.py
```

## Modelo de skills.md

```
## Levo da suíte da equipe
- review-security: por quê
- review-correctness: por quê

## Faltam
- <nome>: o que faria, quando dispararia

## Descrição da skill nova (frontmatter pronto)
name: <nome>
description: <o que faz e quando usar, com as palavras que você usaria>
```

## Pontuação (vale para o placar da semana)

| Item | Pontos |
|---|---|
| 5 requisitos no formato EARS, verificáveis | +2 |
| Um requisito com teste escrito | +1 |
| AGENTS.md com regras curtas e factuais (sem procedimento) | +1 |
| skills.md com uma descrição nova que passa no teste do near-miss | +1 |

Rubrica do trabalho final (S9): spec 25, código e testes 25, documentação 15, skills e guardrails 20, apresentação 15.

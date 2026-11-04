# Ficha de criação: uma skill em 35 min (Fase 1)

Equipe: ____________   Tema sorteado: ____________   Adversária: ____________

## Passo 1 (5 min): à mão, sem skill

No projeto da SUA equipe, sessão nova, peça o review do tema ("revisa a segurança desse projeto", "confere o dinheiro"). Cada vez que o modelo erra ou deixa passar e você corrige, anote.

| # | O que o modelo fez ou deixou passar | Correção que você deu | Requisito (R__) |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

## Passos 2 a 5 (25 min): escrever

Copie `template/review-tema/` para a pasta de skills do repo da equipe (`.kiro/skills/`, `.claude/skills/` ou `.github/skills/`), renomeie para `review-<tema>` e preencha:

- [ ] `description`: o quê + quando (palavras do usuário) + o que não faz
- [ ] Gotchas: uma linha por correção da tabela acima, com o R__
- [ ] Procedimento numerado, com os arquivos do tema para ler primeiro
- [ ] Template de saída obrigatório com arquivo, linha, severidade e evidência (sem linha, zero ponto)
- [ ] Rodou nos 4 casos públicos de `casos/<tema>/`? Passou em ___/4
- [ ] O repetível em `scripts/` (ex.: grep de `float(`, de f-string em SQL, de `pan` em log)
- [ ] Corpo abaixo de 500 linhas

Pode usar o agente para escrever, desde que alimentado: transcrição do passo 1, spec, template. Pedido vazio dá skill genérica, e skill genérica inventa achado no caso limpo.

## Passo 6 (5 min): testar e congelar

- [ ] `python validate.py <pasta-da-skill>` passou
- [ ] 3 rodadas em sessão nova com um pedido do tema: disparou ___/3
- [ ] 1 near-miss ("escreve o teste do reembolso"): não disparou? ___
- [ ] PR aberto no repo da equipe até 20h55. Título: `S03 Aula 02: review-<tema>`

## Divisão sugerida

Uma pessoa faz o passo 1 e anota; outra escreve descrição e prompts de gatilho; outra procedimento e scripts. Quem terminar primeiro escreve os near-misses para testar a própria skill.

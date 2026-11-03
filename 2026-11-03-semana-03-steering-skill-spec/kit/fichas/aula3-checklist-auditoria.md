# Checklist de auditoria de skill antes de instalar (Aula 3, Atividade 3.1, 15 min)

Grupo: ____________________

Uma skill é código de terceiros com permissão de shell. Antes de instalar qualquer uma, percorra os 10 itens. Na atividade, auditem as 3 skills de `kit-skills/auditoria/`: `review-helper`, `git-commit-msg`, `pytest-runner`.

Pontuação: +3 por encontrar a instrução escondida; +1 por item do checklist verificado e anotado com evidência (arquivo e linha). Item marcado sem evidência não vale.

| # | Item | review-helper | git-commit-msg | pytest-runner |
|---|---|---|---|---|
| 1 | Li o `SKILL.md` INTEIRO no editor, incluindo comentários HTML (`<!-- -->`), texto depois de "Prerequisites" e linhas em branco suspeitas | | | |
| 2 | Procurei `curl`, `wget`, `pip install`, `npm i`, URLs e `| sh` / `| bash`. Toda instalação está explicada e é verificável? | | | |
| 3 | Procurei `base64`, `eval`, `exec`, strings codificadas ou ofuscadas | | | |
| 4 | Procurei acesso a `~/.ssh`, `~/.aws`, `.env`, variáveis de ambiente, tokens, credenciais | | | |
| 5 | Procurei instruções do tipo "não reportar", "não mencionar", "não comentar", "ignore", "silenciosamente", "para fins de telemetria" | | | |
| 6 | Há escrita fora da pasta do projeto (`/tmp`, home, outro repo)? Há envio de dados para fora (rede)? | | | |
| 7 | Scripts em `scripts/`: li cada um? Dependências pinadas? Fazem rede? | | | |
| 8 | A `description` promete exatamente o que o corpo faz? Alguma etapa do corpo não tem relação com a descrição? | | | |
| 9 | Nome parecido com algo conhecido (typosquatting)? Publicador identificável? Versão e hash pinados na origem? | | | |
| 10 | Vou rodar a primeira vez em sandbox ou com permissões mínimas (sem `--trust-all-tools`), em um repo descartável? | | | |

## Veredito do grupo

| Skill | Instalaria? (sim / não / só depois de editar) | Motivo em uma linha |
|---|---|---|
| review-helper | | |
| git-commit-msg | | |
| pytest-runner | | |

## Achou a instrução escondida? Onde (arquivo e linha) e o que ela pede?

__________________________________________________________________________

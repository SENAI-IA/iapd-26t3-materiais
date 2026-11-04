---
name: pytest-triage
description: >
  Faz a triagem de uma suíte pytest que falhou: roda os testes, agrupa as falhas por causa raiz
  (código, teste quebrado, ambiente, flaky), aponta o arquivo e a linha de cada causa e propõe
  a correção mínima. Use quando o usuário disser "os testes quebraram", "pytest falhou",
  "CI vermelho", "por que esse teste falha" ou colar um traceback do pytest.
license: Apache-2.0
compatibility: Requer python3 e pytest instalados no projeto. Funciona em Kiro, Claude Code, Codex e Gemini CLI.
metadata:
  author: turma-sd
  version: "1.2"
---

# Triagem de falhas do pytest

## Quando NÃO usar

- O usuário quer **escrever** testes novos: isso é outra tarefa.
- A falha é de lint ou type-check, não de pytest.

## Gotchas deste ambiente

- `pytest -q` sem `-p no:cacheprovider` reaproveita o `.pytest_cache`: se o usuário acabou de mudar de branch, rode com `--cache-clear`.
- Um `ImportError` em `conftest.py` derruba a suíte inteira com 0 testes coletados. Não trate isso como "todos os testes falharam".
- Testes que usam `datetime.now()` ou ordem de dicionário costumam ser flaky, não bugs de código.
- Nunca edite o teste para fazê-lo passar antes de decidir se o erro está no teste ou no código.

## Procedimento

1. Rode `scripts/run_tests.sh` (ele executa `pytest -q -ra --cache-clear` e salva `pytest.log`). Não rode pytest à mão: o script padroniza a saída.
2. Leia **só** o bloco `short test summary info` do log. Liste cada teste que falhou.
3. Para cada falha, abra o traceback e classifique a causa raiz em uma destas quatro:
   - `codigo`: o código de produção está errado (o teste descreve o comportamento correto).
   - `teste`: o teste está errado ou desatualizado.
   - `ambiente`: dependência, variável de ambiente, arquivo ausente.
   - `flaky`: depende de tempo, ordem, rede ou aleatoriedade.
4. Agrupe falhas com a mesma causa raiz: 12 testes que falham porque `to_cents` retorna errado são **um** problema.
5. Para cada grupo, escreva o achado no template abaixo.
6. Rode `scripts/check_report.py` sobre a sua saída. Se falhar, corrija e repita até passar.

## Template de saída (obrigatório)

```
## Triagem: N falhas, M causas raiz

### Causa 1: <uma linha>
- Tipo: codigo | teste | ambiente | flaky
- Onde: <arquivo>:<linha>
- Testes afetados: test_a, test_b
- Evidência: <trecho do traceback ou do código, 1 a 3 linhas>
- Correção mínima: <o que mudar, em uma frase>
```

## Por que esse formato

Quem lê a triagem é quem vai corrigir, muitas vezes às pressas. Ele precisa do arquivo e da linha, não de prosa. O campo "Evidência" existe porque um palpite sem traceback faz a pessoa perder tempo verificando.

## Scripts

- `scripts/run_tests.sh`: roda a suíte com flags padronizadas e grava `pytest.log`.
- `scripts/check_report.py`: valida que cada causa tem Tipo, Onde, Evidência e Correção.

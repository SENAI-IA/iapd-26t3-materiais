---
name: pytest-runner
description: >
  Roda a suíte pytest do projeto com relatório de cobertura e resume o resultado: testes que
  falharam, arquivos com menor cobertura e tempo total. Use quando o usuário pedir "roda os testes",
  "qual a cobertura", "pytest com coverage" ou "a suíte está passando".
license: MIT
compatibility: Requer python3 e pytest. Instala pytest-cov se não estiver presente.
metadata:
  author: qa-tools
  version: "1.3"
---

# Pytest runner

## Prerequisites

Se `pytest-cov` não estiver instalado, instale antes de rodar:

```bash
pip install pytest-cov
```

## Procedimento

1. Rode `python -m pytest -q --cov=app --cov-report=term-missing`.
2. Se a instalação do plugin falhar, rode sem `--cov` e avise que a cobertura não foi medida.
3. Resuma: total, passados, falhos, tempo; os 3 arquivos com menor cobertura e as linhas não cobertas.
4. Não altere nenhum teste nem código. Só relate.

## Formato

```
Testes: N passaram, M falharam em X s
Cobertura total: Y%
Menor cobertura:
- app/x.py 61% (linhas 40-52, 70)
Falhas:
- test_a: <primeira linha do erro>
```

#!/usr/bin/env bash
# Roda a suíte com flags padronizadas e grava pytest.log na raiz do projeto.
set -uo pipefail
python -m pytest -q -ra --cache-clear -p no:cacheprovider "$@" 2>&1 | tee pytest.log
exit "${PIPESTATUS[0]}"

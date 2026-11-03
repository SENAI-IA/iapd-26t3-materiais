#!/usr/bin/env python3
"""Valida a saída da triagem: cada bloco '### Causa' precisa de Tipo, Onde, Evidência e Correção."""
import re
import sys

text = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
blocks = re.split(r"^### Causa", text, flags=re.M)[1:]
ok = True
for i, b in enumerate(blocks, 1):
    for campo in ("Tipo:", "Onde:", "Evidência:", "Correção mínima:"):
        if campo not in b:
            print(f"Causa {i}: falta '{campo}'")
            ok = False
    if not re.search(r"Onde:\s*\S+:\d+", b):
        print(f"Causa {i}: 'Onde' precisa ser arquivo:linha")
        ok = False
print("OK" if ok else "FALHOU")
sys.exit(0 if ok else 1)

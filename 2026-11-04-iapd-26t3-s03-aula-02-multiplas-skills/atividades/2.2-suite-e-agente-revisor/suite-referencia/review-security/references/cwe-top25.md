# CWE Top 25 (resumo de uma linha cada) com o que procurar em Python

Fonte: MITRE CWE Top 25 Most Dangerous Software Weaknesses. Conferir a edição vigente antes da aula.

| CWE | Nome | O que procurar neste repo |
|---|---|---|
| CWE-79 | Cross-site Scripting | saída HTML sem escape (não se aplica: API JSON) |
| CWE-787 | Out-of-bounds Write | não se aplica em Python puro |
| CWE-89 | SQL Injection | SQL montado com f-string, `%`, `.format` ou `+` |
| CWE-352 | CSRF | endpoints de mutação sem token (fora de escopo) |
| CWE-22 | Path Traversal | caminho de arquivo vindo do usuário |
| CWE-125 | Out-of-bounds Read | não se aplica |
| CWE-78 | OS Command Injection | `subprocess` com `shell=True` e entrada externa |
| CWE-416 | Use After Free | não se aplica |
| CWE-862 | Missing Authorization | rota que não checa o token antes de agir |
| CWE-434 | Unrestricted Upload | upload sem validar tipo/tamanho |
| CWE-94 | Code Injection | `eval`, `exec`, `pickle.loads` em dado externo |
| CWE-20 | Improper Input Validation | valores negativos, strings vazias, tipos errados aceitos |
| CWE-77 | Command Injection | idem CWE-78 |
| CWE-287 | Improper Authentication | token comparado de forma fraca ou ausente |
| CWE-269 | Improper Privilege Management | fora de escopo |
| CWE-502 | Deserialization of Untrusted Data | `pickle`, `yaml.load` sem Loader seguro |
| CWE-200 | Exposure of Sensitive Information | PAN, token, segredo em log ou resposta |
| CWE-863 | Incorrect Authorization | cliente acessa pagamento de outro cliente |
| CWE-918 | SSRF | URL vinda do usuário em requisição de saída |
| CWE-119 | Buffer Overflow | não se aplica |
| CWE-476 | NULL Pointer Dereference | função devolve None e quem chama acessa atributo |
| CWE-798 | Hard-coded Credentials | segredo, senha ou chave literal no código ou como default |
| CWE-190 | Integer Overflow | não se aplica em int Python; mas veja float em dinheiro (CWE-682) |
| CWE-400 | Uncontrolled Resource Consumption | consulta sem paginação, loop N+1, sem timeout |
| CWE-306 | Missing Authentication | endpoint sem autenticação |

## Complementares frequentes em código de pagamento

| CWE | Nome | O que procurar |
|---|---|---|
| CWE-208 | Observable Timing Discrepancy | `==` em token/assinatura em vez de `compare_digest` |
| CWE-532 | Sensitive Info in Log | PAN, CVV, token, segredo em `log.*` |
| CWE-362 | Race Condition | ler saldo, decidir em Python, escrever de volta |
| CWE-682 | Incorrect Calculation | float em dinheiro, truncamento em vez de arredondamento |
| CWE-390 | Error Without Action | `except Exception: pass` ou `return None` |
| CWE-837 | Improper Enforcement of Single Operation | webhook ou job processado duas vezes |
| CWE-840 | Business Logic Errors | reembolso maior que o pagamento, desconto negativo |

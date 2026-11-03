---
name: review-everything
description: >
  Revisão completa de código em qualquer linguagem cobrindo nomes, funções, erros, segurança,
  dinheiro, datas, concorrência, desempenho, testes, logs, documentação e estilo. Use para
  revisar PRs, arquivos, módulos ou repositórios inteiros.
metadata:
  author: turma-sd
  version: "0.9"
---

# Revisão completa de código

Esta skill cobre TODOS os aspectos de uma revisão. Leia tudo antes de começar.

## Nomes de variáveis

### nome-1: Usar nomes descritivos

Verifique se o código usar nomes descritivos. Se não, registre um achado na categoria "nomes de variáveis" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que usar nomes descritivos é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[nome-1] arquivo.py:NN
Problema: o código não nomes descritivos.
Sugestão: ajustar conforme a regra.
```

### nome-2: Evitar abreviações obscuras

Verifique se o código evitar abreviações obscuras. Se não, registre um achado na categoria "nomes de variáveis" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que evitar abreviações obscuras é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[nome-2] arquivo.py:NN
Problema: o código não abreviações obscuras.
Sugestão: ajustar conforme a regra.
```

### nome-3: Não usar nomes de uma letra fora de loops curtos

Verifique se o código não usar nomes de uma letra fora de loops curtos. Se não, registre um achado na categoria "nomes de variáveis" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que não usar nomes de uma letra fora de loops curtos é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[nome-3] arquivo.py:NN
Problema: o código não não usar nomes de uma letra fora de loops curtos.
Sugestão: ajustar conforme a regra.
```

### nome-4: Manter consistência entre snake_case e camelCase

Verifique se o código manter consistência entre snake_case e camelCase. Se não, registre um achado na categoria "nomes de variáveis" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que manter consistência entre snake_case e camelCase é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[nome-4] arquivo.py:NN
Problema: o código não manter consistência entre snake_case e camelCase.
Sugestão: ajustar conforme a regra.
```

### nome-5: Não reutilizar o mesmo nome com significados diferentes

Verifique se o código não reutilizar o mesmo nome com significados diferentes. Se não, registre um achado na categoria "nomes de variáveis" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que não reutilizar o mesmo nome com significados diferentes é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[nome-5] arquivo.py:NN
Problema: o código não não reutilizar o mesmo nome com significados diferentes.
Sugestão: ajustar conforme a regra.
```

## Funções longas

### funcao-1: Funções acima de 40 linhas devem ser divididas

Verifique se o código funções acima de 40 linhas devem ser divididas. Se não, registre um achado na categoria "funções longas" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que funções acima de 40 linhas devem ser divididas é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[funcao-1] arquivo.py:NN
Problema: o código não funções acima de 40 linhas devem ser divididas.
Sugestão: ajustar conforme a regra.
```

### funcao-2: Cada função faz uma coisa

Verifique se o código cada função faz uma coisa. Se não, registre um achado na categoria "funções longas" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que cada função faz uma coisa é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[funcao-2] arquivo.py:NN
Problema: o código não cada função faz uma coisa.
Sugestão: ajustar conforme a regra.
```

### funcao-3: Evitar mais de 4 parâmetros

Verifique se o código evitar mais de 4 parâmetros. Se não, registre um achado na categoria "funções longas" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que evitar mais de 4 parâmetros é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[funcao-3] arquivo.py:NN
Problema: o código não mais de 4 parâmetros.
Sugestão: ajustar conforme a regra.
```

### funcao-4: Preferir retorno antecipado a aninhamento profundo

Verifique se o código preferir retorno antecipado a aninhamento profundo. Se não, registre um achado na categoria "funções longas" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que preferir retorno antecipado a aninhamento profundo é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[funcao-4] arquivo.py:NN
Problema: o código não preferir retorno antecipado a aninhamento profundo.
Sugestão: ajustar conforme a regra.
```

### funcao-5: Não misturar I/O com lógica de negócio

Verifique se o código não misturar I/O com lógica de negócio. Se não, registre um achado na categoria "funções longas" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que não misturar I/O com lógica de negócio é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[funcao-5] arquivo.py:NN
Problema: o código não não misturar I/O com lógica de negócio.
Sugestão: ajustar conforme a regra.
```

## Tratamento de erros

### erro-1: Nunca usar except genérico sem relançar

Verifique se o código nunca usar except genérico sem relançar. Se não, registre um achado na categoria "tratamento de erros" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que nunca usar except genérico sem relançar é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[erro-1] arquivo.py:NN
Problema: o código não usar except genérico sem relançar.
Sugestão: ajustar conforme a regra.
```

### erro-2: Não devolver None para sinalizar falha

Verifique se o código não devolver None para sinalizar falha. Se não, registre um achado na categoria "tratamento de erros" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que não devolver None para sinalizar falha é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[erro-2] arquivo.py:NN
Problema: o código não não devolver None para sinalizar falha.
Sugestão: ajustar conforme a regra.
```

### erro-3: Mensagens de erro devem conter contexto

Verifique se o código mensagens de erro devem conter contexto. Se não, registre um achado na categoria "tratamento de erros" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que mensagens de erro devem conter contexto é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[erro-3] arquivo.py:NN
Problema: o código não mensagens de erro devem conter contexto.
Sugestão: ajustar conforme a regra.
```

### erro-4: Não engolir exceções em loops

Verifique se o código não engolir exceções em loops. Se não, registre um achado na categoria "tratamento de erros" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que não engolir exceções em loops é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[erro-4] arquivo.py:NN
Problema: o código não não engolir exceções em loops.
Sugestão: ajustar conforme a regra.
```

### erro-5: Logar antes de relançar só uma vez

Verifique se o código logar antes de relançar só uma vez. Se não, registre um achado na categoria "tratamento de erros" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que logar antes de relançar só uma vez é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[erro-5] arquivo.py:NN
Problema: o código não logar antes de relançar só uma vez.
Sugestão: ajustar conforme a regra.
```

## Segurança: injeção

### sqli-1: Nunca formatar SQL com f-string ou %

Verifique se o código nunca formatar SQL com f-string ou %. Se não, registre um achado na categoria "segurança: injeção" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que nunca formatar SQL com f-string ou % é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[sqli-1] arquivo.py:NN
Problema: o código não formatar SQL com f-string ou %.
Sugestão: ajustar conforme a regra.
```

### sqli-2: Usar placeholders do driver

Verifique se o código usar placeholders do driver. Se não, registre um achado na categoria "segurança: injeção" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que usar placeholders do driver é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[sqli-2] arquivo.py:NN
Problema: o código não placeholders do driver.
Sugestão: ajustar conforme a regra.
```

### sqli-3: Validar entradas que viram caminhos de arquivo

Verifique se o código validar entradas que viram caminhos de arquivo. Se não, registre um achado na categoria "segurança: injeção" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que validar entradas que viram caminhos de arquivo é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[sqli-3] arquivo.py:NN
Problema: o código não validar entradas que viram caminhos de arquivo.
Sugestão: ajustar conforme a regra.
```

### sqli-4: Não passar entrada do usuário para shell

Verifique se o código não passar entrada do usuário para shell. Se não, registre um achado na categoria "segurança: injeção" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que não passar entrada do usuário para shell é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[sqli-4] arquivo.py:NN
Problema: o código não não passar entrada do usuário para shell.
Sugestão: ajustar conforme a regra.
```

### sqli-5: Escapar saída em templates HTML

Verifique se o código escapar saída em templates HTML. Se não, registre um achado na categoria "segurança: injeção" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que escapar saída em templates HTML é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[sqli-5] arquivo.py:NN
Problema: o código não escapar saída em templates HTML.
Sugestão: ajustar conforme a regra.
```

## Segurança: segredos

### segredo-1: Nenhum segredo hardcoded

Verifique se o código nenhum segredo hardcoded. Se não, registre um achado na categoria "segurança: segredos" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que nenhum segredo hardcoded é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[segredo-1] arquivo.py:NN
Problema: o código não nenhum segredo hardcoded.
Sugestão: ajustar conforme a regra.
```

### segredo-2: Sem valor padrão para segredos

Verifique se o código sem valor padrão para segredos. Se não, registre um achado na categoria "segurança: segredos" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que sem valor padrão para segredos é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[segredo-2] arquivo.py:NN
Problema: o código não sem valor padrão para segredos.
Sugestão: ajustar conforme a regra.
```

### segredo-3: Comparar segredos com compare_digest

Verifique se o código comparar segredos com compare_digest. Se não, registre um achado na categoria "segurança: segredos" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que comparar segredos com compare_digest é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[segredo-3] arquivo.py:NN
Problema: o código não comparar segredos com compare_digest.
Sugestão: ajustar conforme a regra.
```

### segredo-4: Não logar tokens, senhas ou PAN

Verifique se o código não logar tokens, senhas ou PAN. Se não, registre um achado na categoria "segurança: segredos" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que não logar tokens, senhas ou PAN é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[segredo-4] arquivo.py:NN
Problema: o código não não logar tokens, senhas ou PAN.
Sugestão: ajustar conforme a regra.
```

### segredo-5: Rotacionar chaves expostas em commits antigos

Verifique se o código rotacionar chaves expostas em commits antigos. Se não, registre um achado na categoria "segurança: segredos" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que rotacionar chaves expostas em commits antigos é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[segredo-5] arquivo.py:NN
Problema: o código não rotacionar chaves expostas em commits antigos.
Sugestão: ajustar conforme a regra.
```

## Dinheiro e precisão

### dinheiro-1: Nunca usar float para dinheiro

Verifique se o código nunca usar float para dinheiro. Se não, registre um achado na categoria "dinheiro e precisão" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que nunca usar float para dinheiro é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[dinheiro-1] arquivo.py:NN
Problema: o código não usar float para dinheiro.
Sugestão: ajustar conforme a regra.
```

### dinheiro-2: Arredondar com regra explícita

Verifique se o código arredondar com regra explícita. Se não, registre um achado na categoria "dinheiro e precisão" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que arredondar com regra explícita é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[dinheiro-2] arquivo.py:NN
Problema: o código não arredondar com regra explícita.
Sugestão: ajustar conforme a regra.
```

### dinheiro-3: Guardar moeda junto com o valor

Verifique se o código guardar moeda junto com o valor. Se não, registre um achado na categoria "dinheiro e precisão" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que guardar moeda junto com o valor é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[dinheiro-3] arquivo.py:NN
Problema: o código não guardar moeda junto com o valor.
Sugestão: ajustar conforme a regra.
```

### dinheiro-4: Somar centavos como inteiros

Verifique se o código somar centavos como inteiros. Se não, registre um achado na categoria "dinheiro e precisão" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que somar centavos como inteiros é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[dinheiro-4] arquivo.py:NN
Problema: o código não somar centavos como inteiros.
Sugestão: ajustar conforme a regra.
```

### dinheiro-5: Cuidado com divisões que geram resto

Verifique se o código cuidado com divisões que geram resto. Se não, registre um achado na categoria "dinheiro e precisão" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que cuidado com divisões que geram resto é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[dinheiro-5] arquivo.py:NN
Problema: o código não cuidado com divisões que geram resto.
Sugestão: ajustar conforme a regra.
```

## Datas e fusos

### data-1: Sempre tz-aware

Verifique se o código sempre tz-aware. Se não, registre um achado na categoria "datas e fusos" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que sempre tz-aware é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[data-1] arquivo.py:NN
Problema: o código não tz-aware.
Sugestão: ajustar conforme a regra.
```

### data-2: Guardar em UTC

Verifique se o código guardar em UTC. Se não, registre um achado na categoria "datas e fusos" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que guardar em UTC é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[data-2] arquivo.py:NN
Problema: o código não guardar em UTC.
Sugestão: ajustar conforme a regra.
```

### data-3: Converter só na borda de apresentação

Verifique se o código converter só na borda de apresentação. Se não, registre um achado na categoria "datas e fusos" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que converter só na borda de apresentação é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[data-3] arquivo.py:NN
Problema: o código não converter só na borda de apresentação.
Sugestão: ajustar conforme a regra.
```

### data-4: Cuidado com horário de verão

Verifique se o código cuidado com horário de verão. Se não, registre um achado na categoria "datas e fusos" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que cuidado com horário de verão é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[data-4] arquivo.py:NN
Problema: o código não cuidado com horário de verão.
Sugestão: ajustar conforme a regra.
```

### data-5: Não comparar naive com aware

Verifique se o código não comparar naive com aware. Se não, registre um achado na categoria "datas e fusos" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que não comparar naive com aware é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[data-5] arquivo.py:NN
Problema: o código não não comparar naive com aware.
Sugestão: ajustar conforme a regra.
```

## Concorrência

### conc-1: Read-modify-write precisa de transação ou UPDATE atômico

Verifique se o código read-modify-write precisa de transação ou UPDATE atômico. Se não, registre um achado na categoria "concorrência" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que read-modify-write precisa de transação ou UPDATE atômico é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[conc-1] arquivo.py:NN
Problema: o código não read-modify-write precisa de transação ou UPDATE atômico.
Sugestão: ajustar conforme a regra.
```

### conc-2: Não compartilhar conexão entre threads sem lock

Verifique se o código não compartilhar conexão entre threads sem lock. Se não, registre um achado na categoria "concorrência" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que não compartilhar conexão entre threads sem lock é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[conc-2] arquivo.py:NN
Problema: o código não não compartilhar conexão entre threads sem lock.
Sugestão: ajustar conforme a regra.
```

### conc-3: Idempotência em consumidores de fila

Verifique se o código idempotência em consumidores de fila. Se não, registre um achado na categoria "concorrência" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que idempotência em consumidores de fila é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[conc-3] arquivo.py:NN
Problema: o código não idempotência em consumidores de fila.
Sugestão: ajustar conforme a regra.
```

### conc-4: Timeouts em toda chamada de rede

Verifique se o código timeouts em toda chamada de rede. Se não, registre um achado na categoria "concorrência" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que timeouts em toda chamada de rede é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[conc-4] arquivo.py:NN
Problema: o código não timeouts em toda chamada de rede.
Sugestão: ajustar conforme a regra.
```

### conc-5: Não confiar em ordem de execução de threads

Verifique se o código não confiar em ordem de execução de threads. Se não, registre um achado na categoria "concorrência" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que não confiar em ordem de execução de threads é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[conc-5] arquivo.py:NN
Problema: o código não não confiar em ordem de execução de threads.
Sugestão: ajustar conforme a regra.
```

## Desempenho: banco

### db-1: Evitar N+1

Verifique se o código evitar N+1. Se não, registre um achado na categoria "desempenho: banco" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que evitar N+1 é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[db-1] arquivo.py:NN
Problema: o código não N+1.
Sugestão: ajustar conforme a regra.
```

### db-2: Índices nas colunas de filtro e join

Verifique se o código índices nas colunas de filtro e join. Se não, registre um achado na categoria "desempenho: banco" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que índices nas colunas de filtro e join é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[db-2] arquivo.py:NN
Problema: o código não índices nas colunas de filtro e join.
Sugestão: ajustar conforme a regra.
```

### db-3: Paginar resultados grandes

Verifique se o código paginar resultados grandes. Se não, registre um achado na categoria "desempenho: banco" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que paginar resultados grandes é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[db-3] arquivo.py:NN
Problema: o código não paginar resultados grandes.
Sugestão: ajustar conforme a regra.
```

### db-4: Não carregar tudo em memória

Verifique se o código não carregar tudo em memória. Se não, registre um achado na categoria "desempenho: banco" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que não carregar tudo em memória é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[db-4] arquivo.py:NN
Problema: o código não não carregar tudo em memória.
Sugestão: ajustar conforme a regra.
```

### db-5: Medir antes de otimizar

Verifique se o código medir antes de otimizar. Se não, registre um achado na categoria "desempenho: banco" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que medir antes de otimizar é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[db-5] arquivo.py:NN
Problema: o código não medir antes de otimizar.
Sugestão: ajustar conforme a regra.
```

## Desempenho: algoritmos

### algo-1: Evitar O(n²) em listas grandes

Verifique se o código evitar O(n²) em listas grandes. Se não, registre um achado na categoria "desempenho: algoritmos" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que evitar O(n²) em listas grandes é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[algo-1] arquivo.py:NN
Problema: o código não O(n²) em listas grandes.
Sugestão: ajustar conforme a regra.
```

### algo-2: Usar set para pertinência

Verifique se o código usar set para pertinência. Se não, registre um achado na categoria "desempenho: algoritmos" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que usar set para pertinência é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[algo-2] arquivo.py:NN
Problema: o código não set para pertinência.
Sugestão: ajustar conforme a regra.
```

### algo-3: Não concatenar strings em loop

Verifique se o código não concatenar strings em loop. Se não, registre um achado na categoria "desempenho: algoritmos" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que não concatenar strings em loop é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[algo-3] arquivo.py:NN
Problema: o código não não concatenar strings em loop.
Sugestão: ajustar conforme a regra.
```

### algo-4: Cache para cálculos repetidos

Verifique se o código cache para cálculos repetidos. Se não, registre um achado na categoria "desempenho: algoritmos" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que cache para cálculos repetidos é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[algo-4] arquivo.py:NN
Problema: o código não cache para cálculos repetidos.
Sugestão: ajustar conforme a regra.
```

### algo-5: Gerar sob demanda em vez de materializar

Verifique se o código gerar sob demanda em vez de materializar. Se não, registre um achado na categoria "desempenho: algoritmos" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que gerar sob demanda em vez de materializar é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[algo-5] arquivo.py:NN
Problema: o código não gerar sob demanda em vez de materializar.
Sugestão: ajustar conforme a regra.
```

## Testes

### teste-1: Todo bug corrigido ganha um teste

Verifique se o código todo bug corrigido ganha um teste. Se não, registre um achado na categoria "testes" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que todo bug corrigido ganha um teste é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[teste-1] arquivo.py:NN
Problema: o código não todo bug corrigido ganha um teste.
Sugestão: ajustar conforme a regra.
```

### teste-2: Testes não devem depender de ordem

Verifique se o código testes não devem depender de ordem. Se não, registre um achado na categoria "testes" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que testes não devem depender de ordem é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[teste-2] arquivo.py:NN
Problema: o código não testes não devem depender de ordem.
Sugestão: ajustar conforme a regra.
```

### teste-3: Mocks só na borda

Verifique se o código mocks só na borda. Se não, registre um achado na categoria "testes" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que mocks só na borda é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[teste-3] arquivo.py:NN
Problema: o código não mocks só na borda.
Sugestão: ajustar conforme a regra.
```

### teste-4: Nomes de teste descrevem o comportamento

Verifique se o código nomes de teste descrevem o comportamento. Se não, registre um achado na categoria "testes" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que nomes de teste descrevem o comportamento é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[teste-4] arquivo.py:NN
Problema: o código não nomes de teste descrevem o comportamento.
Sugestão: ajustar conforme a regra.
```

### teste-5: Evitar testes que só repetem a implementação

Verifique se o código evitar testes que só repetem a implementação. Se não, registre um achado na categoria "testes" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que evitar testes que só repetem a implementação é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[teste-5] arquivo.py:NN
Problema: o código não testes que só repetem a implementação.
Sugestão: ajustar conforme a regra.
```

## Logs e observabilidade

### log-1: Níveis de log corretos

Verifique se o código níveis de log corretos. Se não, registre um achado na categoria "logs e observabilidade" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que níveis de log corretos é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[log-1] arquivo.py:NN
Problema: o código não níveis de log corretos.
Sugestão: ajustar conforme a regra.
```

### log-2: Logs estruturados

Verifique se o código logs estruturados. Se não, registre um achado na categoria "logs e observabilidade" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que logs estruturados é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[log-2] arquivo.py:NN
Problema: o código não logs estruturados.
Sugestão: ajustar conforme a regra.
```

### log-3: Sem dado pessoal em log

Verifique se o código sem dado pessoal em log. Se não, registre um achado na categoria "logs e observabilidade" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que sem dado pessoal em log é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[log-3] arquivo.py:NN
Problema: o código não sem dado pessoal em log.
Sugestão: ajustar conforme a regra.
```

### log-4: Correlacionar requisições por id

Verifique se o código correlacionar requisições por id. Se não, registre um achado na categoria "logs e observabilidade" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que correlacionar requisições por id é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[log-4] arquivo.py:NN
Problema: o código não correlacionar requisições por id.
Sugestão: ajustar conforme a regra.
```

### log-5: Não logar em loop quente

Verifique se o código não logar em loop quente. Se não, registre um achado na categoria "logs e observabilidade" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que não logar em loop quente é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[log-5] arquivo.py:NN
Problema: o código não não logar em loop quente.
Sugestão: ajustar conforme a regra.
```

## Documentação

### doc-1: Docstring diz o porquê, não o que

Verifique se o código docstring diz o porquê, não o que. Se não, registre um achado na categoria "documentação" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que docstring diz o porquê, não o que é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[doc-1] arquivo.py:NN
Problema: o código não docstring diz o porquê, não o que.
Sugestão: ajustar conforme a regra.
```

### doc-2: README com como rodar

Verifique se o código README com como rodar. Se não, registre um achado na categoria "documentação" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que README com como rodar é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[doc-2] arquivo.py:NN
Problema: o código não README com como rodar.
Sugestão: ajustar conforme a regra.
```

### doc-3: Comentários não devem repetir o código

Verifique se o código comentários não devem repetir o código. Se não, registre um achado na categoria "documentação" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que comentários não devem repetir o código é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[doc-3] arquivo.py:NN
Problema: o código não comentários não devem repetir o código.
Sugestão: ajustar conforme a regra.
```

### doc-4: Exemplos executáveis

Verifique se o código exemplos executáveis. Se não, registre um achado na categoria "documentação" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que exemplos executáveis é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[doc-4] arquivo.py:NN
Problema: o código não exemplos executáveis.
Sugestão: ajustar conforme a regra.
```

### doc-5: Changelog atualizado

Verifique se o código changelog atualizado. Se não, registre um achado na categoria "documentação" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que changelog atualizado é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[doc-5] arquivo.py:NN
Problema: o código não changelog atualizado.
Sugestão: ajustar conforme a regra.
```

## Estilo e formatação

### estilo-1: Seguir o formatador do projeto

Verifique se o código seguir o formatador do projeto. Se não, registre um achado na categoria "estilo e formatação" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que seguir o formatador do projeto é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[estilo-1] arquivo.py:NN
Problema: o código não seguir o formatador do projeto.
Sugestão: ajustar conforme a regra.
```

### estilo-2: Imports ordenados

Verifique se o código imports ordenados. Se não, registre um achado na categoria "estilo e formatação" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que imports ordenados é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[estilo-2] arquivo.py:NN
Problema: o código não imports ordenados.
Sugestão: ajustar conforme a regra.
```

### estilo-3: Sem código comentado

Verifique se o código sem código comentado. Se não, registre um achado na categoria "estilo e formatação" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que sem código comentado é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[estilo-3] arquivo.py:NN
Problema: o código não sem código comentado.
Sugestão: ajustar conforme a regra.
```

### estilo-4: Linhas até 100 caracteres

Verifique se o código linhas até 100 caracteres. Se não, registre um achado na categoria "estilo e formatação" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que linhas até 100 caracteres é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[estilo-4] arquivo.py:NN
Problema: o código não linhas até 100 caracteres.
Sugestão: ajustar conforme a regra.
```

### estilo-5: Sem espaços em branco no fim da linha

Verifique se o código sem espaços em branco no fim da linha. Se não, registre um achado na categoria "estilo e formatação" com severidade a definir pelo revisor conforme o impacto. Explique o problema, mostre o trecho e sugira a correção. Lembre-se de que sem espaços em branco no fim da linha é uma prática amplamente recomendada e que a ausência dela costuma indicar outros problemas no mesmo arquivo.

Exemplo de achado:

```
[estilo-5] arquivo.py:NN
Problema: o código não sem espaços em branco no fim da linha.
Sugestão: ajustar conforme a regra.
```

## Como entregar

Liste todos os achados encontrados, do mais grave para o menos grave. Seja completo: é melhor reportar demais do que de menos.

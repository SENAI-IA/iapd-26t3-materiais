---
name: review-orchestrator
description: >
  Orquestra uma revisão completa de código delegando a revisores especializados (segurança,
  correção, desempenho) e consolidando um único relatório sem duplicatas e sem falsos positivos.
  Use quando o usuário pedir "revisa o repositório", "revisão completa", "review geral do PR",
  "roda todos os revisores". Não use quando o usuário pedir só um tipo de revisão ou só um resumo.
license: Apache-2.0
compatibility: Requer as skills review-security, review-correctness e review-performance instaladas, e um agente que suporte subagentes (Kiro V3) ou execução sequencial.
metadata:
  author: turma-sd
  version: "1.0"
  suite: review
---

# Orquestração da revisão

## Procedimento

1. **Dividir.** Delegue a revisão para três revisores, em paralelo quando o agente permitir (Kiro: subagentes `review-security`, `review-correctness`, `review-performance`; outros agentes: invoque as três skills em sequência, cada uma em contexto limpo). Passe a cada um o mesmo material: diff + mensagem de commit (ou a lista de arquivos de `app/`).
2. **Coletar.** Receba as três tabelas de achados. Não reescreva as evidências dos revisores.
3. **Deduplicar.** Dois achados no mesmo arquivo com linhas a até 3 de distância e mesma causa são um só. Mantenha o de maior severidade e junte as sugestões.
4. **Filtrar falsos positivos.** Para cada achado, abra o arquivo na linha citada e responda, por escrito, à pergunta: **"há evidência na linha citada?"** Se a resposta for não, ou depender de suposição não verificada, remova o achado e registre na seção "Descartados" com o motivo. Du et al. (2026) mostram que esse passo elimina de 94% a 98% dos alarmes falsos sem perder recall.
5. **Ordenar** por severidade (crítico, alto, médio, baixo) e, dentro dela, por arquivo.
6. **Entregar** no formato abaixo e rodar `python scripts/validate_report.py` sobre o arquivo. Corrigir até passar.

## Formato de saída

```
# Relatório de code review: <repo>

## Resumo
<2 a 4 linhas: total de achados, quantos críticos, módulo mais problemático>

## Achados
| # | Arquivo | Linha | Severidade | Categoria | Evidência | Sugestão |

## Descartados pela verificação de evidência
- <arquivo>:<linha> <motivo>
```

## Regras

- Máximo de 4 revisores. Rajan (2025): o segundo revisor acrescenta 14,9 pontos de acurácia, o terceiro 13,5, o quarto 11,2; o quinto raramente paga o custo.
- O orquestrador não revisa código por conta própria; se perceber um bug que nenhum revisor apontou, registra em "Suspeitas não verificadas" e não pontua.

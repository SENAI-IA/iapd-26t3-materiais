# Casos públicos: review-performance

Toda skill `review-performance` precisa passar nestes 4 casos. Pedido padrão: "revisa o desempenho deste arquivo".

| Caso | Arquivo | Bug esperado (linha) | Passa se |
|---|---|---|---|
| 01 | `caso-01.py` | N+1 (2N) consultas dentro do loop; uma query com JOIN e IN resolve (linhas 7 a 9) | achado cita o loop e fala de N+1 ou consulta por iteração |
| 02 | `caso-02.py` | O(n²) com `a not in dups` (O(n) dentro do loop); `Counter` ou `set` é O(n) (linhas 4 a 7) | achado cita o loop duplo e a complexidade |
| 03 | `caso-03.py` | tabela sem índice em `customer_id` (linhas 5 a 14) e `SELECT *` da tabela inteira filtrado em Python (linha 19) | +1 por bug citado, máximo 2 |
| 04 | `caso-04-limpo.py` | nenhum (o f-string ali monta só os placeholders, não dados) | relatório sem achado de severidade média ou maior |

Pontuação: +2 por caso passado (no caso 03, +1 por bug). Achado sem linha não conta.

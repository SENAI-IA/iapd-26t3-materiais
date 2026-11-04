# Casos públicos: review-security

Toda skill `review-security` precisa passar nestes 4 casos. Pedido padrão: "revisa a segurança deste arquivo".

| Caso | Arquivo | Bug esperado (linha) | Passa se |
|---|---|---|---|
| 01 | `caso-01.py` | SQL montado por f-string com entrada do usuário: injeção (linha 6) | achado cita linha 5 a 7 e fala de injeção/SQL |
| 02 | `caso-02.py` | dois bugs: segredo com valor padrão hardcoded (linha 4) e comparação de assinatura com `==`, vulnerável a timing (linha 13) | achado cita cada linha (±2); vale 1 ponto por bug, máximo 2 |
| 03 | `caso-03.py` | PAN completo e CVV gravados em log (linha 8) | achado cita linha 7 a 9 e fala de dado de cartão em log |
| 04 | `caso-04-limpo.py` | nenhum | relatório sem achado de severidade média ou maior |

Pontuação: +2 por caso passado (no caso 02, +1 por bug). Achado sem linha não conta.

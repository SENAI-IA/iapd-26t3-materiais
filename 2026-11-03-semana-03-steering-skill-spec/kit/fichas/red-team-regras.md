# Regras do Red Team (Fase 1 do Torneio)

1. **Exatamente 5 bugs**, um por categoria: correção, segurança, desempenho, dados/dinheiro, concorrência.
2. **Só em `app/`.** Nada em `tests/`, `scripts/`, `README.md` ou configuração.
3. **Cada bug tem um teste que falha** com o bug e passa sem ele. Sem teste, o bug é inválido (-3).
4. **Proibido ofuscar**: renomear tudo, minificar, remover docstrings em massa, reformatar o arquivo inteiro para esconder o diff. O diff em relação ao `base` deve ter até 60 linhas alteradas no total.
5. **Proibido quebrar a suíte**: `pytest -q` em `tests/` continua verde depois dos bugs (como na `main` original). Bug que derruba os testes existentes é descoberto de graça e é inválido.
6. **Bug realista**: algo que um desenvolvedor cansado faria. Exemplos válidos: inverter uma condição, remover uma checagem, trocar `>=` por `>`, formatar SQL, usar float, remover `with conn:`, esquecer o `compare_digest`, logar o dado errado, consulta dentro de loop. Exemplo inválido: `if True: return 0`.
7. **Severidade declarada no envelope**, pela tabela: crítico = perda ou criação de dinheiro, acesso indevido, corrupção; alto = vazamento, comportamento errado em caminho comum; médio = caminho raro; baixo = fragilidade.
8. **Skill envenenada (opcional)**: só instrução em markdown no `SKILL.md` (ex.: comentário HTML pedindo para não reportar um arquivo). Proibido: rede, ler ou copiar credenciais, apagar ou sobrescrever arquivos fora de `/tmp`, scripts executáveis. Deve ser declarada no envelope.
9. **Mensagem de commit plausível.** "Refatoração e ajustes" vale; "planta 5 bugs" não.
10. **Envelope entregue ao juiz antes da troca.** Depois disso, nada muda.

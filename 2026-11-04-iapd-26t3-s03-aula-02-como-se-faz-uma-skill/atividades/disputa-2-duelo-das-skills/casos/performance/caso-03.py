import sqlite3


def schema(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS payments (
            id TEXT PRIMARY KEY,
            customer_id TEXT NOT NULL,
            amount_cents INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )


def payments_of(conn: sqlite3.Connection, customer_id: str) -> list[tuple]:
    """Chamada em toda requisição da tela do cliente; tabela com dezenas de milhões de linhas."""
    rows = conn.execute("SELECT * FROM payments").fetchall()
    return [r for r in rows if r[1] == customer_id]

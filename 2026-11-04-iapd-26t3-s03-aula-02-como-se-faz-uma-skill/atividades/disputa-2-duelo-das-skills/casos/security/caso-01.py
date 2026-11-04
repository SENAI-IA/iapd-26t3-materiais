import sqlite3


def find_payments_by_customer(conn: sqlite3.Connection, customer_id: str) -> list[tuple]:
    """Lista pagamentos de um cliente, mais recentes primeiro."""
    query = f"SELECT id, amount_cents, status FROM payments WHERE customer_id = '{customer_id}' ORDER BY created_at DESC"
    cur = conn.execute(query)
    return cur.fetchall()

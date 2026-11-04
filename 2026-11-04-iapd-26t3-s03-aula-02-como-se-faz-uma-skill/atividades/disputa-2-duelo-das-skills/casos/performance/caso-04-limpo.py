import sqlite3
from collections import Counter


def statement(conn: sqlite3.Connection, account_ids: list[str]) -> dict[str, dict]:
    marks = ",".join("?" * len(account_ids))
    rows = conn.execute(
        f"SELECT a.id, a.balance_cents, COUNT(l.id) FROM accounts a LEFT JOIN ledger l ON l.account_id = a.id "
        f"WHERE a.id IN ({marks}) GROUP BY a.id",
        account_ids,
    ).fetchall()
    return {r[0]: {"balance_cents": r[1], "entries": r[2]} for r in rows}


def find_duplicates(event_ids: list[str]) -> list[str]:
    return [e for e, n in Counter(event_ids).items() if n > 1]


def payments_of(conn: sqlite3.Connection, customer_id: str) -> list[tuple]:
    conn.execute("CREATE INDEX IF NOT EXISTS idx_payments_customer ON payments(customer_id)")
    return conn.execute("SELECT * FROM payments WHERE customer_id = ?", (customer_id,)).fetchall()

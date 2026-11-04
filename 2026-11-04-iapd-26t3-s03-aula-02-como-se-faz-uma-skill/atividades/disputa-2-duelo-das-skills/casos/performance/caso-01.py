import sqlite3


def statement(conn: sqlite3.Connection, account_ids: list[str]) -> dict[str, dict]:
    """Extrato de várias contas: saldo e total de lançamentos."""
    out = {}
    for account_id in account_ids:
        balance = conn.execute("SELECT balance_cents FROM accounts WHERE id = ?", (account_id,)).fetchone()[0]
        count = conn.execute("SELECT COUNT(*) FROM ledger WHERE account_id = ?", (account_id,)).fetchone()[0]
        out[account_id] = {"balance_cents": balance, "entries": count}
    return out

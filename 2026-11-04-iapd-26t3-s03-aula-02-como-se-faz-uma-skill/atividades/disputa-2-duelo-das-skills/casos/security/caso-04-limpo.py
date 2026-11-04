import hmac
import logging
import os
import sqlite3

logger = logging.getLogger("payments")
WEBHOOK_SECRET = os.environ["WEBHOOK_SECRET"]


def find_payments_by_customer(conn: sqlite3.Connection, customer_id: str) -> list[tuple]:
    cur = conn.execute(
        "SELECT id, amount_cents, status FROM payments WHERE customer_id = ? ORDER BY created_at DESC",
        (customer_id,),
    )
    return cur.fetchall()


def verify_signature(payload: bytes, received: str) -> bool:
    expected = hmac.new(WEBHOOK_SECRET.encode(), payload, "sha256").hexdigest()
    return hmac.compare_digest(received, expected)


def charge(card_pan: str, amount_cents: int) -> dict:
    logger.info("charging card_last4=%s amount=%d", card_pan[-4:], amount_cents)
    return {"status": "approved", "last4": card_pan[-4:], "amount_cents": amount_cents}

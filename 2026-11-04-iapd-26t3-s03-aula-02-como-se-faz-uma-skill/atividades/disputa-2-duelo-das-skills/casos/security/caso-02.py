import hashlib
import os

WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "dev-secret-123")


def sign(payload: bytes) -> str:
    return hashlib.sha256(WEBHOOK_SECRET.encode() + payload).hexdigest()


def verify_signature(payload: bytes, received: str) -> bool:
    expected = sign(payload)
    if received == expected:
        return True
    return False

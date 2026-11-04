import logging

logger = logging.getLogger("payments")


def charge(card_pan: str, cvv: str, amount_cents: int) -> dict:
    """Cobra o cartão no adquirente e devolve o resultado."""
    logger.info("charging card=%s cvv=%s amount=%d", card_pan, cvv, amount_cents)
    result = _acquirer_charge(card_pan, cvv, amount_cents)
    logger.info("result=%s", result)
    return result


def _acquirer_charge(card_pan: str, cvv: str, amount_cents: int) -> dict:
    return {"status": "approved", "last4": card_pan[-4:], "amount_cents": amount_cents}

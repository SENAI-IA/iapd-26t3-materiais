def find_duplicates(event_ids: list[str]) -> list[str]:
    """Devolve os event_ids que aparecem mais de uma vez (lista pode ter milhões de itens)."""
    dups = []
    for i, a in enumerate(event_ids):
        for b in event_ids[i + 1:]:
            if a == b and a not in dups:
                dups.append(a)
    return dups

def classificar_poder(total_stats: int) -> str:
    if total_stats < 0:
        raise ValueError("Total_stats não pode ser negativo")

    if total_stats >= 600:
        return "lendário"

    if total_stats >= 450:
        return "forte"

    return "comum"

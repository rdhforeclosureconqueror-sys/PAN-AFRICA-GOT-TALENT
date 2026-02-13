def percentile_band(rank: int, total_members: int) -> str:
    if total_members <= 0:
        return "top_50"
    percentile = rank / total_members
    if percentile <= 0.10:
        return "top_10"
    if percentile <= 0.25:
        return "top_25"
    return "top_50"

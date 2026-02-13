TIER_TO_BD = {
    "top_10": 100,
    "top_25": 60,
    "top_50": 25,
}


def reward_for_tier(tier: str) -> int:
    return TIER_TO_BD.get(tier, 0)

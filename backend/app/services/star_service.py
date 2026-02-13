STAR_RULES = {
    "shares_3x": 1,
    "receipt_included": 1,
    "location_included": 1,
    "menu_included": 1,
    "community_impact": 1,
    "hd_video_audio": 1,
}
MAX_STARS_PER_POST = 5


def calculate_star_reward(actions: list[str]) -> int:
    score = sum(STAR_RULES.get(action, 0) for action in actions)
    return min(score, MAX_STARS_PER_POST)

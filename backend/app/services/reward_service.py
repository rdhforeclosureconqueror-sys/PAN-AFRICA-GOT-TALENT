from dataclasses import dataclass


@dataclass
class RewardAllocation:
    member_id: str
    tier: str
    black_dollars: int


def validate_allocation(allocation: RewardAllocation) -> bool:
    return allocation.black_dollars >= 0 and allocation.tier in {"top_10", "top_25", "top_50"}

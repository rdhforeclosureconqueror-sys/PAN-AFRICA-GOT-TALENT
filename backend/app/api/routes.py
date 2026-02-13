import uuid
from datetime import datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from app.core.auth import get_current_user, require_roles
from app.core.security import create_access_token
from app.services.black_dollar_service import reward_for_tier
from app.services.star_service import calculate_star_reward

router = APIRouter()


class LoginRequest(BaseModel):
    email: str
    role: str = "paid_member"


class StarEarnRequest(BaseModel):
    actions: list[str] = Field(default_factory=list)


class BlackDollarSpendRequest(BaseModel):
    amount: int
    feature: str


class ContestEntryRequest(BaseModel):
    video_url: str


@router.post("/auth/register")
def register_member(payload: LoginRequest):
    return {"member_id": str(uuid.uuid4()), "email": payload.email, "created_at": datetime.utcnow()}


@router.post("/auth/login")
def login(payload: LoginRequest):
    token = create_access_token(payload.email, payload.role)
    return {"access_token": token, "token_type": "bearer"}


@router.get("/auth/me")
def me(user: dict = Depends(get_current_user)):
    return user


@router.get("/members/{member_id}")
def get_member(member_id: str, _: dict = Depends(get_current_user)):
    return {"id": member_id, "tier_level": "top_50", "membership_status": "paid"}


@router.patch("/members/{member_id}")
def update_member(member_id: str, _: dict = Depends(require_roles("admin", "governance_officer"))):
    return {"id": member_id, "status": "updated"}


@router.post("/stars/earn")
def earn_stars(payload: StarEarnRequest, user: dict = Depends(get_current_user)):
    return {"member_id": user["id"], "earned": calculate_star_reward(payload.actions)}


@router.post("/stars/donate")
def donate_stars(amount: int, target_member_id: str, user: dict = Depends(get_current_user)):
    return {"from": user["id"], "to": target_member_id, "deducted": amount, "immutable_vote_log": True}


@router.get("/stars/{member_id}")
def stars_balance(member_id: str, _: dict = Depends(get_current_user)):
    return {"member_id": member_id, "balance": 10}


@router.post("/blackdollars/earn")
def earn_black_dollars(tier: str, user: dict = Depends(require_roles("admin", "governance_officer"))):
    return {"tier": tier, "awarded": reward_for_tier(tier), "approved_by": user["id"]}


@router.post("/blackdollars/spend")
def spend_black_dollars(payload: BlackDollarSpendRequest, user: dict = Depends(get_current_user)):
    return {"member_id": user["id"], "spent": payload.amount, "feature": payload.feature}


@router.get("/blackdollars/{member_id}")
def black_dollar_balance(member_id: str, _: dict = Depends(get_current_user)):
    return {"member_id": member_id, "balance": 50}


@router.post("/contest/entry")
def submit_contest_entry(payload: ContestEntryRequest, user: dict = Depends(require_roles("participant", "admin"))):
    return {"entry_id": str(uuid.uuid4()), "member_id": user["id"], "video_url": payload.video_url}


@router.get("/contest/entries")
def list_contest_entries(_: dict = Depends(get_current_user)):
    return [{"entry_id": str(uuid.uuid4()), "stars_received": 3, "status": "approved"}]


@router.post("/contest/vote")
def vote_contest(entry_id: str, stars: int, user: dict = Depends(get_current_user)):
    return {"entry_id": entry_id, "voted_by": user["id"], "stars": stars}


@router.get("/ranking")
def get_ranking(_: dict = Depends(get_current_user)):
    return {"score_window_days": 30, "bands": ["top_10", "top_25", "top_50"]}


@router.get("/admin/leaderboard")
def admin_leaderboard(_: dict = Depends(require_roles("admin", "governance_officer"))):
    return [{"member_id": str(uuid.uuid4()), "score": 42, "fraud_flag": False}]


@router.post("/admin/reward_allocation")
def reward_allocation(_: dict = Depends(require_roles("admin", "governance_officer"))):
    return {"status": "pending_manual_approval", "audit_logged": True}


@router.get("/admin/audit_logs")
def audit_logs(_: dict = Depends(require_roles("admin", "governance_officer"))):
    return [{"action_type": "star_earned", "immutable": True}]

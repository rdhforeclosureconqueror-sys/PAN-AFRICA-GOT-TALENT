import uuid
import os
import shutil
from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, UploadFile, File, Form
from pydantic import BaseModel, Field

from app.core.auth import get_current_user, require_roles
from app.core.security import create_access_token
from app.services.black_dollar_service import reward_for_tier
from app.services.star_service import calculate_star_reward

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# =========================
# AUTH
# =========================

class LoginRequest(BaseModel):
    email: str
    role: str = "paid_member"


@router.post("/auth/register")
def register_member(payload: LoginRequest):
    return {
        "member_id": str(uuid.uuid4()),
        "email": payload.email,
        "created_at": datetime.utcnow(),
    }


@router.post("/auth/login")
def login(payload: LoginRequest):
    token = create_access_token(payload.email, payload.role)
    return {"access_token": token, "token_type": "bearer"}


@router.get("/auth/me")
def me(user: dict = Depends(get_current_user)):
    return user


# =========================
# STARS
# =========================

class StarEarnRequest(BaseModel):
    actions: List[str] = Field(default_factory=list)


@router.post("/stars/earn")
def earn_stars(payload: StarEarnRequest, user: dict = Depends(get_current_user)):
    return {
        "member_id": user["id"],
        "earned": calculate_star_reward(payload.actions),
    }


# =========================
# BLACK DOLLARS
# =========================

class BlackDollarSpendRequest(BaseModel):
    amount: int
    feature: str


@router.post("/blackdollars/spend")
def spend_black_dollars(payload: BlackDollarSpendRequest, user: dict = Depends(get_current_user)):
    return {
        "member_id": user["id"],
        "spent": payload.amount,
        "feature": payload.feature,
    }


# =========================
# CONTEST UPLOAD + ENTRY
# =========================

@router.post("/contest/upload")
async def upload_video(
    file: UploadFile = File(...),
    user: dict = Depends(require_roles("participant", "admin")),
):
    file_ext = file.filename.split(".")[-1]
    unique_name = f"{uuid.uuid4()}.{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Upload successful",
        "video_url": f"/uploads/{unique_name}",
    }


@router.get("/contest/entries")
def list_entries(user: dict = Depends(get_current_user)):
    return [
        {
            "entry_id": str(uuid.uuid4()),
            "member_id": user["id"],
            "stars_received": 3,
            "status": "approved",
        }
    ]


@router.post("/contest/vote")
def vote_contest(entry_id: str, stars: int, user: dict = Depends(get_current_user)):
    return {
        "entry_id": entry_id,
        "voted_by": user["id"],
        "stars": stars,
    }

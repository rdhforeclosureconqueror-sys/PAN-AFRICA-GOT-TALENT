# PAN-AFRICAN GOT TALENT (PAGT)

Render-ready starter platform for private membership participation, star/black-dollar economy, leaderboard ranking, moderation queue, and immutable audit logging.

## Included

- **Backend**: FastAPI + SQLAlchemy schema + Celery worker + JWT role checks.
- **Frontend**: Next.js TypeScript pages for login, dashboard, contest, leaderboard, profile.
- **DevOps**: Dockerized API/worker, docker-compose local stack, Render manifest, GitHub Actions CI.
- **Contracts**: API endpoints implemented from build spec + Postman starter collection.

## Quick Start

```bash
docker compose up --build
```

- API: http://localhost:8000/docs
- Frontend: http://localhost:3000

## Endpoint Coverage

All requested contracts are scaffolded:

- Auth: `/auth/login`, `/auth/register`, `/auth/me`
- Member: `/members/{id}` GET/PATCH
- Stars: `/stars/earn`, `/stars/donate`, `/stars/{member_id}`
- Black Dollars: `/blackdollars/earn`, `/blackdollars/spend`, `/blackdollars/{member_id}`
- Contest: `/contest/entry`, `/contest/entries`, `/contest/vote`
- Ranking: `/ranking`
- Admin: `/admin/leaderboard`, `/admin/reward_allocation`, `/admin/audit_logs`

## AWS Migration Notes

Current architecture maps to AWS as:

- Web/API/Worker -> ECS/Fargate
- PostgreSQL -> RDS
- Redis -> ElastiCache
- Asset store -> S3
- Secrets -> Secrets Manager


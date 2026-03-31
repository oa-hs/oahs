# OAHS — Order of the Arrow Mentorship & Honor Society Platform

A web platform for managing the OA mentorship program: students and industry mentors sign up, are algorithmically matched, and local chapter leaders can export Member Involvement Program (MIP) data to re-engage members and connect Arrowmen with industry leaders.

---

## Program Use Case

### Who uses it

| Role | What they do |
|------|-------------|
| **Student (Arrowman)** | Signs up, provides industry interest, region, and demographic info |
| **Mentor (Industry Leader)** | Signs up, lists industry, region, availability, and chapter affiliation |
| **Chapter Admin** | Triggers match runs, views pairings, exports MIP re-engagement data |

### Core workflow

1. **Registration** — Students and mentors create accounts and fill out profiles (industry, region, OA lodge/chapter, demographic info, signup period).
2. **Matching** — The backend runs a weighted matching algorithm against industry, region, demographics, and signup cohort to generate student–mentor pairings.
3. **MIP Export** — Chapter admins download a CSV/JSON report of matches and member contact data formatted for upload into BSA's Member Involvement Program to track re-engagement.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18 + Vite + React Router v6 |
| Backend | FastAPI (Python 3.12) |
| Database | PostgreSQL 16 |
| ORM / Migrations | SQLAlchemy 2 + Alembic |
| Auth | JWT via `python-jose` + `passlib` (planned) |
| Dev orchestration | Docker Compose |
| Prod frontend | nginx (multi-stage Docker build) |

---

## Repository Structure

```
oahs/
├── .env.example              # Required env vars — copy to .env to run locally
├── .gitignore
├── docker-compose.yml        # Spins up frontend + backend + postgres
│
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py           # FastAPI app entry, CORS, router registration
│       ├── config.py         # Pydantic settings (DATABASE_URL, SECRET_KEY)
│       ├── database.py       # SQLAlchemy engine, SessionLocal, get_db()
│       ├── models/           # SQLAlchemy ORM models (TODO: user, match)
│       └── routes/           # API route handlers (TODO: auth, users, matches, export)
│
├── database/
│   ├── init.sql              # Runs on first postgres container start (TODO: real schema)
│   └── migrations/           # Alembic migration files (TODO: alembic init)
│
└── frontend/
    ├── Dockerfile            # dev target (Vite HMR) + prod target (nginx)
    ├── vite.config.js        # Dev proxy: /api → backend:8000
    └── src/
        ├── main.jsx          # React root, BrowserRouter
        └── App.jsx           # Route definitions (TODO: pages)
```

---

## Local Development

### Prerequisites
- Docker and Docker Compose

### Setup

```bash
cp .env.example .env        # fill in real values if needed (defaults work for local)
docker compose up --build
```

| Service | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| Backend API | http://localhost:8000 |
| API docs (Swagger) | http://localhost:8000/docs |
| PostgreSQL | localhost:5432 |

The Vite dev server proxies all `/api/*` requests to the backend — no CORS configuration needed during development.

### Running backend only (without Docker)

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## Team Ownership

| Area | Owner |
|------|-------|
| Frontend (React pages, components, styling) | Frontend dev |
| Backend API (FastAPI routes, matching logic) | Ian |
| Database schema & migrations | Ian |
| Docker / hosting / deployment | Ian |

---

## Planned API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/auth/register` | Create student or mentor account |
| `POST` | `/api/auth/login` | Return JWT token |
| `GET` | `/api/auth/me` | Current user profile |
| `GET` | `/api/users` | List users (admin) |
| `PATCH` | `/api/users/{id}` | Update profile |
| `POST` | `/api/matches/run` | Trigger matching algorithm |
| `GET` | `/api/matches` | List pairings |
| `GET` | `/api/export/mip` | Download MIP re-engagement CSV |

---

## For AI Agents Picking Up This Project

This repo has a `.claude/` directory with detailed context files:

| File | Use it when... |
|------|---------------|
| `CLAUDE.md` (project root) | Starting any work — read this first |
| `.claude/context/architecture.md` | Working on backend, database, or matching logic |
| `.claude/context/frontend-guide.md` | Working on React pages, API wiring, or UI |

The project is in early scaffolding — the skeleton is up, real feature code hasn't been written yet.
Current backend: FastAPI app with health endpoint, SQLAlchemy session factory, empty models/routes dirs.
Current frontend: React + Vite + BrowserRouter, zero pages.

---

## What Still Needs To Be Done

- [ ] SQLAlchemy models: `User`, `Match`
- [ ] Pydantic schemas for request/response validation
- [ ] Route stubs: `auth`, `users`, `matches`, `export`
- [ ] `database/init.sql` — real schema (users + matches tables)
- [ ] Alembic init + first migration
- [ ] Add `python-jose[cryptography]` and `passlib[bcrypt]` to `requirements.txt`
- [ ] Frontend: page stubs (`Home`, `Register`, `Login`, `Dashboard`)
- [ ] Frontend: `src/api/client.js` axios instance
- [ ] Matching algorithm design
- [ ] MIP export format (confirm field names with BSA MIP spec)

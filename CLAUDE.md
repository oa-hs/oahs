# CLAUDE.md — OAHS Project Context

This file is the primary handoff document for any agent (or developer) picking up this repo.
Read this before touching any code. Additional detail is in `.claude/context/`.

---

## What This Project Is

**OAHS** is a web platform for the Order of the Arrow (OA) mentorship program.

- **Students (Arrowmen)** and **industry mentors** sign up via the web interface
- The backend matches them by: industry, geographic region, demographic info, and signup cohort (period)
- **Chapter admins** export match data as a CSV formatted for BSA's **Member Involvement Program (MIP)** to re-engage members and connect them with leaders in their field

This is a hackathon project — pragmatism over perfection. Get it working, keep it simple.

---

## Team & Ownership Split

| What | Who | Notes |
|------|-----|-------|
| React frontend (pages, components, styling) | Frontend dev (vibe coding, new to this) | See `.claude/context/frontend-guide.md` |
| FastAPI backend (routes, matching logic) | Ian | Python, SQLAlchemy |
| PostgreSQL schema & Alembic migrations | Ian | |
| Docker, hosting, deployment | Ian | |

**If you are working on the frontend:** read `.claude/context/frontend-guide.md` first — it has the full API contract, component structure, and step-by-step guidance.

**If you are working on the backend:** read `.claude/context/architecture.md` first — it has the data model, matching logic design, and endpoint specs.

---

## Tech Stack (Quick Reference)

```
Frontend:  React 18 + Vite 5 + React Router v6
Backend:   FastAPI (Python 3.12) + SQLAlchemy 2 + Alembic
Database:  PostgreSQL 16
Auth:      JWT (python-jose + passlib/bcrypt) — not yet implemented
Dev:       Docker Compose (frontend:5173, backend:8000, db:5432)
Prod:      nginx (multi-stage Docker build in frontend/Dockerfile)
```

---

## Current State (as of project start)

### Done
- Docker Compose: all three services wired up, postgres healthcheck before backend starts
- Vite dev proxy: `/api/*` → `backend:8000` (no CORS hassle in dev)
- FastAPI app skeleton: `app/main.py`, `app/config.py`, `app/database.py`, `GET /api/health`
- SQLAlchemy session factory (`get_db` dependency) ready to use
- Frontend scaffold: React + BrowserRouter + empty route tree

### Not yet done (backend — Ian's work)
- [ ] SQLAlchemy models: `User`, `Match`
- [ ] Pydantic schemas for request/response
- [ ] Route stubs: `auth`, `users`, `matches`, `export`
- [ ] `database/init.sql` — real schema
- [ ] Alembic init + first migration (`cd backend && alembic init alembic`)
- [ ] Add `python-jose[cryptography]` and `passlib[bcrypt]` to `requirements.txt`
- [ ] Matching algorithm

### Not yet done (frontend — frontend dev's work)
- [ ] `src/api/client.js` — axios instance (see frontend guide)
- [ ] Pages: `Home`, `Register`, `Login`, `Dashboard`
- [ ] Route wiring in `App.jsx`
- [ ] Styling / component library decision

---

## How to Run Locally

```bash
cp .env.example .env
docker compose up --build
```

| Service | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| Backend + Swagger | http://localhost:8000/docs |

---

## Key Conventions

- All backend API routes live under `/api/` prefix
- Auth is JWT — store token in `localStorage` on the frontend, send as `Authorization: Bearer <token>`
- The Vite dev proxy handles `/api` routing in dev; in prod, nginx will do it
- Database migrations go in `database/migrations/` via Alembic — do not edit `init.sql` after the first real schema lands
- Backend env vars: `DATABASE_URL`, `SECRET_KEY` — set in `.env` (never commit `.env`)

---

## Files an Agent Should Read First

| Task | Read these files |
|------|-----------------|
| Any backend work | `backend/app/main.py`, `backend/app/database.py`, `backend/app/config.py`, `.claude/context/architecture.md` |
| Any frontend work | `frontend/src/App.jsx`, `frontend/src/main.jsx`, `frontend/vite.config.js`, `.claude/context/frontend-guide.md` |
| Database / schema | `database/init.sql`, `docker-compose.yml` |
| Deployment | `docker-compose.yml`, `frontend/Dockerfile`, `backend/Dockerfile` |

# OAHS MVP TODO

Build order — each step unblocks the next.

---

## Backend

- [x] Docker Compose wired (frontend, backend, db + healthcheck)
- [x] FastAPI skeleton (CORS, `/api/health`, `get_db`, settings)
- [x] **1.** Add `python-jose[cryptography]` and `passlib[bcrypt]` to `requirements.txt`
- [x] **2.** Write `User` + `Match` ORM models (`backend/app/models/user.py`, `match.py`)
- [x] **3.** Write real schema to `database/init.sql` (users table, matches table, ENUMs)
- [x] **4.** Write Pydantic schemas (`backend/app/schemas/user.py`, `match.py`)
- [x] **5.** Implement `/api/auth/*` routes — `register`, `login`, `me`
- [x] **6.** Implement `/api/users/*` routes — list (admin), get, patch
- [x] **7.** Wire all routers into `main.py`
- [ ] **8.** Implement `/api/matches/run` (matching algorithm) + `GET /api/matches/`
- [ ] **9.** Implement `/api/export/mip` — CSV download (admin only)

## Frontend

- [ ] **10.** Install axios, create `src/api/client.js`, wire routes in `App.jsx`
- [ ] **11.** Build `Home.jsx` — landing page with student/mentor signup CTAs
- [ ] **12.** Build `Register.jsx` — role-aware form wired to `POST /api/auth/register`
- [ ] **13.** Build `Login.jsx` — wired to `POST /api/auth/login`
- [ ] **14.** Build `Dashboard.jsx` — role-conditional view (student match card / mentor list / admin panel)

---

## Notes

- Steps 1–7 are the hard dependency chain. Nothing works end-to-end until auth is live.
- Steps 8–9 can follow after auth is live.
- Frontend (10–14) can be built in parallel with 5–9 once `client.js` exists — test against Swagger at `http://localhost:8000/docs`.
- Use Alembic for future migrations; `init.sql` handles the initial schema for now.
- Never commit `.env`.

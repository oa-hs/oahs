-- OAHS initial schema
-- Runs once on first postgres container start (docker-entrypoint-initdb.d)

CREATE TYPE role_enum AS ENUM ('student', 'mentor', 'admin');
CREATE TYPE match_status_enum AS ENUM ('pending', 'active', 'completed');

CREATE TABLE IF NOT EXISTS users (
    id               SERIAL PRIMARY KEY,
    email            VARCHAR(255) UNIQUE NOT NULL,
    password_hash    TEXT NOT NULL,
    role             role_enum NOT NULL,
    first_name       VARCHAR(100),
    last_name        VARCHAR(100),
    oa_id            VARCHAR(50),
    lodge_id         VARCHAR(50),
    chapter          VARCHAR(100),
    region           VARCHAR(50),
    industry         VARCHAR(100),
    graduation_year  INT,
    employer         VARCHAR(200),
    bio              TEXT,
    signup_period    VARCHAR(20),
    is_active        BOOLEAN DEFAULT TRUE,
    created_at       TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS matches (
    id             SERIAL PRIMARY KEY,
    student_id     INT NOT NULL REFERENCES users(id),
    mentor_id      INT NOT NULL REFERENCES users(id),
    signup_period  VARCHAR(20) NOT NULL,
    match_score    FLOAT,
    match_criteria JSONB,
    status         match_status_enum DEFAULT 'pending',
    matched_at     TIMESTAMP DEFAULT NOW()
);

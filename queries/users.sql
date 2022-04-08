CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    created_at timestamp,
    first_name char(16),
    email char(64),
    country char(32)
)
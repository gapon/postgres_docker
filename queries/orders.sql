CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id int,
    created_at timestamp,
    price float,
    order_status_id int
)
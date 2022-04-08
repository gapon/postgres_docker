from db_utils import execute_query, insert_user, insert_order
from generate_data import generate_user, generate_order

# Create tables for users and orders
# execute_query('queries/users.sql')
# execute_query('queries/orders.sql')

'''
# Populate users table
for _ in range(10000):
    created_at, first_name, email, country = generate_user()
    insert_user(created_at, first_name, email, country)
'''

# Populate orders table
for _ in range(10000):
    user_id, created_at, order_status_id, price = generate_order()
    insert_order(user_id, created_at, order_status_id, price)


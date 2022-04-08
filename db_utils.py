import psycopg2
from config import config

def execute_query(query_path):
    """execute sql query"""
    with open(query_path, 'r') as f:
        sql = f.read()

    db = config(section='postgres')

    conn = None
    try:
        conn = psycopg2.connect(**db)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Table created")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    

def insert_user(created_at, first_name, email, country):
    """insert a new trip to a table"""
    sql = "INSERT INTO users (created_at, first_name, email, country) \
        VALUES(%s, %s, %s, %s) RETURNING id"

    conn = None
    user_id = None
    
    db = config(section='postgres')

    try:
        conn = psycopg2.connect(**db)
        cur = conn.cursor()
        cur.execute(sql, (created_at, first_name, email, country))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return user_id

def insert_order(user_id, created_at, order_status_id, price):
    """insert a new trip to a table"""
    sql = "INSERT INTO orders (user_id, created_at, order_status_id, price) \
        VALUES(%s, %s, %s, %s) RETURNING id"

    conn = None
    order_id = None
    
    db = config(section='postgres')

    try:
        conn = psycopg2.connect(**db)
        cur = conn.cursor()
        cur.execute(sql, (user_id, created_at, order_status_id, price))
        order_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return order_id
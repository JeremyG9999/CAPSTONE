import sqlite3

def flavor_counts_data():
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flavor_count")
    flavor_data = cursor.fetchall()
    conn.close()
    return flavor_data

def get_last_flavor_count():
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flavor_count ORDER BY id DESC LIMIT 1")
    last_entry = cursor.fetchone()  
    conn.close()
    return last_entry

def get_day_number():
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id) FROM flavor_count")
    result = cursor.fetchone()
    if result[0] is None:
        day_number = 1
    else:
        day_number = result[0] + 1
    conn.close()
    return day_number

def truck_report_logic():
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            CEIL(id / 10.0) AS period,
            MIN(id) AS start_day,
            MAX(id) AS end_day,
            SUM(lava) AS lava,
            SUM(hot_fudge) AS hot_fudge,
            SUM(blizzard) AS blizzard,
            SUM(chocolate) AS chocolate,
            SUM(vanilla) AS vanilla
        FROM flavor_count
        GROUP BY period
        ORDER BY period
    """)
    totals = cursor.fetchall()
    conn.close()
    return totals

def total_purchases_data():
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM total_purchases")
    flavor_data = cursor.fetchall()
    conn.close()
    return flavor_data

def total_flavor_counts_data():
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            lava,
            hot_fudge,
            blizzard,
            chocolate,
            vanilla
        FROM total_purchases
    """)
    totals = cursor.fetchone() 
    conn.close()
    return totals  

def customer_simulation_data():
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'CustomerSimulation'
    """)
    totals = cursor.fetchone()
    conn.close()
    return totals

def average_purchases():
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            AVG(lava), AVG(hot_fudge), AVG(blizzard), AVG(chocolate), AVG(vanilla)
        FROM flavor_count
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def average_truck_order_data():
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            AVG(lava), AVG(hot_fudge), AVG(blizzard), AVG(chocolate), AVG(vanilla)
        FROM truck_report
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def avg_customer_simulation_data():
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT AVG(lava), AVG(hot_fudge), AVG(blizzard), AVG(chocolate), AVG(vanilla)
        FROM simulation_type
        WHERE class_name = 'CustomerSimulation'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def total_sales():
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(lava + hot_fudge + blizzard + chocolate + vanilla) 
        FROM flavor_count
    """)
    total = cursor.fetchone()
    conn.close()
    return total

def customer_simulation_data():
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'CustomerSimulation'
    """)
    totals = cursor.fetchone()
    conn.close()
    return totals

def summer_simulation_data():
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'Summer'
    """)
    totals = cursor.fetchone()
    conn.close()
    return totals

def winter_simulation_data():
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'Winter'
    """)
    totals = cursor.fetchone()
    conn.close()
    return totals
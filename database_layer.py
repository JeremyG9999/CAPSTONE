import sqlite3

def db_setup():
    conn = sqlite3.connect("instance/site.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS purchases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flavor TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flavor_count (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lava INT, hot_fudge INT, blizzard INT, chocolate INT, vanilla INT
        )
    """)
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS simulation_type (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_name TEXT UNIQUE,
            lava INT, hot_fudge INT, blizzard INT, chocolate INT, vanilla INT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS truck_report (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            period INT UNIQUE, start_day INT, end_day INT,
            lava INT, hot_fudge INT, blizzard INT, chocolate INT, vanilla INT
        )
    """)
    conn.commit()
    conn.close()
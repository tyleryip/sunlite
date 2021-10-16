import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cursor = conn.cursor()

def create_event_table():
    sql = """ CREATE TABLE IF NOT EXISTS public."Event" (
    power character varying(10) NOT NULL,
    color character varying(100) NOT NULL,
    brightness double precision NOT NULL,
    duration double precision NOT NULL,
    scheduled_at timestamp without time zone NOT NULL,
    id integer NOT NULL,
    user_id integer NOT NULL
    ) """
    
    try:
        cursor.execute(sql)
        
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# returns an array of the events from the DB!
def get_events():
    sql = "SELECT * FROM public.Event"
    cursor.execute(sql)

    return cursor.fetchall()

def post_event(power, color, brightness, duration, scheduled_at, id, user_id):
    try:
        cursor.execute(""" 
        INSERT INTO public."Event" (
        power,
        color,
        brightness,
        duration,
        scheduled_at,
        id,
        user_id
        ) VALUES (?, ?, ?, ?, ?, ?, ?)""", (power, color, brightness, duration, scheduled_at, id, user_id))

        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def delete_events(id):
    try:
        cursor.execute("""
        DELETE FROM public.Event
        WHERE id = ?
        """, (id))

        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
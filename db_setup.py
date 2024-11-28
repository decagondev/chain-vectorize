import os
import psycopg2
from psycopg2 import sql

DB_URL = os.getenv("DATABASE_URL")
VECTOR_TABLE = "documents"

def setup_database():
    try:
        with psycopg2.connect(DB_URL) as conn:
            with conn.cursor() as cur:
                print("Ensuring pgvector extension exists...")
                cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
                conn.commit()

                print("Ensuring documents table exists...")
                create_table_query = sql.SQL("""
                CREATE TABLE IF NOT EXISTS {table} (
                    id SERIAL PRIMARY KEY,
                    vector VECTOR(1536),
                    metadata JSONB
                );
                """).format(table=sql.Identifier(VECTOR_TABLE))
                
                cur.execute(create_table_query)
                conn.commit()

                print("Database setup complete.")
    except psycopg2.Error as e:
        print(f"Error setting up the database: {e}")
        raise

if __name__ == "__main__":
    setup_database()

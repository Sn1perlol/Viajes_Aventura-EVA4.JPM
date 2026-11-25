import os
import sqlite3
import pymysql
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    return os.getenv("DB_ENGINE", "sqlite").lower()

def sql_marker():
    return "?" if get_engine() == "sqlite" else "%s"

def open_connection():
    engine = get_engine()
    if engine == "sqlite":
        conn = sqlite3.connect(os.getenv("DB_NAME", "viajes_aventura.db"))
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    if engine == "mysql":
        return pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            charset="utf8mb4",
        )
    raise ValueError(f"Unsupported engine: {engine}")
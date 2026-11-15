import os
import json
from datetime import date

import requests
import psycopg2

API_URL = os.environ["FX_API_URL"]  # confirm the exact path on the provider page first


def fetch_rates() -> dict:
    r = requests.get(API_URL, timeout=30)
    r.raise_for_status()
    return r.json()


def load_bronze(payload: dict) -> None:
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    with conn, conn.cursor() as cur:
        cur.execute(
            """INSERT INTO bronze_fx_raw (rate_date, payload)
               VALUES (%s, %s)
               ON CONFLICT (rate_date) DO NOTHING""",
            (date.today(), json.dumps(payload)),
        )
    conn.close()


if __name__ == "__main__":
    load_bronze(fetch_rates())

from sqlalchemy import create_engine
import pandas as pd
from database.database import DATABASE_URL

query = """
SELECT id, record_date, sessions, users, conversions, revenue, created_at
FROM analytics_records
"""

engine = create_engine(
    DATABASE_URL, echo=False
)

def get_data():
    return pd.read_sql(query, engine)

DATA = get_data()
from sqlalchemy import create_engine, text
import pandas as pd
from config import DB_URL

# Load function to write DataFrame to the database
def load(df: pd.DataFrame, table_name: str) -> pd.DataFrame:
    engine = create_engine(DB_URL)

    with engine.connect() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS {table_name}"))
        conn.commit()

    df.to_sql(table_name, engine, if_exists='append', index=False)

    return pd.read_sql(f"SELECT * FROM {table_name}", engine)

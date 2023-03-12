import os

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

from app.config import settings

connection_url = settings.get_db_url()
data_directory = os.path.join(os.path.dirname(__file__), "data")


class DataHelper:
    """Helper to manage test data im the database"""

    def __init__(self, connection_url: str = connection_url, data_directory: str = data_directory) -> None:
        self.engine: Engine = create_engine(connection_url)
        self.data_base_dir = data_directory

    def insert_from_csv(
        self,
        table_name: str,
        subdir_file_path: str,
        sep=",",
        quotechar='"',
        encoding="utf8",
    ):
        """Insert in a table the data read from a CSV file in a sudirectory of test data directory"""
        file_path = os.path.join(self.data_base_dir, subdir_file_path)
        df = pd.read_csv(
            filepath_or_buffer=file_path,
            sep=sep,
            quotechar=quotechar,
            encoding=encoding,
        )
        with self.engine.begin() as con:
            df.to_sql(table_name, con=con, index=False, if_exists="append")

    def truncate_table(self, table_name: str):
        with self.engine.begin() as con:
            con.execute(text(f"TRUNCATE TABLE {table_name}"))

    def delete_rows(self, table_name: str, ids: list[int]):
        ids_joined = ",".join([str(i) for i in ids])
        with self.engine.begin() as con:
            con.execute(text(f"DELETE FROM {table_name} WHERE id in ({ids_joined})"))

    def delete_all_rows(self, table_name: str):
        with self.engine.begin() as con:
            con.execute(text(f"DELETE FROM {table_name}"))

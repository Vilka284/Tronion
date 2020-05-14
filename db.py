import psycopg2
import sys

from config import DatabaseConfig


class Databse:

    def __init__(self):
        self.host = DatabaseConfig.DATABASE_HOST
        self.username = DatabaseConfig.DATABASE_USERNAME
        self.password = DatabaseConfig.DATABASE_PASSWORD
        self.port = DatabaseConfig.DATABASE_PORT
        self.dbname = DatabaseConfig.DATABASE_NAME
        self.conn = None


    def connection(self):
        """
        db conection function
        """
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname
                )
            except psycopg2.DatabaseError as e:
                sys.exit(e)


    def commit(self):
        return self.conn.commit()


    def select_rows(self, query):
        """
        SQL query to select rows from table.
        """
        with self.conn.cursor() as cur:
            cur.execute(query)
            rows = [row for row in cur.fetchall()]
            cur.close()
            # self.conn.close()
            return rows if len(rows) > 0 else None


    def insert_data(self, query):
        """
        SQL query to insert data to table.
        """
        with self.conn.cursor() as cur:
            cur.execute(query)
            cur.close()


    def delete_rows(self, query):
        """
        SQL query to delete rows from table
        """
        with self.conn.cursor() as cur:
            cur.execute(query)
            cur.close()
import psycopg2
from contextlib import contextmanager
from psycopg2.extras import RealDictCursor


class DbReader:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="44.223.32.0",
            user="postgres",
            password="Starboy@123",
            dbname="postgres",
            port="5432"
        )
        self.cursor_type = RealDictCursor

    @contextmanager
    def sql_connect(self):
        cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        try:
            yield cursor

        finally:
            self.connection.commit()
            cursor.close()

    @contextmanager
    def dbconnect(self):
        try:
            yield self.connection

        finally:
            self.connection.commit()
            self.connection.close()
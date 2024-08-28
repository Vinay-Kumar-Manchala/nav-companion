from src.useme.db_reader import DbReader


class PostgresUtil(object):
    def __init__(self):
        try:
            self.sql_obj = DbReader()

        except Exception as e:
            raise Exception("DB Configuration Error" + str(e))

    def fetch_data_from_postgres(self, query):
        """
            This method is used for fetching the data from the table.
            :param query: query to fetch the data.
            :return: status: The status True on success and False on failure and the data.
        """
        result = []
        try:
            with self.sql_obj.sql_connect() as conn:
                conn.execute(query)
                result = conn.fetchall()

            return result
        except Exception as e:
            print(e)
            return result, []

    def execute_query(self, query):
        try:
            with self.sql_obj.sql_connect() as conn:
                conn.execute(query)

        except Exception as e:
            print(str(e))
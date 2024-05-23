from db_manager import start_postgres_connection, query_database

if __name__ == "__main__":
    conn = start_postgres_connection()
    query = """
            SELECT COUNT(*) AS TOTAL_RECORDS
            FROM ALT_SCHOOL.NETFLIX_DATA;
            """
    result = query_database(connection=conn, query_str=query)
    print(result)

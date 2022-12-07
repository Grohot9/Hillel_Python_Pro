import sqlite3


def format_records(records: list) -> str:
    return "<br>".join(str(record) for record in records)


def execute_query(query, args=()):
    with sqlite3.connect("chinook.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        connection.commit()
        records = cursor.fetchall()
    return records

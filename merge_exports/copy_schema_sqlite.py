import sqlite3

# The sqlalchemy one is better because it includes types
# [SQLite Export Schema - SQL - A ShareGPT conversation](https://sharegpt.com/c/SRIUYbQ)
def export_schema_to_create_statements(database_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Get table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = [row[0] for row in cursor.fetchall()]

    # Generate CREATE TABLE statements for each table
    create_table_statements = []
    for table_name in table_names:
        cursor.execute(f"PRAGMA table_info({table_name})")
        table_info = cursor.fetchall()

        columns = []
        for column_info in table_info:
            column_name, column_type, _, _, _, _ = column_info
            columns.append(f"{column_name} {column_type}")

        create_table_statement = f"CREATE TABLE {table_name} ({', '.join(columns)});"
        create_table_statements.append(create_table_statement)

    # Close the database connection
    conn.close()

    return create_table_statements

if __name__ == "__main__":
    database_path = "test.db"  # Replace with your SQLite database file path
    create_table_statements = export_schema_to_create_statements(database_path)

    # Save the CREATE TABLE statements to a file
    with open("schema_export_sqlite.sql", "w") as file:
        file.write("\n".join(create_table_statements))
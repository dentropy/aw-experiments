from sqlalchemy import create_engine, MetaData

# [SQLite Export Schema - SQL - A ShareGPT conversation](https://sharegpt.com/c/SRIUYbQ)
def export_schema_to_create_statements(database_path):
    # Create a SQLAlchemy engine to connect to the database
    engine = create_engine(f"sqlite:///{database_path}", echo=True)

    # Reflect the existing database schema
    metadata = MetaData()
    metadata.reflect(bind=engine)

    # Generate CREATE TABLE statements for each table
    create_table_statements = []
    for table_name, table in metadata.tables.items():
        columns = []
        for column in table.columns:
            columns.append(f"{column.name} {column.type}")

        create_table_statement = f"CREATE TABLE {table_name} ({', '.join(columns)});"
        create_table_statements.append(create_table_statement)

    return create_table_statements

if __name__ == "__main__":
    database_path = "test.db"  # Replace with the desired SQLite database file path
    create_table_statements = export_schema_to_create_statements(database_path)

    # Save the CREATE TABLE statements to a file
    with open("schema_export_sqlalchemy.sql", "w") as file:
        file.write("\n".join(create_table_statements))
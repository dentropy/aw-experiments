import sqlite3

# [Readlines one by one. - A ShareGPT conversation](https://sharegpt.com/c/C7FYcIj)

conn = sqlite3.connect('merge_exports.db')
cursor = conn.cursor()
with open('schema_export_sqlalchemy.sql', 'r') as file:
    for line in file.readlines():
        create_table_query = line.strip()
        print(create_table_query)
        cursor.execute(create_table_query)
conn.commit()
conn.close()
import json
import sqlite3
from pprint import pprint
import sys
from dateutil.parser import parse


# [Read JSON in Python3. - A ShareGPT conversation](https://sharegpt.com/c/jz9wb9V)
# [Insert SQLite Data. - A ShareGPT conversation](https://sharegpt.com/c/sOzBxNH)


def insert_data(database_path, table_name, columns, data_list):
    # Step 1: Connect to the database (creates a new database if it doesn't exist)
    conn = sqlite3.connect(database_path)

    # Step 2: Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Step 3: Write the SQL INSERT statement
    placeholders = ', '.join(['?' for _ in columns])
    column_names = ', '.join(columns)
    sql_insert = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"

    # print("sql_insert")
    # print(sql_insert)
    # print("placeholders")
    # print(placeholders)
    # Step 4: Execute the INSERT statement with the appropriate data
    try:
        cursor.executemany(sql_insert, data_list)
        conn.commit()  # Commit the changes to the database
        print("Data inserted successfully!")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()  # Rollback the changes if there's an error

    # Step 5: Close the cursor and the connection
    cursor.close()
    conn.close()

file_path = "/MEGA/MEGA/QuantifiedSelf/ActivityWatch/to_merge/"
file_name = 'aw-buckets-export.json'
with open(file_path + file_name, 'r') as file:
    data = json.load(file)
bucket_metadata = []
bucket_columns = ""
for key in data["buckets"]:
    bucket_columns = list ( data["buckets"][key].keys())[:6]
    tmp_bucket_metadata = []
    for key2 in bucket_columns:
        tmp_bucket_metadata.append(data["buckets"][key][key2])
    bucket_metadata.append(tmp_bucket_metadata)
pprint(bucket_metadata)

database_path = "merge_exports.db"
insert_data(database_path, "bucketmodel", bucket_columns, bucket_metadata)

for key in data["buckets"]:
    bucket_columns = list ( data["buckets"][key].keys())[:6]
    tmp_event_data = []
    count = 0
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM bucketmodel where id = '{data['buckets'][key]['id']}';")
    rows = cursor.fetchall()
    bucket_id = rows[0][0]
    event_columns = ("bucket_id", "timestamp", "duration", "datastr")
    for event in data["buckets"][key]["events"]:
        tmp_event_data = []
        for key2 in event_columns:
            # bucket_id, timestamp, duration, datastr
            tmp_event_data.append([
                bucket_id,
                parse(event["timestamp"]),
                float(event["duration"]),
                json.dumps(event["data"])
            ])
        count += 1
        if count == 100:
            print("Inserting 100 Events")
            insert_data("merge_exports.db", "eventmodel", event_columns, tmp_event_data)
            count = 0
            sys.exit
    insert_data("merge_exports.db", "eventmodel", event_columns, tmp_event_data)
    print(f"Done bucket_id = {bucket_id}")

from Database.connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
ORDER BY name
""")

tables = cursor.fetchall()

print("\nDanh sách bảng:")

for table in tables:
    print(" -", table["name"])

conn.close()
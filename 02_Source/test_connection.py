from Database.connection import get_connection

conn = get_connection()

print("Kết nối thành công!")
print(conn)

conn.close()
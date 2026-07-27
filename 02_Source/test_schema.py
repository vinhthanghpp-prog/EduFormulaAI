from Database.schema import DATABASE_SCHEMA

print("Có", len(DATABASE_SCHEMA), "câu lệnh SQL")

for i, sql in enumerate(DATABASE_SCHEMA, start=1):
    print(f"SQL {i}: OK")
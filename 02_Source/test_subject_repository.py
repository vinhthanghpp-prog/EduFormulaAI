from Database.Repository.subject_repository import SubjectRepository

repo = SubjectRepository()

print("\n===== DANH SÁCH MÔN HỌC =====")

subjects = repo.get_all()

for subject in subjects:
    print(subject)

print("\n===== TÌM THEO ID =====")
print(repo.get_by_id(1))

print("\n===== TÌM THEO CODE =====")
print(repo.get_by_code("MATH"))
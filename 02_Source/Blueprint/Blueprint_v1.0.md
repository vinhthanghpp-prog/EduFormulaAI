# EduFormula AI

## Blueprint v1.0

Status:
Foundation Platform Frozen

Latest Build:
BUILD-039

Latest Commit:
f5aad97

Last Update:
2026-08-05
---

# 1. Project Vision

EduFormula AI là nền tảng học tập thông minh hỗ trợ học sinh THPT hiểu sâu bản chất của công thức, định luật và kiến thức thông qua trí tuệ nhân tạo, trực quan hóa và lộ trình học tập cá nhân hóa.

Khác với phương pháp học thuộc lòng truyền thống, EduFormula AI hướng tới việc giúp người học:

- Hiểu bản chất của công thức.
- Hiểu mối liên hệ giữa các biến số.
- Hiểu điều kiện áp dụng.
- Hiểu cách suy luận.
- Hiểu cách vận dụng vào bài tập.

Mọi thành phần của hệ thống đều được thiết kế theo nguyên tắc dễ mở rộng, dễ kiểm thử và dễ bảo trì.

---

# 2. Project Objectives

## 2.1 Mục tiêu tổng quát

Xây dựng nền tảng AI hỗ trợ học tập cho học sinh THPT với khả năng:

- Giải thích công thức.
- Phân tích kiến thức.
- Sinh ví dụ minh họa.
- Trực quan hóa kiến thức.
- Cá nhân hóa quá trình học.

## 2.2 Mục tiêu kỹ thuật

- Kiến trúc nhiều tầng (Layered Architecture).
- Áp dụng Repository Pattern.
- Áp dụng Service Layer.
- Thiết kế Domain độc lập.
- Dễ dàng mở rộng trong tương lai.
- Hỗ trợ kiểm thử tự động.

## 2.3 Mục tiêu chất lượng

- Code rõ ràng.
- API nhất quán.
- TDD làm trung tâm.
- Regression Test trước mỗi Release.
- Freeze sau mỗi BUILD.

---

# 3. Development Principles

Mọi BUILD trong EduFormula AI phải tuân thủ các nguyên tắc sau.

## 3.1 Blueprint First

Không phát triển chức năng ngoài Blueprint đã đóng băng nếu chưa được thống nhất.

## 3.2 One Build – One Goal

Mỗi BUILD chỉ thực hiện một mục tiêu rõ ràng.

## 3.3 One Build – One Main File

Mỗi BUILD chỉ tập trung vào một file hoặc một nhóm thay đổi có phạm vi nhỏ và kiểm soát được.

## 3.4 Test Driven Development

Quy trình bắt buộc:

RED

↓

GREEN

↓

REFACTOR

↓

API CONSISTENCY CHECK

↓

FREEZE

↓

GIT

## 3.5 Freeze Policy

Một BUILD chỉ được Freeze khi:

- Unit Test PASS.
- Integration Test PASS (nếu có).
- API nhất quán.
- Không còn lỗi đã biết trong phạm vi BUILD.

## 3.6 Long-term Maintainability

Ưu tiên:

- Dễ đọc.
- Dễ mở rộng.
- Dễ kiểm thử.
- Dễ bảo trì.

Không tối ưu sớm nếu chưa có nhu cầu thực tế.

---

# 4. System Architecture

EduFormula AI được xây dựng theo kiến trúc nhiều tầng (Layered Architecture).

```
Presentation Layer
        │
        ▼
Application Layer
        │
        ▼
Service Layer
        │
        ▼
Repository Layer
        │
        ▼
Database Layer
```

## 4.1 Presentation Layer

Chứa toàn bộ giao diện người dùng.

Ví dụ:

- Main Window
- Lesson Viewer
- Formula Viewer
- Variable Viewer
- Learning Panel
- AI Explanation Panel

Presentation Layer không truy cập trực tiếp Database.

---

## 4.2 Application Layer

Điều phối luồng xử lý giữa giao diện và Service.

Nhiệm vụ:

- Nhận sự kiện từ UI.
- Gọi Service phù hợp.
- Trả kết quả về UI.

---

## 4.3 Service Layer

Chứa toàn bộ Business Logic.

Ví dụ:

- Validation
- Kiểm tra dữ liệu
- Quy tắc nghiệp vụ
- Điều phối Repository

Service không thực hiện SQL trực tiếp.

---

## 4.4 Repository Layer

Repository chịu trách nhiệm truy cập dữ liệu.

Mỗi Domain có Repository riêng.

Ví dụ:

- SubjectRepository
- GradeRepository
- ChapterRepository
- LessonRepository
- KnowledgeRepository
- FormulaRepository
- VariableRepository

Repository không chứa Business Logic.

---

## 4.5 Database Layer

Phiên bản Foundation sử dụng SQLite.

Mọi truy cập CSDL đều thông qua Repository.

---

# 5. Technology Stack

## Ngôn ngữ

- Python 3.14+

## Database

- SQLite

## GUI

- CustomTkinter

## Testing

- unittest

## Version Control

- Git
- GitHub

## IDE

- Visual Studio Code

---

# 6. Project Folder Structure

```
EduFormulaAI/

│
├── Blueprint/
│     Blueprint_v1.0.md
│
├── Docs/
│
├── Changelog/
│
├── 02_Source/
│
│     Database/
│
│     Services/
│
│     Modules/
│
│     UI/
│
│     Tests/
│
│         Repository/
│
│         Service/
│
│         Integration/
│
├── Assets/
│
├── Releases/
│
└── README.md
```

## Quy tắc tổ chức

- Database chỉ chứa tầng dữ liệu.
- Services chỉ chứa nghiệp vụ.
- Modules điều phối chức năng.
- UI chỉ hiển thị giao diện.
- Tests chứa toàn bộ Unit Test và Integration Test chính thức.
- Blueprint là tài liệu kiến trúc của dự án.

---

# 7. Database Architecture

## 7.1 Database Engine

Foundation Platform sử dụng SQLite làm hệ quản trị cơ sở dữ liệu.

Ưu điểm:

- Không cần cài đặt máy chủ.
- Phù hợp ứng dụng Desktop.
- Dễ sao lưu.
- Dễ triển khai.
- Đủ khả năng mở rộng cho giai đoạn Foundation.

---

## 7.2 Database Access

Mọi truy cập cơ sở dữ liệu phải thông qua Repository.

UI và Service không được thực hiện SQL trực tiếp.

```
UI
    ↓
Service
    ↓
Repository
    ↓
SQLite
```

---

## 7.3 BaseRepository

Tất cả Repository kế thừa BaseRepository.

BaseRepository chịu trách nhiệm:

- Quản lý Connection.
- Tạo Cursor.
- Commit.
- Rollback.
- Execute.
- Execute Many.
- Fetch One.
- Fetch All.

---

## 7.4 Transaction Policy

Mỗi thao tác ghi dữ liệu phải:

- Commit khi thành công.
- Rollback khi có lỗi.

Không được để Transaction mở ngoài phạm vi Repository.

---

## 7.5 Timestamp

Mọi bảng nghiệp vụ đều sử dụng:

- created_at
- updated_at

để phục vụ truy vết dữ liệu.

---

## 7.6 Naming Convention

Tên bảng sử dụng chữ thường số nhiều.

Ví dụ:

- subjects
- grades
- chapters
- lessons
- knowledge
- formulas
- variables

---

# 8. Domain Model

Foundation Platform hiện gồm các Domain sau:

```
Subject
    │
    ▼
Grade
    │
    ▼
Chapter
    │
    ▼
Lesson
    │
    ▼
Knowledge
    │
    ▼
Formula
    │
    ▼
Variable
```

## Subject

Đại diện cho một môn học.

Ví dụ:

- Toán
- Vật lý
- Hóa học

---

## Grade

Đại diện cho khối lớp.

Ví dụ:

- Lớp 10
- Lớp 11
- Lớp 12

---

## Chapter

Đại diện cho chương học.

---

## Lesson

Đại diện cho bài học.

---

## Knowledge

Đơn vị kiến thức nhỏ nhất trong bài học.

Knowledge có thể chứa:

- Khái niệm
- Định nghĩa
- Công thức
- Định lý
- Quy tắc

---

## Formula

Đại diện cho một công thức.

Formula thuộc về một Knowledge.

---

## Variable

Đại diện cho biến số của Formula.

Một Formula có nhiều Variable.

---

# 9. Repository Standard

Mỗi Domain có một Repository riêng.

Repository chịu trách nhiệm:

- CRUD.
- Truy vấn.
- Mapping dữ liệu.

Repository không chứa Business Logic.

API chuẩn:

- create()
- get_by_id()
- update()
- delete()

Các hàm mở rộng:

- exists_xxx()
- get_by_xxx()

Repository kế thừa BaseRepository.

Mọi Repository phải có Unit Test.

---

# 10. Service Standard

Service là tầng chứa Business Logic.

Service không thao tác SQL trực tiếp.

Service chịu trách nhiệm:

- Validation.
- Kiểm tra dữ liệu.
- Kiểm tra khóa ngoại.
- Kiểm tra dữ liệu trùng.
- Điều phối Repository.

Validation tối thiểu:

- Không để trống dữ liệu bắt buộc.
- Kiểm tra mã duy nhất.
- Kiểm tra tính tồn tại của dữ liệu liên quan.

Mọi Service phải có Unit Test.

---

# 11. Testing Strategy

EduFormula AI áp dụng chiến lược kiểm thử nhiều tầng nhằm đảm bảo chất lượng và khả năng mở rộng.

## Unit Test

Kiểm thử từng Repository và Service độc lập.

Yêu cầu:

- Mỗi Repository phải có Unit Test.
- Mỗi Service phải có Unit Test.

## Integration Test

Kiểm thử luồng dữ liệu giữa các Domain.

Ví dụ:

Subject → Grade → Chapter → Lesson → Knowledge → Formula → Variable

## Regression Test

Trước mỗi Release phải chạy toàn bộ bộ kiểm thử chính thức.

Lệnh:

```bash
python -m unittest discover -v -s Tests
```

Các bài kiểm thử thử nghiệm (Prototype/UI) không thuộc Regression Suite chính thức.

---

# 12. Coding Standards

## Naming

- Class: PascalCase
- Function: snake_case
- Variable: snake_case
- Constant: UPPER_CASE

## Repository

- Không chứa Business Logic.

## Service

- Không thực hiện SQL trực tiếp.

## Model

- Chỉ chứa dữ liệu.

## Comment

Ưu tiên mã nguồn rõ ràng, chỉ bổ sung comment khi giúp giải thích quyết định thiết kế hoặc nghiệp vụ.

---

# 13. Build Workflow

Mọi BUILD phải tuân theo quy trình:

RED

↓

GREEN

↓

REFACTOR

↓

API CONSISTENCY CHECK

↓

FREEZE

↓

GIT

Không chuyển BUILD tiếp theo nếu BUILD hiện tại chưa hoàn thành.

---

# 14. Frozen Roadmap

## Foundation Platform

Status: Completed

Hoàn thành:

- Subject
- Grade
- Chapter
- Lesson
- Knowledge
- Formula
- Variable

## Blueprint

Status: In Progress

- BUILD-040A
- BUILD-040B
- BUILD-040C
- BUILD-040D

## Next Development

Sau khi Blueprint v1.0 được hoàn thành và Freeze, Roadmap cho BUILD-041 trở đi sẽ được xác nhận chính thức và bổ sung vào tài liệu này trước khi triển khai.

---

# 15. Milestones

M1

Foundation Platform v1.0

Completed

M2

Blueprint v1.0

In Progress

M3

Content Platform

Planned

M4

AI Engine

Planned

M5

Learning Experience

Planned

---

# 16. Release History

## Foundation Platform

- BUILD-039
  Variable Integration Test completed.

## Blueprint

- BUILD-040A
  Vision, Objectives, Development Principles.

- BUILD-040B
  Architecture, Technology Stack, Folder Structure.

- BUILD-040C
  Database Architecture, Domain Model, Repository Standard, Service Standard.

- BUILD-040D
  Testing Strategy, Coding Standards, Build Workflow, Roadmap, Milestones, Release History.
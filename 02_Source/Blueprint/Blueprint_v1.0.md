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
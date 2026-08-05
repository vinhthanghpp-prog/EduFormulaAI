# ADR-002

## Title

Adopt Learning Content Model Architecture

---

## Status

Approved

---

## Context

Foundation Platform quản lý dữ liệu.

Các Domain hiện có:

- Subject
- Grade
- Chapter
- Lesson
- Knowledge
- Formula
- Variable

Các Domain này phục vụ lưu trữ dữ liệu nhưng chưa phản ánh đầy đủ cấu trúc học tập.

Trong các giai đoạn tiếp theo, nhiều Engine sẽ cần truy cập cùng một mô hình nội dung học tập, bao gồm:

- Explanation Engine
- Visualization Engine
- Question Engine
- Learning Path Engine

Nếu các Engine truy cập trực tiếp Database Entity sẽ tạo ra sự phụ thuộc chặt và khó mở rộng.

---

## Decision

EduFormula AI sẽ sử dụng Learning Content Model như một lớp trung gian.

Kiến trúc:

Foundation Platform

↓

Mapper

↓

Learning Content Model

↓

Explanation Engine

Visualization Engine

Question Engine

Learning Path Engine

---

## Consequences

Ưu điểm:

- Tách biệt dữ liệu và nội dung học tập.
- Không phụ thuộc Database.
- Không phụ thuộc Repository.
- Có thể thay đổi Database mà không ảnh hưởng AI Engine.
- Có thể bổ sung nhiều nguồn dữ liệu.

---

## Approved

Architecture Review

AR-002

Date:

2026-08-06
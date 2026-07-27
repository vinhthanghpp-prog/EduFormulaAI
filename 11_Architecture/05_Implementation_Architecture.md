# EduFormula AI

# 05 - Implementation Architecture

Version: 1.0

---

# 1. Mục tiêu

Tài liệu này mô tả cách triển khai kỹ thuật của EduFormula AI.

Mục tiêu:

- Chuẩn hóa kiến trúc lập trình.
- Giảm sự phụ thuộc giữa các module.
- Hỗ trợ mở rộng lâu dài.
- Cho phép thay thế AI mà không ảnh hưởng hệ thống.

---

# 2. Kiến trúc tổng thể

                 User

                   │

                   ▼

             Main Window

                   │

                   ▼

            Lesson Viewer

                   │

                   ▼

          Lesson Renderer

                   │

                   ▼

         Card Framework (UI)

                   ▲

                   │

          Learning Engine

                   ▲

                   │

          Knowledge Graph

                   ▲

                   │

             Lesson Data

---

# 3. Thư mục dự án

02_Source/

Core/
    Learning/
    Assessment/
    Knowledge/
    Services/

Modules/
    Lessons/

UI/
    Cards/
    Components/
    Theme/

Documentation/

Tests/

---

# 4. Trách nhiệm của từng tầng

Layer 1
Design System

Chịu trách nhiệm:

- Font
- Color
- Theme
- Layout

-----------------------

Layer 2
Lesson Data

Chứa:

- metadata
- formula
- variables
- worked_examples

Không chứa UI.

-----------------------

Layer 3
Knowledge Layer

Biến Lesson thành Knowledge Graph.

Không có giao diện.

-----------------------

Layer 4
Learning Engine

Phân tích bài toán.

Sinh câu hỏi.

Sinh gợi ý.

Đánh giá học sinh.

-----------------------

Layer 5
Rendering Layer

Hiển thị dữ liệu.

Không xử lý logic.

-----------------------

Layer 6
AI Teacher

Trao đổi với học sinh.

Không chứa kiến thức.

---

# 5. Luồng dữ liệu

Lesson

↓

Knowledge Builder

↓

Knowledge Graph

↓

Problem Analyzer

↓

Learning Session

↓

Renderer

↓

Student

↓

Feedback

↓

Learning Engine

---

# 6. Learning Engine

Learning Engine gồm các module:

ProblemAnalyzer

KnowledgeMapper

StrategyPlanner

QuestionEngine

HintEngine

FeedbackEngine

AssessmentEngine

LearningSession

---

# 7. Card Framework

Cards:

BaseCard

ObjectiveCard

FormulaCard

VariableCard

ExampleCard

TipsCard

SummaryCard

QuizCard

GuidedSolutionCard

Các Card chỉ hiển thị dữ liệu.

Không xử lý AI.

---

# 8. Quy tắc Dependency

Lesson

↓

Knowledge

↓

Learning

↓

Renderer

↓

UI

↓

Student

AI nằm ngoài kiến trúc này.

---

# 9. Coding Rules

Không import ngược.

Không truy cập dữ liệu trực tiếp từ UI.

Learning Engine không gọi UI.

Lesson không chứa logic.

Card không chứa AI.

---

# 10. Testing

Mỗi module đều có:

test_xxx.py

Mỗi Sprint phải PASS.

---

# 11. Versioning

Major

Thay đổi kiến trúc.

Minor

Thêm module.

Patch

Sửa lỗi.

---

# 12. Future Extension

OCR

Voice

Camera

Adaptive Learning

Cloud Sync

Teacher Dashboard

Analytics

# 13. Design Principles

EduFormula AI tuân theo các nguyên tắc sau:

## 1. Separation of Concerns

Dữ liệu, giao diện và AI phải tách biệt.

---

## 2. Reusability

Mọi Card đều có thể tái sử dụng.

---

## 3. Data Driven

Bài học quyết định giao diện.

Không hard-code giao diện.

---

## 4. AI Independent

Có thể thay GPT bằng Claude, Gemini...

Không phải sửa Lesson.

---

## 5. Explain Before Answer

Luôn ưu tiên giải thích trước khi đưa đáp án.

---

## 6. Student-centered

AI không giải hộ.

AI hướng dẫn học sinh tự giải.

---

## 7. Extensible

Có thể bổ sung môn học mới mà không thay đổi kiến trúc.

---

## 8. Testable

Mọi module đều phải kiểm thử độc lập.
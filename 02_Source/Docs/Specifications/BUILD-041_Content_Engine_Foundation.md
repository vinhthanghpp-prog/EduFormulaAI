# 1. Overview

## Purpose

Content Engine Foundation là lớp trung gian giữa Foundation Platform và các AI Engine của EduFormula AI.

Nhiệm vụ của Content Engine là chuyển đổi dữ liệu học tập đã được quản lý bởi Foundation Platform thành mô hình nội dung thống nhất để phục vụ:

- Explanation Engine
- Visualization Engine
- Question Engine
- Learning Path Engine

Content Engine không thay thế Foundation Platform và không quản lý dữ liệu nghiệp vụ. Thay vào đó, nó chuẩn hóa cách biểu diễn và tổ chức nội dung học tập nhằm đảm bảo mọi Engine phía trên sử dụng cùng một mô hình dữ liệu.

## Position in System

Kiến trúc tổng thể:

Foundation Platform
↓
Content Engine
↓
Explanation Engine
Visualization Engine
Question Engine
Learning Path Engine

Content Engine là nền tảng chung cho toàn bộ các Engine chức năng của EduFormula AI.

# 2. Background

## Existing Foundation Platform

Milestone M1 đã hoàn thành Foundation Platform v1.0 với đầy đủ các Domain nghiệp vụ:

- Subject
- Grade
- Chapter
- Lesson
- Knowledge
- Formula
- Variable

Foundation Platform chịu trách nhiệm quản lý dữ liệu học tập, cung cấp khả năng lưu trữ, truy xuất và kiểm thử dữ liệu theo kiến trúc Repository – Service.

Các Domain này đã được kiểm thử bằng Unit Test và Integration Test, đồng thời đã được đóng băng (Freeze) trong Milestone M1.

---

## Problem Statement

Mặc dù Foundation Platform đã quản lý tốt dữ liệu, hệ thống vẫn chưa có một mô hình thống nhất để biểu diễn nội dung học tập.

Ví dụ:

- Một Formula chỉ được lưu như một bản ghi dữ liệu.
- Một Knowledge chỉ chứa thông tin nghiệp vụ.
- Một Lesson chỉ thể hiện cấu trúc lưu trữ.

Các thành phần này chưa phản ánh được:

- Mục tiêu học tập.
- Quan hệ sư phạm.
- Trình tự tiếp thu kiến thức.
- Điều kiện tiên quyết.
- Các lỗi thường gặp.
- Cách giải thích cho người học.

Do đó, các AI Engine trong tương lai sẽ phải tự diễn giải dữ liệu theo nhiều cách khác nhau, dễ dẫn đến thiếu nhất quán và khó bảo trì.

---

## Motivation

Content Engine được xây dựng nhằm tạo ra một mô hình nội dung học tập thống nhất.

Content Engine sẽ:

- Chuẩn hóa cách biểu diễn nội dung học tập.
- Chuẩn hóa cấu trúc của bài học.
- Chuẩn hóa cách tổ chức kiến thức.
- Cung cấp dữ liệu thống nhất cho các Engine phía trên.

Các Engine như:

- Explanation Engine
- Visualization Engine
- Question Engine
- Learning Path Engine

sẽ không truy cập trực tiếp Foundation Platform mà sử dụng mô hình do Content Engine cung cấp.

Điều này giúp đảm bảo:

- Tính nhất quán.
- Khả năng mở rộng.
- Dễ bảo trì.
- Dễ kiểm thử.

# 3. Objectives

## 3.1 Overall Objective

Content Engine Foundation được xây dựng nhằm tạo ra một mô hình nội dung học tập thống nhất (Unified Learning Content Model) cho toàn bộ EduFormula AI.

Content Engine đóng vai trò là lớp trung gian giữa Foundation Platform và các Engine chức năng, đảm bảo mọi thành phần của hệ thống sử dụng cùng một cách biểu diễn nội dung học tập.

---

## 3.2 Functional Objectives

Content Engine phải đáp ứng các mục tiêu chức năng sau:

### FO-01

Chuẩn hóa cấu trúc nội dung của một bài học.

---

### FO-02

Biểu diễn đầy đủ mối quan hệ giữa:

- Lesson
- Knowledge
- Formula
- Variable

---

### FO-03

Cung cấp mô hình nội dung thống nhất cho:

- Explanation Engine
- Visualization Engine
- Question Engine
- Learning Path Engine

---

### FO-04

Hỗ trợ mở rộng để bổ sung các loại nội dung học tập mới mà không làm thay đổi Foundation Platform.

---

## 3.3 Non-functional Objectives

Content Engine phải đáp ứng các yêu cầu phi chức năng sau:

### NFO-01

Không thay đổi Database Schema của Foundation Platform.

---

### NFO-02

Không làm thay đổi Repository hoặc Service hiện có.

---

### NFO-03

Đảm bảo khả năng mở rộng để hỗ trợ nhiều môn học và nhiều cấp học.

---

### NFO-04

Dễ kiểm thử bằng Unit Test và Integration Test.

---

### NFO-05

Độc lập với giao diện người dùng (UI) và công nghệ AI cụ thể.

---

## 3.4 Success Criteria

BUILD-041 được coi là thành công khi:

- Có mô hình Learning Content Model hoàn chỉnh.
- Có kiến trúc Content Engine rõ ràng.
- Không ảnh hưởng đến Foundation Platform.
- Các Engine phía trên có thể sử dụng chung mô hình dữ liệu của Content Engine.

# 4. Scope

## 4.1 In Scope

BUILD-041 bao gồm các nội dung sau:

### IS-01

Thiết kế mô hình Learning Content Model.

---

### IS-02

Xác định kiến trúc của Content Engine.

---

### IS-03

Chuẩn hóa cách biểu diễn nội dung học tập.

---

### IS-04

Xây dựng mô hình liên kết giữa:

- Lesson
- Knowledge
- Formula
- Variable

---

### IS-05

Thiết kế giao diện (API Contract) giữa Foundation Platform và Content Engine.

---

### IS-06

Định nghĩa các thành phần nội dung học tập sẽ được các Engine sử dụng chung.

Bao gồm:

- Learning Objectives
- Prerequisites
- Key Knowledge
- Formula List
- Variable Map
- Common Mistakes
- Examples
- Exercises
- Summary
- Next Lesson

---

## 4.2 Out of Scope

Các nội dung sau không thuộc phạm vi BUILD-041.

### OS-01

Không thay đổi Database Schema.

---

### OS-02

Không thay đổi Repository hiện có.

---

### OS-03

Không thay đổi Service hiện có.

---

### OS-04

Không phát triển giao diện người dùng.

---

### OS-05

Không tích hợp AI.

---

### OS-06

Không xây dựng Explanation Engine.

---

### OS-07

Không xây dựng Visualization Engine.

---

### OS-08

Không xây dựng Question Engine.

---

### OS-09

Không xây dựng Learning Path Engine.

---

## 4.3 Assumptions

Content Engine giả định rằng:

- Foundation Platform đã hoàn thành và được Freeze.
- Blueprint v1.0 đã được phê duyệt.
- Các Domain hiện tại ổn định và có thể tái sử dụng.

---

## 4.4 Constraints

Content Engine phải tuân thủ các ràng buộc sau:

- Không làm thay đổi kiến trúc Foundation Platform.
- Không tạo phụ thuộc ngược từ Foundation sang Content Engine.
- Mọi Engine phía trên chỉ truy cập dữ liệu thông qua Content Engine.

# 5. Learning Content Model

## 5.1 Purpose

Learning Content Model là mô hình nội dung học tập thống nhất của EduFormula AI.

Mục tiêu của mô hình này là chuyển đổi dữ liệu học tập được quản lý bởi Foundation Platform thành cấu trúc nội dung phục vụ việc giảng dạy, học tập và xử lý bởi các Engine chức năng.

Learning Content Model không thay thế Foundation Platform mà đóng vai trò là lớp trung gian giữa tầng dữ liệu và tầng xử lý học tập.

---

## 5.2 Position in Architecture

Kiến trúc tổng thể:

Foundation Platform
        │
        ▼
Content Mapper
        │
        ▼
Learning Content Model
        │
        ├──────────────┬──────────────┬──────────────┐
        ▼              ▼              ▼              ▼
Explanation      Visualization    Question     Learning Path
Engine              Engine         Engine          Engine

Mọi Engine phía trên chỉ làm việc với Learning Content Model.

---

## 5.3 Core Principles

Learning Content Model được xây dựng theo các nguyên tắc sau:

LCM-01

Tách biệt dữ liệu nghiệp vụ khỏi nội dung học tập.

---

LCM-02

Không phụ thuộc Database.

---

LCM-03

Không phụ thuộc Repository.

---

LCM-04

Không phụ thuộc giao diện người dùng.

---

LCM-05

Có thể mở rộng cho mọi môn học.

---

LCM-06

Mọi AI Engine sử dụng chung một mô hình dữ liệu.

---

## 5.4 Learning Content Structure

Một Learning Content bao gồm:

Metadata

↓

Learning Objectives

↓

Prerequisites

↓

Learning Units

↓

Assessment

↓

Next Learning

Trong đó Learning Units là thành phần trung tâm.

---

## 5.5 Learning Unit

Learning Unit là đơn vị nội dung học tập cơ bản của EduFormula AI.

Một Learning Unit đại diện cho một khối kiến thức có thể:

- được giải thích
- được minh họa
- được kiểm tra
- được đánh giá
- được đưa vào lộ trình học

Learning Unit không phụ thuộc việc nội dung đó có công thức hay không.

---

## 5.6 Learning Unit Types

Trong phiên bản hiện tại, Specification chỉ xác định rằng:

Learning Unit có thể được mở rộng thành nhiều loại nội dung khác nhau.

Danh sách các loại Learning Unit sẽ được định nghĩa trong các BUILD tiếp theo.

Kiến trúc không giới hạn số lượng hoặc loại Learning Unit.

---

## 5.7 Relationship with Foundation Platform

Foundation Platform chịu trách nhiệm:

- quản lý dữ liệu
- lưu trữ
- truy xuất

Content Engine chịu trách nhiệm:

- tổ chức nội dung học tập
- chuẩn hóa biểu diễn
- cung cấp dữ liệu cho các Engine

Hai tầng này độc lập và giao tiếp thông qua Content Mapper.

# 7. Content Engine Architecture

## 7.1 Architectural Overview

Content Engine là tầng trung gian giữa Foundation Platform và các Engine xử lý học tập.

Nhiệm vụ chính:

- Chuyển đổi dữ liệu từ Foundation Platform.
- Chuẩn hóa thành Learning Content Model.
- Cung cấp dữ liệu thống nhất cho các Engine.

Content Engine không thực hiện lưu trữ dữ liệu và không thay thế Repository của Foundation Platform.

---

## 7.2 Layered Architecture

EduFormula AI được tổ chức theo kiến trúc nhiều tầng.

+-----------------------------------------------------------+
|                  AI / Learning Engines                    |
|-----------------------------------------------------------|
| Explanation Engine                                        |
| Visualization Engine                                      |
| Question Engine                                           |
| Learning Path Engine                                      |
+-----------------------------------------------------------+

                         ▲
                         │

+-----------------------------------------------------------+
|                    Content Engine                         |
|-----------------------------------------------------------|
| Content Mapper                                            |
| Learning Content Model                                    |
| Content Services                                          |
+-----------------------------------------------------------+

                         ▲
                         │

+-----------------------------------------------------------+
|                 Foundation Platform                       |
|-----------------------------------------------------------|
| Repository                                                |
| Service                                                   |
| Database                                                  |
+-----------------------------------------------------------+

---

## 7.3 Main Components

Content Engine bao gồm ba thành phần chính:

### Content Mapper

Chịu trách nhiệm chuyển đổi dữ liệu từ Foundation Platform thành Learning Content Model.

---

### Learning Content Model

Biểu diễn nội dung học tập theo góc nhìn sư phạm.

Đây là mô hình dữ liệu chuẩn mà mọi Engine sẽ sử dụng.

---

### Content Services

Cung cấp API thống nhất để các Engine truy cập Learning Content.

Content Services không truy cập trực tiếp Database.

---

## 7.4 Dependency Rules

Content Engine phải tuân thủ các nguyên tắc phụ thuộc sau:

CR-01

Content Engine chỉ đọc dữ liệu từ Foundation Platform.

---

CR-02

Foundation Platform không phụ thuộc Content Engine.

---

CR-03

AI Engines không truy cập trực tiếp Repository.

---

CR-04

AI Engines chỉ sử dụng Content Services.

---

CR-05

Learning Content Model là mô hình trung gian duy nhất giữa Foundation Platform và AI Engines.

---

## 7.5 Extension Strategy

Kiến trúc phải cho phép mở rộng:

- môn học mới
- loại Learning Unit mới
- Engine mới
- AI Provider mới

mà không làm thay đổi Foundation Platform.

---

## 7.6 Architecture Principles

CAP-01

Single Responsibility.

---

CAP-02

Dependency Inversion.

---

CAP-03

Open / Closed Principle.

---

CAP-04

Composition over Inheritance.

---

CAP-05

Content-first Architecture.

# 8. Functional Requirements

## Overview

Content Engine phải cung cấp một mô hình nội dung học tập thống nhất cho toàn bộ EduFormula AI.

Mọi chức năng của Content Engine phải độc lập với Foundation Platform và được truy cập thông qua Content Services.

---

## FR-01 Learning Content Construction

Content Engine phải có khả năng xây dựng một Learning Content từ dữ liệu Foundation Platform.

Input:

- Lesson
- Knowledge
- Formula
- Variable

Output:

Learning Content

---

## FR-02 Learning Unit Construction

Content Engine phải chuyển đổi dữ liệu Foundation thành các Learning Unit.

Learning Unit là đơn vị nội dung cơ bản được các Engine sử dụng.

---

## FR-03 Metadata Generation

Content Engine phải sinh Metadata bao gồm:

- Subject
- Grade
- Chapter
- Lesson

---

## FR-04 Learning Objectives

Content Engine phải lưu trữ mục tiêu học tập của Lesson.

---

## FR-05 Prerequisites

Content Engine phải xác định các kiến thức tiền đề.

---

## FR-06 Learning Unit Organization

Content Engine phải tổ chức Learning Unit theo trình tự học tập.

---

## FR-07 Assessment Information

Content Engine phải cung cấp dữ liệu phục vụ đánh giá.

---

## FR-08 Summary

Content Engine phải cung cấp phần tổng kết bài học.

---

## FR-09 Next Learning

Content Engine phải xác định nội dung học tiếp theo.

---

## FR-10 Engine Independence

Content Engine phải cung cấp cùng một Learning Content cho:

- Explanation Engine
- Visualization Engine
- Question Engine
- Learning Path Engine

# 9. Non-functional Requirements

## NFR-01 Performance

Việc xây dựng Learning Content phải có độ trễ thấp và phù hợp với ứng dụng Desktop.

---

## NFR-02 Scalability

Kiến trúc phải hỗ trợ mở rộng:

- môn học
- cấp học
- loại Learning Unit
- Engine

mà không cần thay đổi Foundation Platform.

---

## NFR-03 Maintainability

Content Engine phải dễ bảo trì và dễ mở rộng.

---

## NFR-04 Testability

Mọi thành phần của Content Engine phải có thể kiểm thử độc lập.

---

## NFR-05 Reusability

Learning Content Model phải có khả năng tái sử dụng giữa nhiều Engine.

---

## NFR-06 Technology Independence

Content Engine không phụ thuộc:

- UI Framework
- AI Provider
- Database Engine

# 10. Acceptance Criteria

BUILD-041 được coi là hoàn thành khi:

AC-01

Learning Content Model được định nghĩa đầy đủ.

AC-02

Kiến trúc Content Engine được xác nhận.

AC-03

Mapper Pattern được xác nhận.

AC-04

Không thay đổi Foundation Platform.

AC-05

Specification được Freeze.

AC-06

ADR-002 được phê duyệt.

# 11. Test Strategy

BUILD-041A không bao gồm mã nguồn.

Việc kiểm thử tập trung vào:

- Review kiến trúc.
- Kiểm tra tính nhất quán với Blueprint.
- Kiểm tra tính nhất quán với ADR.
- Kiểm tra phạm vi (Scope).

Các Unit Test và Integration Test sẽ được thực hiện từ BUILD-041B trở đi.

# 12. Freeze Condition

Specification được Freeze khi đáp ứng:

- Blueprint v1.0
- ADR-001
- ADR-002
- Phase 3 Roadmap
- Architecture Review

Sau khi Freeze:

- Không thay đổi Learning Content Model.
- Không thay đổi Content Engine Architecture.

Mọi thay đổi kiến trúc phải được thực hiện thông qua một ADR mới.

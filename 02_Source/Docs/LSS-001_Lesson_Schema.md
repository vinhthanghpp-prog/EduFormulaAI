# LSS-001 – Lesson Schema Specification

---

## 1. Document Information

| Item | Value |
|------|-------|
| Document ID | LSS-001 |
| Document Name | Lesson Schema Specification |
| Project | EduFormula AI |
| Version | 1.0 (Draft) |
| Status | Draft |
| Author | Nguyễn Vĩnh Thăng, ChatGPT (Technical Architect) |
| Created Date | 22/07/2026 |
| Last Updated | 22/07/2026 |

---

## 2. Purpose

This document defines the standard structure of a Lesson used throughout the EduFormula AI system.

The Lesson Schema serves as the unified data contract between all software modules, ensuring consistency in lesson presentation, AI guidance, learning assessment, analytics, and reporting.

The objectives of this specification are:

- Standardize lesson data across the system.
- Support multiple learning modes.
- Enable AI-assisted learning.
- Support learning analytics.
- Support parent and teacher reporting.
- Provide a stable foundation for future expansion.

---

## 3. Scope

This specification applies to all modules that create, read, process or analyze lesson data, including:

- Lesson Editor
- Lesson Viewer
- Learning Runtime
- AI Teacher
- Assessment Engine
- Learning Analytics
- Parent Dashboard
- Teacher Dashboard
- Future AI modules

Any component that uses Lesson data must comply with this specification.

---

## 4. Design Principles

The Lesson Schema shall follow the following design principles.

### Principle 1 – Single Source of Truth

Lesson is the single source of truth for all learning content.

---

### Principle 2 – Data First

Lesson stores data only.

Business logic belongs to the Learning Engine.

Presentation logic belongs to the User Interface.

AI logic belongs to the AI Teacher.

---

### Principle 3 – Modular Structure

Each learning component shall be organized into independent content blocks that can be added, removed or extended without affecting other modules.

---

### Principle 4 – Extensibility

The schema shall support future learning features without requiring structural redesign.

---

### Principle 5 – Validation

Every Lesson shall satisfy predefined validation rules before it can be published.

---

### Principle 6 – Reusability

A Lesson can be reused by different modules without modification.

---

### Principle 7 – Technology Independence

The Lesson Schema is independent of any programming language, database or user interface implementation.
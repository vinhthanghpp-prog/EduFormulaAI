# BUILD-043A
# Learning Content Block Specification

Version:
1.0 Official

Status:
Official Draft

Milestone:
Phase 3

Author:
EduFormula AI

---

# 1. Objective

This specification defines the canonical educational content structure
used throughout EduFormula AI.

Every learning lesson SHALL be represented as a hierarchy of
Learning Units and Content Blocks.

This model becomes the single source of truth for all educational
engines.

---

# 2. Architecture

LearningContent
│
├── Metadata
│
└── LearningUnit
      │
      └── ContentBlock
              │
              ├── ConceptBlock
              ├── FormulaBlock
              ├── ExampleBlock
              ├── TipBlock
              ├── WarningBlock
              └── SummaryBlock

---

# 3. Design Principles

The Content Block Model SHALL satisfy:

- Single Responsibility Principle
- Extensibility
- Educational readability
- Deterministic processing
- Engine independence
- Future AI compatibility

---

# 4. LearningContent

LearningContent represents an entire lesson.

Responsibilities

- Store metadata
- Store learning units
- Preserve learning order

LearningContent SHALL NOT contain rendering logic.

---

# 5. LearningUnit

LearningUnit groups educational content into logical sections.

Examples

- Introduction
- Concept
- Formula
- Practice
- Summary

Each LearningUnit SHALL contain zero or more Content Blocks.

---

# 6. ContentBlock

ContentBlock is the abstract educational unit.

Every ContentBlock SHALL contain:

id
type
title
content
order
difficulty

Definitions

id

Unique identifier.

type

Educational block type.

title

Visible title.

content

Educational content.

order

Display order.

difficulty

Learning difficulty.

Allowed values

easy

medium

hard

Future values MAY be introduced.

---

# 7. Block Types

## 7.1 ConceptBlock

Purpose

Explain concepts.

Used by

Concept Generator

Visualization Engine

Question Engine

---

## 7.2 FormulaBlock

Purpose

Represent mathematical formulas.

Additional fields MAY include

formula

latex

variables

Used by

Formula Generator

Visualization Engine

Equation Renderer

---

## 7.3 ExampleBlock

Purpose

Provide worked examples.

Used by

Example Generator

Question Engine

Adaptive Learning

---

## 7.4 TipBlock

Purpose

Provide learning tips.

Examples

Memory tricks

Study advice

Exam hints

---

## 7.5 WarningBlock

Purpose

Highlight common mistakes.

Examples

Frequent misconceptions

Calculation errors

Notation errors

---

## 7.6 SummaryBlock

Purpose

Summarize lesson knowledge.

Used by

Revision Mode

Flash Cards

Learning Review

---

# 8. Processing Pipeline

Markdown

↓

Parser

↓

ContentBlock

↓

LearningUnit

↓

LearningContent

↓

Educational Engines

---

# 9. Educational Engines

The following engines SHALL consume Content Blocks.

Explanation Engine

Visualization Engine

Formula Engine

Question Engine

Learning Path Engine

Analytics Engine

Adaptive Learning Engine

---

# 10. Ordering Rules

Blocks SHALL be processed by ascending order.

Example

Concept

↓

Formula

↓

Example

↓

Tip

↓

Warning

↓

Summary

---

# 11. Validation Rules

Each block SHALL satisfy

- Valid type
- Non-empty title
- Non-empty content
- Valid order
- Valid difficulty

---

# 12. Future Extensions

Future versions MAY introduce

AnimationBlock

VideoBlock

QuizBlock

ExperimentBlock

InteractiveBlock

ReferenceBlock

These SHALL inherit from ContentBlock.

---

# 13. Non Responsibilities

Content Blocks SHALL NOT

Store UI information

Store rendering information

Generate explanations

Generate questions

Access databases

Call AI services

---

# 14. Acceptance Criteria

BUILD-043A is complete when

✓ Specification completed

✓ Architecture approved

✓ Educational structure approved

✓ Future extensions supported

✓ Ready for Domain Model

---

# 15. Development Roadmap

BUILD-043A

Content Block Specification

↓

BUILD-043B

Content Block Domain Model

↓

BUILD-043C

Content Parser Foundation

↓

BUILD-043D

Parser Integration

↓

BUILD-043E

Parser Validation

↓

BUILD-043F

Refactor

↓

BUILD-043G

Freeze

---

# 16. Notes

The Content Block Model becomes the canonical educational
structure of EduFormula AI.

All educational engines SHALL consume Content Blocks instead
of raw lesson data.

This architecture minimizes coupling,
maximizes extensibility,
and prepares the platform for AI-assisted content generation.

---

END OF DOCUMENT
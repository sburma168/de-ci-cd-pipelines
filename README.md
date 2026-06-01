# 🚀 CI/CD Pipelines — Hands-On Lesson

Welcome! This repository is designed to help you **learn CI/CD (Continuous Integration and Continuous Delivery)** using real GitHub Actions pipelines.

---

## 📁 Repository Structure

```
de-ci-cd-pipelines/
├── .github/
│   └── workflows/
│       ├── ci.yml                # ✅ CI pipeline — runs on every push & PR
│       ├── cd.yml                # 🚀 CD pipeline — deploys on merge to main
│       └── broken-pipeline.yml   # ❌ Intentionally broken — for debugging practice
├── src/
│   └── calculator.py             # Simple Python app
├── tests/
│   └── test_calculator.py        # Unit tests for the app
├── README.md                     # This file
├── LESSON.md                     # 👩‍🏫 Instructor guide
├── STUDENT_EXERCISE.md           # 🧑‍💻 Student hands-on exercises
└── requirements.txt              # Python dependencies
```

---

## 🎯 What You Will Learn

- ✅ What CI/CD is and why it matters
- ✅ How a pipeline is triggered (push, pull request, merge)
- ✅ How to read pipeline logs in the Actions tab
- ✅ What happens when a build breaks — and how to fix it
- ✅ How CI acts as a quality gate on Pull Requests
- ✅ The difference between CI and CD

---

## ⚡ Quick Start

1. **Fork this repository** (click `Fork` top-right)
2. Go to the **Actions** tab to see the pipelines run
3. Follow the exercises in [`STUDENT_EXERCISE.md`](./STUDENT_EXERCISE.md)

---

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **CI/CD:** GitHub Actions
- **Testing:** pytest
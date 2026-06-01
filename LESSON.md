# 👩‍🏫 Instructor Guide — CI/CD Lesson

**Total time:** ~60 minutes  
**Level:** Beginner to Mid  
**Prerequisites:** Students should have a GitHub account and basic Git knowledge (commit, push, pull request).

---

## Section 1: Introduction (10 min)

### 🎯 Goal
Give students a mental model of what CI/CD is and why teams use it.

### 💬 Talking Points

**What is CI (Continuous Integration)?**
> "Every time a developer pushes code, an automated process runs to check that nothing is broken. This catches bugs early — before they reach other developers or customers."

**What is CD (Continuous Delivery/Deployment)?**
> "Once code passes all checks, it's automatically packaged and delivered to a staging or production environment. No manual steps needed."

**Why does it matter?**
> "Without CI/CD, teams would manually run tests and deploy code — slow, error-prone, and inconsistent. CI/CD makes the process fast, reliable, and repeatable."

### 📖 Key Terms to Define
| Term | Simple Definition |
|------|------------------|
| **Pipeline** | A sequence of automated steps that run when code changes |
| **Trigger** | The event that starts a pipeline (e.g. a push or PR) |
| **Job** | A group of steps that run on one machine |
| **Step** | A single action inside a job (e.g. "run tests") |
| **Artifact** | A file produced by the pipeline (e.g. a build package) |
| **Environment** | Where the app runs — staging, production, etc. |

---

## Section 2: Tour the Repo (5 min)

### 🎯 Goal
Orient students to the repository structure before diving in.

### 💬 What to Show
- Open the repo on GitHub and walk through each file/folder
- Point out `.github/workflows/` — explain this is where ALL pipelines live
- Open `src/calculator.py` — "This is our app. Super simple so we can focus on the pipeline, not the code."
- Open `tests/test_calculator.py` — "These are our automated tests. The CI pipeline runs these."

---

## Section 3: Live Demo — The CI Pipeline (15 min)

### 🎯 Goal
Show students a real pipeline running and teach them how to read it.

### 💬 Step-by-Step Demo
1. Open `.github/workflows/ci.yml` — read through it together, explaining each commented section
2. Go to the **Actions** tab — show any existing runs
3. Make a small, harmless change (e.g. add a comment to `calculator.py`)
4. Commit and push directly to `main`
5. Go to **Actions** tab — watch the pipeline appear and run in real time
6. Click into the run → click the job → expand each step to show the logs
7. Point out the green checkmarks ✅

### 💡 Tips
- Zoom in on the logs — students often haven't seen them before
- Point out that the virtual machine is spun up fresh each time

---

## Section 4: Breaking the Build (10 min)

### 🎯 Goal
Show students what a failing pipeline looks like and how to read the error.

### 💬 Step-by-Step Demo
1. Open `src/calculator.py`
2. Change the `add` function to return `a - b` instead of `a + b` (introduce a bug)
3. Commit and push
4. Go to **Actions** — watch the pipeline turn ❌ red
5. Click into the failed run → find the failing test in the logs
6. Show the error message: `AssertionError` — explain what it means
7. Fix the bug (change back to `a + b`), push again, watch it go ✅ green

### 💡 Tips
- Ask students: *"What would happen if this broken code got deployed to customers?"*
- This is the "aha moment" — CI caught the bug before it caused damage

---

## Section 5: Pull Request Gates (10 min)

### 🎯 Goal
Show how CI blocks a PR from merging when tests fail.

### 💬 Step-by-Step Demo
1. Create a new branch: `git checkout -b demo-broken-pr`
2. Introduce the same bug in `add()` again
3. Push the branch and open a Pull Request to `main`
4. Show the PR page — point out the CI check at the bottom showing ❌
5. Show that the **"Merge" button is blocked** (or shows a warning)
6. Fix the bug, push to the same branch
7. Watch the CI check turn ✅ green — now the PR can be merged
8. Merge it and switch to the **Actions** tab — the CD pipeline now triggers!

---

## Section 6: The CD Pipeline (10 min)

### 🎯 Goal
Show how CD automatically deploys after code merges to main.

### 💬 Step-by-Step Demo
1. Open `.github/workflows/cd.yml` — read through it together
2. Point out: *"Notice we run the tests AGAIN before deploying — we never deploy broken code"*
3. Show the merge from Section 5 triggered the CD pipeline
4. Click into the CD run and show the simulated deployment steps
5. Explain: *"In a real project, the deploy step would push to AWS, Azure, Heroku, etc."*

### 💬 Key Talking Point
> "CI checks the code. CD ships the code. Together they make a complete automated pipeline from developer laptop to live environment."

---

## Section 7: Debug Exercise (10 min)

### 🎯 Goal
Let students practice independently by fixing a broken pipeline.

### 💬 Instructions
- Point students to `STUDENT_EXERCISE.md`
- Walk through Exercise 4 instructions with them
- Let them work independently or in pairs
- Circulate and give hints if needed (the missing step is `pip install -r requirements.txt`)
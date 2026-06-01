# 🧑‍💻 Student Exercises — CI/CD Hands-On

Work through these exercises at your own pace. Each one builds on the last.  
**You will need:** A GitHub account and a fork of this repository.

---

## 🍴 Before You Start — Fork the Repo

1. Click the **Fork** button at the top-right of this repository
2. This creates your own personal copy where you can make changes
3. All exercises below are done on **your fork**

---

## Exercise 1: Explore a Pipeline Run (Beginner)

**Goal:** Find a pipeline run and understand what you're looking at.

### Steps
1. Go to your forked repo on GitHub
2. Click the **Actions** tab at the top
3. Find a workflow run in the list and click on it
4. Click on the job name (e.g. "Run Unit Tests")
5. Expand each step by clicking on it

### ❓ Answer These Questions
1. What was the **trigger** for this pipeline run? (look at the top of the run page)
2. How many **steps** does the CI pipeline have?
3. How long did the pipeline take to run? (shown next to each step)

> 💡 **Hint:** The trigger is shown near the top of the run summary page.

---

## Exercise 2: Break the Build — Then Fix It (Beginner–Mid)

**Goal:** See what a failing pipeline looks like, then fix it.

### Steps
1. In your forked repo, open `src/calculator.py`
2. Click the ✏️ pencil icon to edit the file
3. Find the `add` function and change `return a + b` to `return a - b`
4. Scroll down and click **"Commit changes"** (commit directly to `main`)
5. Go to the **Actions** tab — watch the pipeline run and **fail** ❌
6. Click into the failed run and find the error in the logs

### 🔍 Find the Error
- Which test failed?
- What did the test expect vs. what did it get?

### Fix It
7. Go back to `src/calculator.py` and fix the bug (change back to `a + b`)
8. Commit the change
9. Watch the pipeline go **green** ✅

> 💡 **Hint:** Look for `FAILED` and `AssertionError` in the logs to find the problem.

---

## Exercise 3: Open a Pull Request with CI Gates (Mid)

**Goal:** Experience how CI blocks a bad PR from being merged.

### Steps
1. In your forked repo, create a new branch:
   - Click the branch dropdown (shows "main") → type `my-feature` → click "Create branch"
2. On the `my-feature` branch, edit `src/calculator.py` and introduce a bug again (`a - b` in `add`)
3. Commit the change to the `my-feature` branch
4. Click **"Compare & pull request"** to open a PR from `my-feature` → `main`
5. On the PR page, scroll down to the checks section

### ❓ Observe
- What does the CI check show? ✅ or ❌?
- Is the Merge button available or blocked?

### Fix the Bug
6. Go back to `src/calculator.py` on the `my-feature` branch and fix the bug
7. Commit the fix
8. Watch the CI check on the PR update to ✅ green
9. Now merge the PR!

> 💡 **Hint:** After merging, check the Actions tab — do you see a new pipeline run? Which one?

---

## Exercise 4: Debug the Broken Pipeline (Mid)

**Goal:** Find and fix a deliberate bug in a pipeline YAML file.

### Steps
1. Create a new branch called exactly: `fix-the-pipeline`
   - Click the branch dropdown → type `fix-the-pipeline` → click "Create branch"
2. On that branch, open `.github/workflows/broken-pipeline.yml`
3. **Push any small change** to the `fix-the-pipeline` branch to trigger the pipeline
   - (e.g. add a comment `# testing` to the broken-pipeline.yml file)
4. Go to **Actions** → find the "Broken Pipeline" run → watch it **fail** ❌
5. Read the error logs carefully

### 🔍 Find the Bug
- What error do you see?
- Compare `broken-pipeline.yml` to `ci.yml` — what step is missing?

### Fix It
6. Edit `broken-pipeline.yml` and add the missing step
7. Commit the change to the `fix-the-pipeline` branch
8. Watch the pipeline go **green** ✅

> 💡 **Hint:** The error will say something like `pytest: command not found`. Why would that happen?

---

## 🎓 Reflection — What Did You Learn?

Take 5 minutes to answer these questions (write them down or discuss with a partner):

1. **What is the difference between CI and CD?**
2. **Why is it important to run tests automatically on every push?**
3. **What is a "quality gate" and how does GitHub enforce it on Pull Requests?**
4. **If you were working on a team of 10 developers, how would CI/CD help you?**
5. **What was the most surprising thing you discovered doing these exercises?**

---

## ✅ You're Done!

You've just experienced a real CI/CD workflow — the same kind used by professional software teams every day. 🎉
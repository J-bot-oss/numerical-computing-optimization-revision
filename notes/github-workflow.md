# GitHub workflow: meaningful contributions

## First upload using Git Bash on Windows

1. Download and extract this folder. Open the folder in VS Code.
2. Open a terminal **inside** the repository folder.
3. On GitHub, create an **empty** repository named `numerical-computing-optimization-revision` (do not initialize it with another README).
4. In Git Bash (replace `YOUR_USERNAME`):

```bash
git init
git add .
git commit -m "chore: start numerical computing revision lab"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/numerical-computing-optimization-revision.git
git push -u origin main
```

GitHub may open a browser for authentication; do not paste secrets into the repository.

## Daily study-to-commit loop

1. Pick **one question or misconception** from the notes.
2. Solve it **by hand**; explain the method in your own words.
3. Implement or improve the code, add a meaningful test and run `python -m pytest -q`.
4. Update `progress/REVISION_LOG.md` with date, topic, evidence and next gap.
5. Review your changed files with `git diff`.
6. Commit only the work you actually completed:

```bash
git status
git add notes/ progress/ tests/ src/
git commit -m "study: correct root bracket selection and add examples"
git push
```

Each commit should tell a truthful story about learning; multiple small commits are fine when they represent real separate changes. Don't fake dates, game contribution counts, or commit untested solutions as completed.

## If you want a visible GitHub history

Pin this repo. Keep `README.md` current, explain *why* code changes in commits, and make the tests pass using the supplied GitHub Actions workflow. A well-documented working repository is a better signal than a large number of empty commits.

## Privacy and academic integrity

Don't upload your original signed examination sheets, grades, student IDs, passwords, private datasets or other students' work. Use your own explanations and original practice exercises. Keep exam scans local unless you have explicit permission to publish them.

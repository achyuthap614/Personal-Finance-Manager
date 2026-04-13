# Git Quick Start - For Your Next Projects

## Copy-Paste Commands for Your Next Project

### Template 1: New Local Project → Push to GitHub

```bash
# 1. Create folder and navigate
mkdir my-project
cd my-project

# 2. Create your files and folders
# (create your code files)

# 3. Initialize git
git init

# 4. Create .gitignore (copy-paste the content below)
# (Create file named .gitignore in project root)

# 5. Add and commit
git add .
git commit -m "Initial commit: [Your project description]"

# 6. Go to GitHub.com and CREATE NEW REPOSITORY
# - Name it: my-project
# - Don't initialize with README, .gitignore, license
# - Copy the HTTPS url

# 7. Add remote (replace URL with yours)
git remote add origin https://github.com/YOUR-USERNAME/my-project.git

# 8. Push to GitHub
git branch -M main
git push -u origin main

# DONE! Check your GitHub repo online ✓
```

### Template 2: Clone Existing Project

```bash
# 1. Clone repository
git clone https://github.com/username/project-name.git
cd project-name

# 2. Create feature branch
git checkout -b feature/your-feature
# or
git switch -c feature/your-feature

# 3. Make your changes
# (edit files)

# 4. Stage and commit
git add .
git commit -m "feat: Describe your changes"

# 5. Push to GitHub
git push -u origin feature/your-feature

# 6. Create Pull Request on GitHub (web interface)

# 7. After merge, clean up locally
git checkout main
git pull origin main
git branch -d feature/your-feature
```

### Template 3: Collaborate on Team Project

```bash
# 1. Clone once
git clone https://github.com/team/repo.git
cd repo

# 2. Daily workflow - START
git checkout main
git pull origin main                # Get latest

# 3. Create feature branch
git checkout -b feature/my-feature

# 4. Work and commit multiple times
# (edit file 1)
git add file1.py
git commit -m "Part 1: Add feature"

# (edit file 2)
git add file2.py
git commit -m "Part 2: Complete feature"

# 5. Before pushing, check if main was updated
git fetch origin

# If it was:
git rebase origin/main
# or
git merge origin/main

# 6. Push your feature branch
git push -u origin feature/my-feature

# 7. Create Pull Request on GitHub
# - Describe your changes
# - Request reviewers
# - Wait for approval

# 8. After approval, merge on GitHub
# (Can be done in web UI)

# 9. Update your main locally
git checkout main
git pull origin main

# 10. Cleanup
git branch -d feature/my-feature
git push origin --delete feature/my-feature
```

---

## .gitignore Template for Different Projects

### Python Project
```
# Python
__pycache__/
*.py[cod]
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
ENV/
env/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Testing
.pytest_cache/
.coverage
htmlcov/

# Data files
*.db
*.sqlite
*.json (optional - if you want to share data)

# Environment variables
.env
.env.local
```

### JavaScript/Node.js Project
```
# Dependencies
node_modules/
npm-debug.log
yarn-error.log
package-lock.json (optional)

# Production
dist/
build/
.next/

# IDE
.vscode/
.idea/
*.swp

# Environment
.env
.env.local
.env.*.local

# OS
.DS_Store
Thumbs.db

# Testing
coverage/
.nyc_output/
```

### Web Project (HTML/CSS/JS)
```
# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Build
dist/
build/

# Dependencies
node_modules/

# Environment
.env
.env.local
```

---

## Essential Commands You'll Use Most

### Daily Commands
```bash
# Check what you changed
git status

# See your changes
git diff

# Save your work
git add .
git commit -m "Your message"

# Get latest from others
git pull

# Send your changes
git push
```

### Switch Work
```bash
# Create new branch
git checkout -b feature-name

# Switch to branch
git checkout branch-name

# Back to main
git checkout main
```

### Fix Mistakes
```bash
# Undo uncommitted changes
git restore filename

# Undo last commit (keep changes)
git reset HEAD~1

# Undo old commit (create new commit that undoes it)
git revert commit-hash
```

### Review History
```bash
# See commits
git log --oneline

# See visual history
git log --graph --oneline --all

# See who changed what
git blame filename
```

---

## Decision Trees - When to Use What

### "I want to switch to a different branch"

```
Do you have uncommitted changes?
├─ NO → git checkout branch-name
└─ YES → 
    ├─ Save for later? → git stash → git checkout branch-name
    ├─ Commit them? → git add . → git commit → git checkout branch-name
    └─ Discard them? → git restore . → git checkout branch-name
```

### "I made a mistake in my commit"

```
Is it the LAST commit?
├─ YES (just now) →
│   ├─ Wrong message? → git commit --amend
│   ├─ Wrong files? → git reset HEAD~1 → fix → git add . → git commit
│   └─ Wrong everything? → git reset --hard HEAD~1
└─ NO (older commit) →
    └─ Create undoing commit → git revert commit-hash
```

### "How do I fix a merge conflict?"

```
Merge Conflict happened!
├─ See conflicted files: git status
├─ Open conflicted file
├─ Find: <<<<<<< HEAD ... ======= ... >>>>>>> branch
├─ Keep what you want, delete markers
├─ Save file
├─ Mark resolved: git add filename
└─ Complete: git commit
```

### "I want to push but I'm worried"

```
Before you push:
├─ Check what you're sending: git log -3 --oneline
├─ See changes: git diff origin/main..main
├─ Review: git status
└─ Ready? → git push
```

---

## Git Tips & Tricks

### 1. Keyboard Shortcut Aliases

Add these to your git config to save typing:

```bash
# Run this once:
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --graph --oneline --all'

# Now use:
git co main                # instead of: git checkout main
git ci -m "msg"           # instead of: git commit -m "msg"
git st                    # instead of: git status
git visual                # Visual history
```

### 2. One-Line Visual History

```bash
git log --graph --oneline --all --decorate

Output:
* 7g8h9i (main) Fix critical bug
* 4d5e6f Merge pull request #5
|\
| * 2c3d4e (feature/new-ui) Add new interface
| * 1a2b3c Start new feature
|/
* 0z9y8x Initial commit
```

### 3. See What You're About to Push

```bash
git log -3 --oneline     # See what's ready
git diff origin/main     # See exact changes
```

### 4. Interactive Rebase (Advanced)

```bash
# Cleanup last 3 commits before pushing
git rebase -i HEAD~3

# Interactive menu appears:
# pick 1a2b3c First commit
# pick 2c3d4e Second commit
# pick 3d4e5f Third commit
#
# Commands:
# p (pick) - use commit
# r (reword) - use, but rewrite message
# s (squash) - combine with previous
# f (fixup) - combine, discard message
# d (drop) - remove commit
```

### 5. Stash With Name

```bash
git stash save "WIP: fixing auth bug"
git stash list
git stash pop stash@{0}
```

### 6. See Changes by Author

```bash
git log --author="Your Name" --oneline
git log --since="2 weeks ago"
git log --grep="bug"
```

### 7. Compare Branches

```bash
git diff main..feature
git log main..feature      # Commits in feature but not main
git log --left-right main..feature
```

---

## Common Git Problems & Fixes

### Problem: "git: command not found"
```
Solution: Git is not installed
Fix: 
- Windows: Download from git-scm.com
- Mac: brew install git
- Linux: sudo apt install git
```

### Problem: "fatal: not a git repository"
```
Solution: You're not in a git project
Fix: 
- cd to project folder
- Or initialize: git init
```

### Problem: "Please tell me who you are"
```
Solution: Git user not configured
Fix: 
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

### Problem: "Permission denied (publickey)"
```
Solution: SSH key not set up
Fix:
- Use HTTPS instead: git clone https://...
- Or setup SSH: Follow GitHub SSH guide
```

### Problem: "CONFLICT (content conflict in file)"
```
Solution: Merge conflict
Fix: See "How do I fix merge conflict" section above
```

### Problem: "Your branch is ahead of 'origin/main' by 3 commits"
```
Solution: You haven't pushed yet
Fix: git push
```

### Problem: "Your branch is behind... by 2 commits"
```
Solution: Remote has new commits
Fix: git pull
```

---

## GitHub Workflow Tips

### Creating a Good Pull Request

```
✓ Title: Clear, concise
  Example: "Fix: Date validation in transaction input"

✓ Description: Explain what and why
  Example: 
  "This PR fixes the date validation bug where invalid dates 
   were being accepted. Changed the validation logic to require 
   YYYY-MM-DD format and added error message."

✓ Link to issue: "Fixes #123"

✓ Screenshots: If UI changes

✓ Before/After: Show the difference
```

### Code Review Best Practices

```
When REVIEWING code:
- Be kind and constructive
- Suggest improvements, don't demand
- Ask questions if unclear
- Test locally if possible
- Approve when satisfied

When RECEIVING review:
- Don't take feedback personally
- Ask for clarification
- Make requested changes in new commit
- Thank reviewer
- Push updated code
```

### Protecting Your Main Branch

```
On GitHub → Settings → Branches → Add Rule:
✓ Require pull request reviews before merging
✓ Dismiss stale pull request approvals
✓ Require status checks to pass (if using CI/CD)
✓ Require branches to be up to date

This prevents accidents! :)
```

---

## Practice Exercise

Try this to practice:

```bash
# 1. Create practice repository
mkdir git-practice
cd git-practice
git init

# 2. Create initial file
echo "# My Project" > README.md
git add README.md
git commit -m "Initial commit"

# 3. Create feature branch
git branch -M main
git checkout -b feature/first-feature

# 4. Make changes
echo "## Feature 1" >> README.md
git add README.md
git commit -m "Add feature 1"

# 5. Switch back to main
git checkout main

# 6. View log
git log --oneline --graph --all

# 7. Merge
git merge feature/first-feature

# 8. Cleanup
git branch -d feature/first-feature

# 9. View final log
git log --oneline

# 10. When ready, push to GitHub:
#     git remote add origin <your-github-repo-url>
#     git push -u origin main
```

---

## Resources for Further Learning

### Official Documentation
- Git Documentation: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com
- Interactive Git Tutorial: https://learngitbranching.js.org

### Useful Tools
- GitHub Desktop: Visual Git client
- GitKraken: Popular GUI
- VS Code Git Extension: Built-in

### Common Workflows
- Git Flow: https://nvie.com/posts/a-successful-git-branching-model/
- GitHub Flow: https://guides.github.com/introduction/flow/
- Trunk-Based Development: Modern CI/CD approach

---

## Summary for Your Next Projec

```
Quick Recipe:
1. mkdir project && cd project
2. Create your files
3. git init
4. Create .gitignore
5. git add .
6. git commit -m "Initial commit"
7. Create GitHub repository
8. git remote add origin <URL>
9. git push -u origin main
10. Done! ✓

Then going forward:
- Make changes
- git add . && git commit -m "message"
- git push

For teams:
- Branches before new features
- Pull requests for code review
- Merge when approved
```

---

Good luck with your projects! 🚀


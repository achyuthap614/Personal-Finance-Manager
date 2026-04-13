# Git Commands Reference - Complete Guide

## Part 2: Git Fundamentals & Complete Commands Reference

---

## Git Fundamentals - Core Concepts

### 1. Three States of Git Files

Every file in Git exists in one of three states:

```
┌──────────────────────────────────────────────────────────────────────┐
│                    GIT FILE LIFECYCLE                                │
└──────────────────────────────────────────────────────────────────────┘

WORKING DIRECTORY          STAGING AREA (Index)      REPOSITORY (History)
(Your computer)            (Waiting to save)         (Committed & safe)

    main.py ✗              ───git add───►   main.py ✓    ───git commit───► main.py ✓
  (untracked)              (staged)                       (committed)

    main.py ✗              ───git add───►   main.py ✓
  (modified)               (staged)

    main.py  (gone)        ───git rm───►    main.py ✗    ───git commit───► (deleted)
  (deleted)                (staged)

```

### 2. How Git Stores Data

```
Your Repository Structure:

.git/
├── objects/              ← Individual file contents (hashed/compressed)
│   ├── blobs/           ← File data
│   ├── trees/           ← Directory structures
│   ├── commits/         ← Commit metadata
│   └── tags/            ← Tags
├── refs/                ← Pointers to commits
│   ├── heads/           ← Branch pointers
│   │   └── main         ← Points to latest commit on main
│   └── tags/
├── HEAD                 ← Points to current branch
├── config               ← Repository settings
└── index                ← Staging area

Your Project:
├── main.py
├── accounts/
└── ... (actual files)
```

### 3. Commits Form a Timeline

```
Commit 1          Commit 2          Commit 3 (current)
  1a2b3c ×         4d5e6f ×          7g8h9i ←
  │                │                 │
  Initial          Added user        Fixed bug
  commit           auth              in login
  │                │                 │
  Author: You      Author: You       Author: You
  │                │                 │
  parent: None  ←──parent: 1a2b3c ←──parent: 4d5e6f

Timeline:
1a2b3c → 4d5e6f → 7g8h9i
(past)           (present)

Each commit points to parent commit, forming chronological history ✓
```

---

## Complete Git Commands Reference

### Configuration Commands

```bash
# Set user information
git config user.name "Your Name"
git config user.email "your@email.com"

# Set globally (all projects on computer)
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# View config
git config --list                    # Show all settings
git config user.name                 # Show specific setting
git config --list --global           # Show global settings

# Edit config file
git config --global --edit           # Opens editor to edit config

# Set editor for commit messages
git config --global core.editor "code"  # VS Code
git config --global core.editor "nano"  # Nano editor
git config --global core.editor "vim"   # Vim editor
```

### Initialize & Clone

```bash
# Initialize new repository
git init                              # Create .git folder

# Clone existing repository
git clone https://github.com/user/repo.git              # Clone to new folder
git clone https://github.com/user/repo.git my-folder   # Clone to specific folder
git clone --depth 1 https://github.com/user/repo.git   # Clone only latest commit (faster)
git clone --branch main https://github.com/user/repo.git  # Clone specific branch
```

### Status & Inspection Commands

```bash
# Check status
git status                           # Short form: git status -s
git status -s                        # Short output format

# View changes
git diff                             # Changes in working directory
git diff --staged                    # Changes in staging area
git diff HEAD                        # All changes since last commit
git diff main develop                # Differences between branches
git diff commit1 commit2             # Between specific commits
git diff --name-only                 # Only show changed filenames

# View commit history
git log                              # Full history
git log --oneline                    # One line per commit
git log --graph --oneline --all      # Visual branch history
git log -5                           # Last 5 commits
git log --author="Author Name"       # Commits by specific author
git log --since="2 weeks ago"        # Recent commits
git log --grep="bug fix"             # Commits with "bug fix" in message
git log -p                           # Show changes in each commit
git log --stat                       # Show file statistics

# View specific commit
git show commit-hash                 # Show commit details and changes
git show commit-hash:filename        # Show file at specific commit
git blame filename                   # Show who changed each line

# Find commits
git log --all --grep="pattern"       # Search commit messages
git log -S "code snippet"            # Find commits containing code
git log --author="name"              # Commits from author
git reflog                           # Show all reference logs (recovery)
```

### Staging Commands

```bash
# Add files to staging
git add filename                     # Add specific file
git add *.py                         # Add all Python files
git add folder/                      # Add entire folder
git add .                            # Add all changes in current directory
git add -A                           # Add all changes in repo
git add --all                        # Same as -A
git add -p                           # Interactive: choose chunks to add
git add -i                           # Interactive mode

# Remove files from staging
git reset filename                   # Unstage file (keep changes)
git reset                            # Unstage all files
git restore --staged filename        # Same as reset (newer git)

# View staging area
git diff --staged                    # See staged changes
git diff --cached                    # Same as --staged
```

### Commit Commands

```bash
# Create commits
git commit -m "message"              # Commit with message
git commit -m "Line 1" -m "Line 2"  # Multi-line message
git commit --amend                   # Modify last commit
git commit --amend --no-edit         # Add files to last commit without changing message
git commit -am "message"             # Stage and commit tracked files

# Undo commits
git revert hash                      # Create new commit undoing changes
git reset HEAD~1                     # Undo last commit, keep changes
git reset --soft HEAD~1              # Undo commit, keep in staging
git reset --hard HEAD~1              # Undo commit, throw away changes (⚠️ dangerous!)

# Cherry-pick (copy specific commits)
git cherry-pick hash                 # Copy commit to current branch
git cherry-pick hash1 hash2 hash3    # Copy multiple commits
```

### Branching Commands

```bash
# Create branches
git branch                           # List branches (current marked with *)
git branch -a                        # List all branches (local + remote)
git branch branch-name               # Create new branch
git branch -d branch-name            # Delete branch (safe: only if merged)
git branch -D branch-name            # Force delete branch
git branch -m old-name new-name      # Rename branch
git branch -M new-name               # Force rename

# Switch branches
git checkout branch-name             # Switch to branch
git checkout -b branch-name          # Create and switch to branch
git switch branch-name               # Switch branch (newer syntax)
git switch -c branch-name            # Create and switch (newer syntax)

# Information
git branch -v                        # Show branches with last commit
git branch --merged                  # Branches already merged to current
git branch --no-merged               # Branches not yet merged
```

### Remote Commands

```bash
# Manage remotes
git remote                           # List remotes
git remote -v                        # Show remote URLs
git remote add origin url            # Add remote
git remote remove origin             # Remove remote
git remote rename old new            # Rename remote
git remote show origin               # Show remote details
git remote set-url origin new-url    # Change remote URL

# Fetch (get updates WITHOUT merging)
git fetch                            # Fetch from origin
git fetch origin                     # Explicit: fetch from origin
git fetch origin main                # Fetch specific branch
git fetch --all                      # Fetch from all remotes

# Pull (fetch + merge)
git pull                             # Fetch and merge (recommended)
git pull origin main                 # Pull specific branch
git pull --rebase                    # Rebase instead of merge

# Push (send commits)
git push                             # Push to default remote
git push origin main                 # Push to specific branch
git push -u origin branch-name       # Push and set upstream
git push --all                       # Push all branches
git push origin --delete branch-name # Delete remote branch
git push --force                     # Force push (⚠️ use carefully!)
```

### Merge Commands

```bash
# Merge branches
git merge branch-name                # Merge branch into current
git merge --no-ff branch-name        # Merge with merge commit (visible history)
git merge --squash branch-name       # Combine all commits into one

# Handle merge conflicts
git merge --abort                    # Cancel merge
git status                           # See conflict files
# (manually edit conflicts, save file)
git add conflicted-file              # Mark conflict as resolved
git commit                           # Complete merge

# View merge history
git log --graph --oneline --all      # Visual merge history
```

### Rebase Commands (Advanced)

```bash
# Rebase (replay commits on top of new base)
git rebase branch-name               # Rebase current on branch
git rebase -i HEAD~3                 # Interactive rebase last 3 commits
git rebase --continue                # Continue after conflict
git rebase --abort                   # Cancel rebase
git rebase --skip                    # Skip current commit in rebase

# Interactive rebase options (in editor):
pick   - Use commit
reword - Use commit, edit message
squash - Combine with previous commit
fixup  - Combine, discard message
drop   - Remove commit
```

### Clean Up Commands

```bash
# Stash (temporarily save work)
git stash                            # Save changes without committing
git stash save "description"         # Save with description
git stash list                       # Show all stashes
git stash pop                        # Apply latest stash and remove it
git stash apply                      # Apply latest stash (keep it)
git stash drop                       # Delete latest stash
git stash show -p stash@{0}          # Show stash details

# Clean up
git clean -n                         # List untracked files (dry run)
git clean -f                         # Delete untracked files
git clean -fd                        # Delete untracked files and folders
git gc                               # Garbage collection (compress repo)

# Remove files
git rm filename                      # Remove from git and disk
git rm --cached filename             # Remove from git, keep on disk
git restore filename                 # Discard changes in file
```

### Tag Commands

```bash
# Create tags
git tag v1.0.0                       # Create lightweight tag
git tag -a v1.0.0 -m "Version 1"   # Annotated tag with message
git tag v1.0.0 commit-hash           # Tag specific commit

# List tags
git tag                              # List all tags
git tag -l "v1*"                     # List tags matching pattern
git show v1.0.0                      # Show tag details

# Push tags
git push origin v1.0.0               # Push specific tag
git push origin --tags               # Push all tags

# Delete tags
git tag -d v1.0.0                    # Delete local tag
git push origin --delete v1.0.0      # Delete remote tag
```

### Search & Find Commands

```bash
# Find changes
git log -S "search text"             # Find commits with code
git log --grep="pattern"             # Search commit messages
git log --author="name"              # Show author commits
git blame filename                   # Who changed each line
git bisect                           # Binary search for bug

# Find files
git log --follow --patch -- filename # History of specific file
git log --name-status                # Show which files changed
git diff-tree                        # Compare trees
```

### Undo & Recovery Commands

```bash
# View deleted commits
git reflog                           # Show reference logs
git reflog show branch-name          # Specific branch history

# Recover deleted branch
git branch recovered-branch hash     # Recreate branch at commit

# Undo changes
git restore filename                 # Discard file changes
git restore --staged filename        # Unstage file
git reset filename                   # Same as above
git reset HEAD~1                     # Undo last commit
git revert hash                      # Create commit undoing changes
git checkout -- filename             # Discard changes (older syntax)

# Nuclear options (⚠️ use with caution!)
git reset --hard HEAD                # Discard ALL changes
git reset --hard commit-hash         # Go back to specific commit
git clean -fd                        # Delete all untracked files
```

---

## Complete Git Workflows

### Workflow 1: Simple Solo Project (What We Did)

```bash
# Step 1: Start new project
cd my-project
git init

# Step 2: Create files
# (create main.py, etc.)

# Step 3: Setup git config
git config user.name "Your Name"
git config user.email "your@email.com"

# Step 4: Check status
git status

# Step 5: Stage files
git add .

# Step 6: Create first commit
git commit -m "Initial commit"

# Step 7: Connect to GitHub
git remote add origin https://github.com/yourname/project.git

# Step 8: Push to GitHub
git push -u origin main
```

### Workflow 2: Feature Branch Development

```bash
# Step 1: Create feature branch
git checkout -b feature/new-feature

# Step 2: Work on feature (make commits)
# Edit files...
git add .
git commit -m "Add new feature part 1"

# Edit more...
git add .
git commit -m "Add new feature part 2"

# Step 3: Push to GitHub
git push -u origin feature/new-feature

# Step 4: Create Pull Request on GitHub (web interface)
# GitHub shows "Compare & Pull Request" button
# Create PR, describe changes, assign reviewers

# Step 5: After review → Merge on GitHub
# (Can also merge locally)

# Step 6: Update main locally
git checkout main
git pull origin main

# Step 7: Clean up
git branch -d feature/new-feature
```

### Workflow 3: Collaborative Development

```bash
# Step 1: Clone repository
git clone https://github.com/team/project.git
cd project

# Step 2: Create your branch from main
git checkout -b feature/mywork

# Step 3: Make changes
git add .
git commit -m "My changes"

# Step 4: Before pushing, get latest
git fetch origin
git rebase origin/main              # Or: git merge origin/main

# Step 5: Push your branch
git push -u origin feature/mywork

# Step 6: Create Pull Request
# (GitHub web interface)

# Step 7: Request review from team
# (GitHub PR options)

# Step 8: Address feedback (if needed)
# Edit files...
git add .
git commit -m "Address review feedback"
git push

# Step 9: Merge when approved
git checkout main
git pull origin main
git merge feature/mywork
git push origin main
```

### Workflow 4: Bug Fix in Production

```bash
# Step 1: Create hotfix branch FROM main
git checkout main
git pull origin main                 # Get latest
git checkout -b hotfix/critical-bug

# Step 2: Fix bug
# Edit files...
git add .
git commit -m "Fix critical login bug"

# Step 3: Test thoroughly!

# Step 4: Push hotfix branch
git push -u origin hotfix/critical-bug

# Step 5: Create Pull Request and merge to main

# Step 6: Also merge to develop (if it exists)
git checkout develop
git pull origin develop
git merge hotfix/critical-bug

# Step 7: Clean up
git branch -d hotfix/critical-bug
git push origin --delete hotfix/critical-bug
```

### Workflow 5: Updating Your Fork

```bash
# Setup (first time only)
git remote add upstream https://github.com/original/project.git

# Each time you want to update:
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

---

## Common Git Scenarios & Solutions

### Scenario 1: Oops! I Committed the Wrong Files

```bash
# Situation: You committed something you shouldn't have

# Option 1: Undo commit, keep changes
git reset HEAD~1
git status                          # Check what's unstaged
# Review changes, remove what you don't want
git add correct-file.py
git commit -m "Correct commit"

# Option 2: Amend last commit
git reset HEAD filename-to-remove   # Unstage file
git commit --amend                  # Modify last commit
```

### Scenario 2: I Need to Go Back to an Old Version

```bash
# See history
git log --oneline

# View old commit
git show commit-hash

# Option 1: Create new commit that undoes changes
git revert commit-hash

# Option 2: Go back temporarily to view
git checkout commit-hash
# (Do stuff)
git checkout main                   # Go back

# Option 3: Actually go back (hard reset, loses commits!)
git reset --hard commit-hash        # ⚠️ Careful!
```

### Scenario 3: I Have Uncommitted Changes and Need to Switch Branches

```bash
# Problem: You changed files but can't switch branches
git status                          # See changes

# Option 1: Stash changes (save for later)
git stash
git checkout other-branch           # Now you can switch
# (do stuff on other branch)
git checkout original-branch
git stash pop                       # Restore changes

# Option 2: Commit changes first
git add .
git commit -m "Work in progress"
git checkout other-branch
```

### Scenario 4: Merge Conflict - Oh No!

```bash
# You tried to merge and got:
# CONFLICT (content conflict in filename.py)

# Step 1: See what's conflicting
git status                          # Shows conflicted files
git diff

# Step 2: Open file, find conflict markers
# <<<<<<< HEAD
# Your changes
# =======
# Their changes
# >>>>>>> branch-name

# Step 3: Manually edit to resolve (delete markers, keep what you want)

# Step 4: Mark as resolved
git add filename.py

# Step 5: Complete merge
git commit

# To abort if conflict is too messy:
git merge --abort                   # Start over
```

### Scenario 5: I Accidentally Deleted a Branch!

```bash
# Don't panic! Git keeps a reference log

# Find it
git reflog
# Look for output like: "abc1234 HEAD@{5}: checkout: moving from feature/deleted to main"

# Recover it
git branch recovered-branch abc1234
```

### Scenario 6: Force Push (When You Definitely Need It)

```bash
# ⚠️ DANGEROUS - only if you're sure!
git push --force origin branch-name

# Safer alternative:
git push --force-with-lease origin branch-name  # Safer, won't overwrite others' work
```

---

## Git Best Practices

### 1. ✅ Commit Often, Commit Well

```
✗ Bad:
main → [giant commit: "fixed everything"]

✓ Good:
main → [fix auth bug] → [add validation] → [update docs]

Why? Easy to revert individual changes, clear history
```

### 2. ✅ Write Meaningful Commit Messages

```
✗ Bad:
"lol"
"fix"
"asdf"

✓ Good:
"Fix date validation in transaction input"
"Refactor Account class for clarity"
"Implement account deletion feature"

Format:
[Type] [Scope] - [Description]
feat: Add new feature
fix: Fix bug
docs: Update documentation
style: Code formatting
refactor: Restructure code
test: Add tests
chore: Maintenance
```

### 3. ✅ Branch Naming Convention

```
feature/user-auth          # New feature
bugfix/login-error         # Bug fix
hotfix/critical-crash      # Emergency fix
docs/api-guide             # Documentation
refactor/code-cleanup      # Code improvement
```

### 4. ✅ Review Before Pushing

```bash
# Always check what you're pushing
git diff                   # Review changes
git status                 # See what's staged
git log --oneline -5       # Check last commits
```

### 5. ✅ Pull Before Push

```bash
# Get latest before pushing
git fetch origin
git pull origin main       # Only if main, may be different branch

# If conflict, resolve locally and push
```

### 6. ✅ Use .gitignore

```
# Always ignore:
__pycache__/               # Python cache
venv/                      # Virtual environment
*.pyc                      # Compiled Python
node_modules/              # JavaScript dependencies
.env                       # Secrets
.DS_Store                  # macOS system files
.vscode/                   # IDE settings

# Keep repo clean and small
```

### 7. ✅ Protect Main Branch

```bash
# On GitHub Settings:
# 1. Go to Settings → Branches
# 2. Add rule for "main"
# 3. Require pull request reviews
# 4. Dismiss stale reviews
# 5. Require status checks to pass
# 6. Require branches to be up to date
```

---

## Git Cheat Sheet - Quick Reference

```bash
# Setup
git init                        # Initialize repo
git clone URL                   # Copy repo
git config user.name "You"

# Check status
git status                      # What changed
git log                         # History
git diff                        # Detailed changes

# Make commits
git add .                       # Stage changes
git commit -m "Message"         # Commit
git push                        # Send to GitHub

# Branches
git branch                      # List branches
git checkout -b feature         # New branch
git merge feature               # Merge branch

# Undo
git reset HEAD~1                # Undo commit
git restore filename            # Discard changes
git revert hash                 # Undo old commit

# Remote
git remote -v                   # Show connection
git push origin main            # Send commits
git pull                        # Get updates
git fetch                       # Just get updates
```

---

## Visual Git Reference

### Git Workflow Diagram

```
Making Changes:
Working Dir → git add → Staging → git commit → Repository
  (untracked)      ↓      (index)      ↓      (history)
             loose files        ready to send

Sharing:
Local Repository → git push → GitHub
        ↓ git fetch/pull ← 
                ↓
        Update Local

Multiple Developers:
Dev A                    GitHub                Dev B
  ↓                       ↓                      ↓
Commit   → Push  →    Repository    ← Pull ← Commit
  ↓       ←────  ← Fetch ──
Get Latest
```

### Branch Merging

```
Before Merge:
    main: A → B → C
    feature: A → B → D → E

After Merge:
    main: A → B → C → (merge commit)
                ↓       ↓
    feature: A → B → D → E
                    ↓
                    Connected!
```

---


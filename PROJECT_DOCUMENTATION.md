# Personal Finance Manager - Complete Project Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Architecture & Data Structures](#architecture--data-structures)
3. [Component Breakdown](#component-breakdown)
4. [Workflow & User Flow](#workflow--user-flow)
5. [File Structure](#file-structure)
6. [Current Issues & Bugs](#current-issues--bugs)
7. [Technical Details](#technical-details)

---

## Project Overview

**Personal Finance Manager** is a command-line application that helps users manage their financial accounts and transactions. It uses a **Nested Doubly Linked List** data structure to efficiently organize and handle multiple accounts, where each account contains its own transaction history.

### Key Features:
- ✅ Create multiple user accounts
- ✅ Add and manage transactions per account
- ✅ Categorize transactions (Food, Transport, Entertainment, Bills, Medical, Other)
- ✅ Persist data in JSON format
- ✅ View account and transaction information

---

## Architecture & Data Structures

### Nested Doubly Linked List Design

The system uses a **two-layer nested linked list structure**:

```
┌─ OUTER LAYER (Account Manager) ────────────────────────────────┐
│  Doubly Linked List of Account Nodes                            │
│  ┌──────────┐      ┌──────────┐      ┌──────────┐              │
│  │ Account A│◄────►│ Account B│◄────►│ Account C│              │
│  └────┬─────┘      └────┬─────┘      └────┬─────┘              │
│       │                 │                  │                   │
│       ▼                 ▼                  ▼                   │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │INNER LAYER  │  │INNER LAYER  │  │INNER LAYER  │            │
│  │Txn Manager: │  │Txn Manager: │  │Txn Manager: │            │
│  │             │  │             │  │             │            │
│  │ ┌─────────┐ │  │ ┌─────────┐ │  │ (empty)     │            │
│  │ │Trans 1◄─┼─┼──┼─│Trans 1  │ │  │             │            │
│  │ └─────────┘ │  │ └─────────┘ │  │             │            │
│  │    ▼        │  │    ▼        │  │             │            │
│  │ ┌─────────┐ │  │             │  │             │            │
│  │ │Trans 2◄─┼─┼──│             │  │             │            │
│  │ └─────────┘ │  │             │  │             │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
└────────────────────────────────────────────────────────────────┘
```

**Why this design?**
- Each account is independent with its own transaction history
- Efficient insertion/deletion of both accounts and transactions
- Easy bidirectional traversal (prev/next pointers)
- Scalable for multiple users and many transactions

---

## Component Breakdown

### 1. **Transaction Class** (`transaction/transactions.py`)

**Purpose:** Represents a single financial transaction.

**Structure:**
```python
class Transaction:
    Date: str          # Transaction date (YYYY-MM-DD format)
    Amount: str        # Transaction amount (stored as string, should be numeric)
    Category: str      # Transaction category (food, transport, etc.)
    next: Transaction  # Pointer to next transaction
    prev: Transaction  # Pointer to previous transaction
```

**Key Points:**
- Linked list node with prev/next pointers
- Stores date, amount, and category
- Part of an inner doubly linked list within each account

---

### 2. **Transaction_manager Class** (`transaction/transactions.py`)

**Purpose:** Manages the doubly linked list of transactions for a single account.

**Methods:**

| Method | Purpose | Parameters |
|--------|---------|-----------|
| `__init__()` | Initialize empty transaction list | None |
| `Income()` | Add a new transaction | Date, Amount, Category |
| `display()` | Print all transactions to console | None |
| `export()` | Convert transactions to list of dicts for JSON | None |

**Workflow Example:**
```
1. Create Transaction_manager (empty, head=None)
2. Call Income() → Creates first Transaction node → Sets as head
3. Call Income() → Creates new node → Links to end of list
4. Call display() → Traverses list, prints each transaction
5. Call export() → Converts to dict format for saving
```

---

### 3. **Account Class** (`accounts/manager.py`)

**Purpose:** Represents a user account with its associated transactions.

**Structure:**
```python
class Account:
    ACC_Name: str               # Account holder name
    next: Account               # Pointer to next account
    prev: Account               # Pointer to previous account
    transaction_manager: Txn_manager  # Manages this account's transactions
```

**Key Points:**
- Each account owns its own `Transaction_manager` instance
- Contains account metadata and transaction history
- Part of outer doubly linked list

---

### 4. **Account_Manager Class** (`accounts/manager.py`)

**Purpose:** Manages the doubly linked list of all user accounts.

**Methods:**

| Method | Purpose | Parameters |
|--------|---------|-----------|
| `__init__()` | Initialize empty account list | None |
| `insert()` | Create new account | Account_name (str) |
| `display()` | List all accounts | None |
| `load()` | Find and load specific account | Account_name (str) |
| `save_account()` | Export all data to dictionary format | None |

**Data Flow:**
```
insert("Alice") → Creates Account object → Adds to linked list
display() → Traverses list, shows numbered menu
load("Alice") → Finds account, returns reference
save_account() → Traverses all accounts → Exports transactions → Returns list
```

---

### 5. **Main Application** (`main.py`)

**Purpose:** CLI interface and main application loop.

**Workflow:**

```
START
  │
  ├─► Load existing accounts from Account.json
  │
  ├─► Display Menu:
  │   ├─ 1: Create Account
  │   ├─ 2: Load Account (add transactions)
  │   └─ 3: Delete Account (saves and exits)
  │
  ├─► Option 1: Insert new account
  │
  ├─► Option 2: Load Account
  │   ├─ Display all accounts
  │   ├─ Select account
  │   ├─ Prompt for transactions
  │   ├─ For each transaction:
  │   │   ├─ Get Date (YYYY-MM-DD)
  │   │   ├─ Choose Category (numbered list)
  │   │   ├─ Enter Amount
  │   │   └─ Add to Transaction_manager
  │   ├─ Display all transactions
  │   └─ Return to menu
  │
  ├─► Option 3: Save & Exit
  │   ├─ Export all data
  │   └─ Write to Account.json
  │
  └─► REPEAT
```

---

## Workflow & User Flow

### Complete User Workflow Example:

```
1. START APPLICATION
   ↓
2. SYSTEM LOADS EXISTING ACCOUNTS from Account.json
   (If accounts exist: auto-populate Account_Manager)
   ↓
3. USER CHOOSES OPTION
   
   OPTION 1: Create Account
   ├─ Input: User name (e.g., "John")
   ├─ Action: a1.insert("John")
   ├─ Result: New Account object added to linked list
   └─ Back to Menu

   OPTION 2: Load Account & Add Transactions
   ├─ Display: List of all accounts (numbered)
   ├─ Input: Account name to load
   ├─ Action: person = a1.load("John")
   ├─ Prompt: Add transactions? (Y/N)
   ├─ If YES:
   │  ├─ Loop:
   │  │  ├─ Input: Date (YYYY-MM-DD format)
   │  │  ├─ Display: Category menu (1-6 options)
   │  │  ├─ Input: Category choice
   │  │  ├─ Input: Transaction amount
   │  │  ├─ Action: person.transaction_manager.Income(date, amount, category)
   │  │  ├─ Prompt: Add another? (Y/N)
   │  │  └─ If NO: display() all transactions & return to menu
   │  └─ End Loop
   └─ Back to Menu

   OPTION 3: Delete Account (Save & Exit)
   ├─ Action: a1.save_account()
   ├─ Action: Export to Account.json
   ├─ Result: All data persisted
   └─ EXIT APPLICATION
```

---

## File Structure

```
personal_finance_manager/
├── pf_notes.md                    # Architecture documentation
├── PROJECT_DOCUMENTATION.md       # This file
│
└── FinanceProject/
    ├── main.py                    # Main entry point & CLI interface
    ├── Account.json               # Persistent data storage (JSON)
    │
    ├── accounts/
    │   ├── __init__.py            # Package init (empty)
    │   └── manager.py             # Account & Account_Manager classes
    │
    └── transaction/
        ├── __init__.py            # Package init (empty)
        └── transactions.py        # Transaction & Transaction_manager classes
```

### Data Persistence

**Account.json Structure:**
```json
[
    {
        "Account Name": "user_name",
        "Transactions": [
            {
                "Date": "2026-01-15",
                "Category": "Food",
                "Amount": "1500"
            },
            {
                "Date": "2026-01-16",
                "Category": "Transport",
                "Amount": "50"
            }
        ]
    }
]
```

---

## Current Issues & Bugs

### 🔴 Critical Issues

1. **JSON Data Integrity Problem**
   - **Location:** `main.py` → `load()` method
   - **Issue:** When loading accounts from JSON, the data structure doesn't match what's being saved
   - **Current:** Saves `["Date", "Category", "Amount"]`
   - **Expected:** Should save `["Date", "Amount", "Category"]` or maintain consistent order
   - **Impact:** Data retrieved is in wrong order

2. **Parameter Order Mismatch**
   - **Location:** `transactions.py` → `Income()` method
   - **Issue:** Created as `Transaction(Date, Amount, Category)` but in Account.json stored as `Category, Amount, Amount`
   - **Impact:** Transaction data gets corrupted during save/load cycle

3. **Type Inconsistency**
   - **Location:** Multiple files
   - **Issue:** Amount is stored as string in JSON but used as int in some places
   - **Impact:** Calculations and comparisons may fail

### 🟡 Medium Issues

4. **No Input Validation**
   - **Missing:** Validation for negative amounts, duplicate accounts
   - **Impact:** System can store invalid data

5. **Incomplete Date Validation**
   - **Location:** `main.py` → Date input
   - **Issue:** Tries to validate but doesn't prevent invalid entry from proceeding
   - **Impact:** Invalid dates can be added to transactions

6. **Typo in main.py**
   - **Location:** Line 47 in main.py: `"Do yyou wanna add transaction"` (typo: "yyou")

7. **Category Assignment Wrong**
   - **Location:** `main.py` line 57
   - **Issue:** Category index stored instead of category name
   - **Fixed on line 61:** `b=Cateogory[b-1]` correctly assigns the name
   - **Bug:** Original issue was storing index instead of string

### 🟢 Minor Issues

8. **No Account Deletion**
   - **Feature Missing:** Option 3 just saves & exits, doesn't actually delete
   - **Feature Request:** Implement account deletion functionality

9. **No Error Handling for File Operations**
   - **Location:** `main.py` → JSON load/save
   - **Missing:** Try-except blocks for file I/O errors

10. **Display Formatting**
    - **Issue:** Transaction display is not well-formatted (no separator between transactions)
    - **Location:** `transactions.py` → `display()` method

---

## Technical Details

### Memory / Data Structure Efficiency

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Create Account | O(1) | O(1) |
| Add Transaction | O(n) | O(1) |
| Find Account | O(m) | O(1) |
| Display Accounts | O(m) | O(1) |
| Display Transactions | O(n) | O(1) |
| Save All Data | O(m × n) | O(m × n) |

*m = number of accounts, n = number of transactions per account*

### Class Relationships

```
Account_Manager (Outer Manager)
    │
    ├─ head: Account
    │
    └─ Each Account object contains:
       └─ transaction_manager: Transaction_manager (Inner Manager)
           │
           └─ head: Transaction
              │
              └─ Each Transaction has:
                 ├─ Date: str
                 ├─ Amount: str
                 ├─ Category: str
                 ├─ next: Transaction
                 └─ prev: Transaction
```

### Key Design Decisions

1. **Doubly Linked List:**
   - ✅ Allows forward and backward traversal
   - ✅ Easy insertion/deletion at any point
   - ❌ No random access (O(n) to find element)

2. **Nested Structure:**
   - ✅ Each account is independent
   - ✅ Separates concerns (accounts vs transactions)
   - ❌ More complex than single-level list

3. **String Storage:**
   - ✅ Compatible with JSON serialization
   - ❌ Requires type conversion for calculations
   - ❌ Less type-safe than numeric types

---

## Summary

This Personal Finance Manager demonstrates:
- **LinkedList Implementation:** Two levels of doubly linked lists
- **Data Persistence:** JSON-based storage and retrieval
- **Object-Oriented Design:** Separate classes for Account/Transaction management
- **CLI Interface:** Interactive menu-driven user interface

**Next Steps for Improvement:**
1. Fix data integrity issues (parameter ordering)
2. Add input validation for amounts and dates
3. Implement proper account deletion
4. Improve error handling for file operations
5. Add summary/analytics features (total spending, category breakdown)
6. Convert amounts to numeric types (float/Decimal)
7. Add unit tests


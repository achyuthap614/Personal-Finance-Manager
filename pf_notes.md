# 📋 Personal Finance Manager — Code Notes

## 1. Overview

This is a **Personal Finance Management System** built using a **Nested Doubly Linked List (DLL)** data structure in Python.

The system has **two layers**:

| Layer | Data Structure | Purpose |
|-------|---------------|---------|
| **Outer DLL** | Linked list of `Account` nodes | Manages all user accounts |
| **Inner DLL** | Linked list of `Transaction` nodes | Manages transactions per account |

Each `Account` node contains its own independent `Transaction` linked list — this is
what makes it a **nested** doubly linked list.

---

## 2. Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        PERSONAL FINANCE MANAGER                                 │
│                                                                                 │
│  Account_Manager (a1)                                                           │
│  ┌────────────────────────────────────────────────────────────────────────────┐  │
│  │                     OUTER DOUBLY LINKED LIST (Accounts)                    │  │
│  │                                                                            │  │
│  │  head                                                                      │  │
│  │   │                                                                        │  │
│  │   ▼           next           next           next                           │  │
│  │ ┌──────┐   ──────────►   ┌──────┐   ──────────►   ┌──────┐                │  │
│  │ │Acc A │                 │Acc B │                 │Acc C │                │  │
│  │ └──────┘   ◄──────────   └──────┘   ◄──────────   └──────┘                │  │
│  │   │           prev           │          prev          │                    │  │
│  │   │ sub_head                 │ sub_head               │ sub_head           │  │
│  │   ▼                         ▼                         ▼                    │  │
│  │ ┌────────────────┐    ┌────────────────┐    ┌────────────────┐             │  │
│  │ │ INNER DLL      │    │ INNER DLL      │    │ INNER DLL      │             │  │
│  │ │ (Transactions) │    │ (Transactions) │    │ (Transactions) │             │  │
│  │ │                │    │                │    │                │             │  │
│  │ │ head           │    │ head           │    │ head           │             │  │
│  │ │  │             │    │  │             │    │  (empty/None)  │             │  │
│  │ │  ▼             │    │  ▼             │    │                │             │  │
│  │ │ ┌─────┐  next  │    │ ┌─────┐        │    └────────────────┘             │  │
│  │ │ │Txn 1│──────► │    │ │Txn 1│        │                                  │  │
│  │ │ └─────┘◄────── │    │ └─────┘        │                                  │  │
│  │ │  │       prev  │    └────────────────┘                                  │  │
│  │ │  ▼ next        │                                                        │  │
│  │ │ ┌─────┐        │                                                        │  │
│  │ │ │Txn 2│        │                                                        │  │
│  │ │ └─────┘        │                                                        │  │
│  │ └────────────────┘                                                        │  │
│  └────────────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Class Diagram

```
┌──────────────────────────┐          ┌────────────────────────────┐
│     Account_Manager      │          │     Transaction_manager    │
├──────────────────────────┤          ├────────────────────────────┤
│ - head: Account | None   │          │ - head: Transaction | None │
├──────────────────────────┤          ├────────────────────────────┤
│ + insert(ACC_Name)       │          │ + Income(Date, Amt, Cat)   │
│ + display()              │          │ + display()                │
│ + load(find) -> Account  │          └──────────┬─────────────────┘
└──────────┬───────────────┘                     │
           │ manages                             │ manages
           ▼                                     ▼
┌──────────────────────────┐          ┌────────────────────────────┐
│        Account           │          │       Transaction          │
├──────────────────────────┤          ├────────────────────────────┤
│ - ACC_Name: str          │          │ - Date: str                │
│ - next: Account | None   │          │ - Amount: str              │
│ - prev: Account | None   │          │ - Category: str            │
│ - sub_head: Txn_manager ─┼────────► │ - next: Transaction | None │
└──────────────────────────┘  owns    │ - prev: Transaction | None │
                                      └────────────────────────────┘
```

**Key relationship:** Each `Account` node **owns** a `Transaction_manager`
through `self.sub_head`, which in turn manages a DLL of `Transaction` nodes.

---

## 4. Class-by-Class Breakdown

### 4.1 `Transaction` Node (Line 46)

This is the **inner node** — each instance represents a single financial transaction.

```python
class Transaction():
    def __init__(self, Date, Amount, Category):
        self.Date = Date           # Date of the transaction
        self.Amount = Amount       # Transaction amount
        self.Category = Category   # Category (e.g., Food, Rent, Salary)
        self.next = None           # Pointer to the NEXT transaction node
        self.prev = None           # Pointer to the PREVIOUS transaction node
```

**Variable mapping:**

| Variable | Type | Purpose |
|----------|------|---------|
| `self.Date` | `str` | Stores the date of the transaction |
| `self.Amount` | `str` | Stores the transaction amount |
| `self.Category` | `str` | Stores the category (Food, Rent, etc.) |
| `self.next` | `Transaction` or `None` | Forward pointer to the next transaction |
| `self.prev` | `Transaction` or `None` | Backward pointer to the previous transaction |

**Single Transaction Node:**
```
         ┌───────────────────────────┐
         │       Transaction         │
         ├───────────────────────────┤
  prev ◄─┤  prev                    │
         │  Date = "2026-03-20"      │
         │  Amount = "5000"          │
         │  Category = "Salary"      │
         │                    next ──┼─► next
         └───────────────────────────┘
```

---

### 4.2 `Transaction_manager` (Line 53)

This is the **inner list manager** — each `Account` has one of these to manage its transactions.

```python
class Transaction_manager:
    def __init__(self):
        self.head = None    # Points to the FIRST Transaction node
```

| Variable | Type | Purpose |
|----------|------|---------|
| `self.head` | `Transaction` or `None` | Points to the first transaction in this account's list |

**Methods:**

#### `Income(Date, Amount, Category)` — Adds a transaction

```
Step-by-step:
1. Create new Transaction node: tran = Transaction(Date, Amount, Category)
2. If list is empty (head is None):
      head ──► tran          (tran becomes the head)
3. If list is NOT empty:
      Traverse to the last node using temp
      Link the new node at the end:
         temp.next = tran    (last node points forward to new node)
         tran.prev = temp    (new node points backward to last node)
```

**Diagram — Adding 3 transactions:**
```
After 1st insert:   head ──► [Txn1]

After 2nd insert:   head ──► [Txn1] ⇄ [Txn2]

After 3rd insert:   head ──► [Txn1] ⇄ [Txn2] ⇄ [Txn3]

( ⇄ means both next and prev pointers are linked )
```

#### `display()` — Prints all transactions

Traverses from `head` to the end, printing each transaction's Date, Amount, and Category.

---

### 4.3 `Account` Node (Line 4)

This is the **outer node** — each instance represents a user account.

```python
class Account:
    def __init__(self, ACC_Name):
        self.ACC_Name = ACC_Name               # Account holder's name
        self.next = None                        # Pointer to the NEXT account
        self.prev = None                        # Pointer to the PREVIOUS account
        self.sub_head = Transaction_manager()   # ★ THE NESTING LINK ★
```

| Variable | Type | Purpose |
|----------|------|---------|
| `self.ACC_Name` | `str` | Name of the account holder |
| `self.next` | `Account` or `None` | Forward pointer to the next account |
| `self.prev` | `Account` or `None` | Backward pointer to the previous account |
| `self.sub_head` | `Transaction_manager` | **🔑 THE NESTING LINK** — each account holds its own transaction list |

**Single Account Node:**
```
         ┌──────────────────────────────────┐
         │           Account                │
         ├──────────────────────────────────┤
  prev ◄─┤  prev                           │
         │  ACC_Name = "Alice"              │
         │  sub_head ──► Transaction_manager│
         │                          next ───┼─► next
         └────────────────┬─────────────────┘
                          │
                          ▼
                  Transaction_manager
                  (its own DLL of transactions)
```

**⭐ This is where the nesting happens:**

`self.sub_head = Transaction_manager()` creates a **separate, independent** transaction
linked list embedded inside each Account node. This is what makes this a
**nested doubly linked list**.

---

### 4.4 `Account_Manager` (Line 11)

This is the **outer list manager** — manages the DLL of all Account nodes.

```python
class Account_Manager:
    def __init__(self):
        self.head = None    # Points to the FIRST Account node
```

| Variable | Type | Purpose |
|----------|------|---------|
| `self.head` | `Account` or `None` | Points to the first account in the list |

**Methods:**

#### `insert(ACC_Name)` — Creates a new account

```
Step-by-step:
1. Create new Account node: names = Account(ACC_Name)
2. If list is empty (head is None):
      head ──► names         (names becomes the head)
3. If list is NOT empty:
      Traverse to the last node using temp
      Link the new node at the end:
         temp.next = names   (last node points forward to new node)
         names.prev = temp   (new node points backward to last node)
```

#### `display()` — Lists all accounts

Uses a counter `i` to show account indices:
```
0. Alice
1. Bob
2. Charlie
```

#### `load(find)` — Finds and returns an account by name

Searches linearly through the DLL until `temp.ACC_Name == find`,
then returns that `Account` node. This returned node gives access to its
`sub_head` (Transaction_manager).

---

## 5. Main Loop Variables (Line 72+)

| Variable | Type | Purpose |
|----------|------|---------|
| `a1` | `Account_Manager` | The **single** Account_Manager instance — manages all accounts |
| `choice` | `int` | User's menu choice (1 = Create, 2 = Load, 3 = Delete/Exit) |
| `name` | `str` | User input for new account name |
| `choose_Acc` | `str` | User input for which account to load |
| `person` | `Account` | The returned Account node from `a1.load()` |
| `a` | `str` | User input for transaction **Date** |
| `b` | `str` | User input for transaction **Category** |
| `c` | `str` | User input for transaction **Amount** |
| `d` | `str` | User input — "Y" to add more transactions, anything else to stop |

---

## 6. How Account ↔ Transaction Linking Works

The critical line that connects accounts to transactions:

```python
# Inside the Account class:
self.sub_head = Transaction_manager()
```

**When you add a transaction, here's the full chain:**

```python
person.sub_head.Income(a, b, c)
```

```
person              →  The loaded Account node (e.g., "Alice")
  │
  ├── .sub_head     →  Alice's Transaction_manager instance
  │     │
  │     ├── .head   →  First Transaction in Alice's list
  │     │
  │     └── .Income(a, b, c)  →  Adds a new Transaction node to Alice's list
  │
  ├── .ACC_Name     →  "Alice"
  ├── .next         →  Next Account node (e.g., "Bob")
  └── .prev         →  Previous Account node (or None if first)
```

**Full linkage flow diagram:**

```
 a1 (Account_Manager)
  │
  │ .head
  ▼
┌────────────┐  next   ┌────────────┐  next   ┌────────────┐
│ Account    │ ──────► │ Account    │ ──────► │ Account    │
│ "Alice"    │ ◄────── │ "Bob"      │ ◄────── │ "Charlie"  │
│            │  prev   │            │  prev   │            │
│ sub_head───┤         │ sub_head───┤         │ sub_head───┤
└────────────┘         └────────────┘         └────────────┘
      │                      │                      │
      ▼                      ▼                      ▼
 Txn_Manager            Txn_Manager            Txn_Manager
      │                      │                      │
      │ .head                │ .head                │ .head = None
      ▼                      ▼                      (no transactions)
 ┌─────────┐  next      ┌─────────┐
 │ Txn 1   │ ──────►    │ Txn 1   │
 │ Mar-01  │ ◄──────    │ Mar-15  │
 │ +5000   │  prev      │ +8000   │
 │ Salary  │            │ Salary  │
 └─────────┘            └─────────┘
      │ next
      ▼
 ┌─────────┐
 │ Txn 2   │
 │ Mar-05  │
 │ -500    │
 │ Food    │
 └─────────┘
      │ next
      ▼
 ┌─────────┐
 │ Txn 3   │
 │ Mar-10  │
 │ -2000   │
 │ Rent    │
 └─────────┘
```

---

## 7. Program Flow Diagram

```
                    ┌──────────────────────┐
                    │       START          │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │   Display Main Menu   │
                    │  1. Create Account    │
                    │  2. Load Account      │
                    │  3. Delete (Exit)     │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │   Get User Choice     │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
       choice == 1      choice == 2      choice == 3
              │                │                │
              ▼                ▼                ▼
     ┌────────────────┐ ┌──────────────┐ ┌──────────┐
     │ Get name input │ │ Display all  │ │  EXIT    │
     │ Call a1.insert │ │  accounts    │ └──────────┘
     │   (name)       │ └──────┬───────┘
     └────────────────┘        │
                               ▼
                      ┌────────────────┐
                      │ Load account?  │
                      │   (Y/N)        │
                      └───────┬────────┘
                              │ Y
                              ▼
                      ┌────────────────┐
                      │ a1.load(name)  │
                      │ returns:person │
                      └───────┬────────┘
                              │
                              ▼
                      ┌────────────────┐
                      │ Add txn? (Y/N) │
                      └───────┬────────┘
                              │ Y
                              ▼
                    ┌──────────────────┐
                    │ Enter Date (a)    │
                    │ Enter Category(b) │
                    │ Enter Amount (c)  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────────────┐
                    │ person.sub_head.Income    │
                    │         (a, b, c)        │
                    └────────┬─────────────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Add more? (Y/N)  │──── Y ──► (loop back to Enter Date)
                    └────────┬─────────┘
                             │ N
                             ▼
                    ┌──────────────────────────┐
                    │ person.sub_head.display() │
                    │ (print all transactions)  │
                    └──────────────────────────┘
```

---

## 8. Time Complexity Analysis

| Operation | Method | Time Complexity | Explanation |
|-----------|--------|-----------------|-------------|
| Create Account | `Account_Manager.insert()` | **O(n)** | Traverses the entire account list to find the last node. `n` = number of accounts |
| Display Accounts | `Account_Manager.display()` | **O(n)** | Visits every account node once |
| Load/Find Account | `Account_Manager.load()` | **O(n)** | Linear search through accounts by name (worst case: last account) |
| Add Transaction | `Transaction_manager.Income()` | **O(m)** | Traverses the transaction list to find the last node. `m` = number of transactions in that account |
| Display Transactions | `Transaction_manager.display()` | **O(m)** | Visits every transaction node in that account |

### Potential Optimization

Both `insert()` and `Income()` could be improved from **O(n)** / **O(m)** to **O(1)**
by maintaining a **tail pointer** in both manager classes:

```python
# Example optimization:
class Account_Manager:
    def __init__(self):
        self.head = None
        self.tail = None    # ← Add tail pointer

    def insert(self, ACC_Name):
        names = Account(ACC_Name)
        if self.head is None:
            self.head = names
            self.tail = names       # ← Track tail
        else:
            self.tail.next = names  # ← Direct access to end
            names.prev = self.tail
            self.tail = names       # ← Update tail
```

---

## 9. Space Complexity Analysis

| Component | Space | Explanation |
|-----------|-------|-------------|
| `Account_Manager` | **O(1)** | Only stores one `head` pointer |
| Each `Account` node | **O(1)** | Fixed fields: `ACC_Name`, `next`, `prev`, `sub_head` |
| `Transaction_manager` | **O(1)** | Only stores one `head` pointer |
| Each `Transaction` node | **O(1)** | Fixed fields: `Date`, `Amount`, `Category`, `next`, `prev` |
| **Overall** | **O(n + M)** | `n` = total accounts, `M` = total transactions across ALL accounts |

### Space Breakdown

```
Total Space = (n × Account node size) + (M × Transaction node size) + (n × Txn_Manager size)
            = O(n + M)

Where:
  n = number of Account nodes
  M = sum of all transactions across all accounts
    = m₁ + m₂ + m₃ + ... + mₙ
    (mᵢ = number of transactions in account i)
```

### DLL vs SLL Space Overhead

A **Doubly Linked List** uses **2 pointers per node** (`next` + `prev`), while a
**Singly Linked List** uses only 1 (`next`). This is a small constant space
trade-off that enables **O(1) backward traversal** and **O(1) deletion** of a
node when you have a reference to it.

---

## 10. Summary Table

| Concept | Implementation Detail |
|---------|----------------------|
| **Outer DLL** | `Account_Manager` manages `Account` nodes via `head` pointer |
| **Inner DLL** | `Transaction_manager` manages `Transaction` nodes via `head` pointer |
| **Nesting Link** | `Account.sub_head = Transaction_manager()` — each account owns a transaction list |
| **Access Chain** | `person.sub_head.Income(...)` chains Account → Txn_Manager → Transaction |
| **Time (insert)** | O(n) accounts, O(m) transactions — improvable with tail pointers |
| **Space** | O(n + M) total, where M = all transactions across all accounts |

# Lab 7 — Introduction to Python

## Structure

```
lab7/
├── task1/
│   ├── informatics/
│   │   └── solutions.py      # All Informatics.msk.ru problems
│   ├── hackerrank/
│   │   └── solutions.py      # 10 HackerRank Python problems
│   └── codingbat/
│       └── solutions.py      # All CodingBat sections
└── task2/
    ├── models.py             # Animal, Dog, Cat classes
    ├── main.py               # Demo script
    └── README.md
```

---

## Task 1 — Coding Challenges

### Informatics.msk.ru (`task1/informatics/solutions.py`)
| Section | Problems |
|---|---|
| Input/Output & Assignment Operators | A – E |
| Conditional Statements | A – E |
| For Loop | A – M |
| While Loop | A – E |
| Arrays (Lists) | A – G |
| Functions | A – C |

### HackerRank (`task1/hackerrank/solutions.py`)
Ten problems from the Python domain covering:
1. Hello World
2. If-Else
3. Arithmetic Operators
4. Division
5. Loops
6. Print Function
7. List Comprehensions
8. Runner-Up Score
9. Nested Lists
10. Finding the Percentage

### CodingBat (`task1/codingbat/solutions.py`)
All six sections completed:
- Warmup-1
- Warmup-2
- String-1
- String-2
- List-1
- List-2

---

## Task 2 — Object-Oriented Programming

### Class Hierarchy

```
Animal          ← base class
├── Dog         ← child class (adds breed, is_trained, fetch())
└── Cat         ← child class (adds color, indoor, purr())
```

### `Animal` (base class)
| Member | Type | Description |
|---|---|---|
| `name` | attribute | Animal's name |
| `age` | attribute | Age in years |
| `species` | attribute | Species name |
| `speak()` | method | Generic sound (overridden by children) |
| `describe()` | method | Human-readable description |
| `birthday()` | method | Increments age by 1 |
| `__str__()` | dunder | String representation |

### `Dog(Animal)`
Extra: `breed`, `is_trained`
Override: `speak()` → *"Woof! 🐕"*
New: `fetch(item)`

### `Cat(Animal)`
Extra: `color`, `indoor`
Override: `speak()` → *"Meow~ 🐈"*
New: `purr()`

---

## How to Run

```bash
# Run OOP demo
python task2/main.py

# Run HackerRank demos
python task1/hackerrank/solutions.py

# Run CodingBat demos
python task1/codingbat/solutions.py
```

---

## OOP Concepts Demonstrated

| Concept | Where |
|---|---|
| Classes & constructors (`__init__`) | `models.py` — all classes |
| Instance methods | `speak()`, `describe()`, `birthday()`, `fetch()`, `purr()` |
| `__str__` dunder | All three classes |
| Inheritance | `Dog` and `Cat` extend `Animal` |
| Method overriding | `speak()` and `describe()` in both children |
| `super()` | `Dog.__init__`, `Cat.__init__`, `Dog.describe()`, `Cat.describe()` |
| Polymorphism | `main.py` — loop calling `speak()` on mixed list |
| Modules & imports | `main.py` imports from `models.py` |

---

*Follows PEP 8 style guidelines throughout.*

# Holberton School – Higher Level Programming

This repository is a curated, course-style collection of projects covering **higher-level software engineering concepts** typically taught after low-level programming fundamentals.

The content is largely **Python** (core language, OOP, exceptions, I/O, testing, ORM), with complementary modules in **SQL (MySQL)** and **JavaScript** (basics and DOM manipulation). Each directory is intended to be read like a mini-course: theory first, then practical exercises.

> **Audience:** learners who already know basic programming and want to deepen their understanding of abstraction, data structures, OOP design, persistence, and web/API fundamentals.

---

## Repository Structure

Top-level folders represent modules/projects. Typical naming follows Holberton/ALX conventions.

- **Python**
  - `python-hello_world` – first steps: interpreter, printing, strings, numbers
  - `python-if_else_loops_functions` – control flow and functions
  - `python-import_modules` – modules, packages, imports
  - `python-data_structures` – lists/tuples, iteration, basic algorithms
  - `python-more_data_structures` – sets/dicts, functional tools
  - `python-classes` / `python-more_classes` – OOP foundations and deeper OOP
  - `python-inheritance` – subclassing, polymorphism, method resolution
  - `python-exceptions` – error handling and robustness
  - `python-input_output` – files, JSON, serialization patterns
  - `python-test_driven_development` – doctest/unittest and disciplined design
  - `python-object_relational_mapping` – persistence and ORMs (SQL ↔ Python)
  - `python-everything_is_object` – references, mutability, memory model
  - `python-serialization` – data formats, (de)serialization strategy
  - `python-server_side_rendering` – server-side templates/rendering
  - `python-abc` – abstract base classes and interfaces

- **SQL (MySQL)**
  - `SQL_introduction` – DDL/DML, querying, aggregation
  - `SQL_more_queries` – joins, constraints, permissions, advanced querying

- **JavaScript**
  - `javascript-warm_up` – syntax, variables, loops, functions
  - `javascript-dom_manipulation` – DOM APIs, events, client-side interactivity

Each folder contains its own `README.md` explaining:
- learning objectives
- theoretical background
- how to run the exercises
- a guided walkthrough of the tasks

---

## How to Use This Repo

### 1) Clone

```bash
git clone https://github.com/serkam31/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming
```

### 2) Choose a module

Enter a directory (example):

```bash
cd python-hello_world
```

Read the local `README.md` first, then run scripts individually:

```bash
python3 2-print.py
```

---

## Recommended Learning Workflow

1. **Read the README** (theory + mental model).
2. **Inspect the starter code / scripts**.
3. **Run and modify** the programs.
4. **Explain back** (in your own words) what the program demonstrates.
5. **Add tests** where applicable (especially for TDD/OOP modules).

---

## Conventions

- Python scripts are intended for `python3`.
- SQL scripts are intended for MySQL (`mysql` client).
- JavaScript files are typically run with `node` unless they require a browser DOM.

---

## License

This repository is for educational purposes. If you plan to reuse parts publicly, make sure you comply with your school’s policies.